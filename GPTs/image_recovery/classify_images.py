#!/usr/bin/env python3
"""IMG-02: classify every inventoried image reference into class A-E.

Phase-1 classifier for the image content recovery job. Applies cheap
deterministic rules over the inventory `context` column, with a curated
vision-verified override set for the (rare) class-E process flowcharts.

Rules were validated against ~95 rasters opened with the image-reading tool;
see GPTs/reports/image_content_audit_20260522.md for the sampled validation.

Output: GPTs/image_recovery/image_classification.tsv
  ref_id  class  decided_by  rationale  raster_readable

The run is resumable: rows already present in the output file (matched by
ref_id) are kept and not recomputed.
"""
import csv, os, re, sys

INV = 'GPTs/image_recovery/image_inventory.tsv'
OUT = 'GPTs/image_recovery/image_classification.tsv'

# ---------------------------------------------------------------- E override
# Class-E process / decision / state-transition flowcharts confirmed by
# opening the raster. Keyed by ref_id (every reference to the diagram).
E_REFS = set("""
img-00358 img-01493 img-02674 img-03867 img-05004 img-06200
img-00359 img-01494 img-02675 img-03868 img-05005 img-06201
img-00360 img-01495 img-02676 img-03869 img-05006 img-06202
img-00088 img-01213 img-02405 img-03588 img-04735 img-05919
img-00332 img-01476 img-02649 img-03851 img-04979 img-06184
img-07061 img-07163 img-07265 img-07367
img-00124 img-02441 img-04771
img-01250 img-03625 img-05956
img-00460 img-02776 img-05106
img-00461 img-02777 img-05107
img-01597 img-01598 img-03971 img-03972 img-06304 img-06305
""".split())

# Short rationale per E diagram, keyed by basename (or 16-1/4-1/4-2 by heading).
E_RATIONALE = {
    'BASIC_STEPS_IN_QUERY_PROCESSING.gif': 'process flowchart: client/server query-processing pipeline (Parsing-Validation-Optimization-Binding-Execution)',
    'optimizer_structure.gif': 'process flowchart: optimizer pipeline (Query Rewriter -> Logical Plan Generator -> Physical Plan Generator)',
    'data_type_conversion_path_kor.gif': 'directed conversion graph: data-type conversion paths with G/E/L penalty edges',
    'cdba9650f1626e7cc409038702eb8b1d.png': 'decision flowchart: index-type classification by YES/No decision diamonds',
    'basic_use_eng.png': 'process flowchart with loop: Log Analysis API usage steps STEP1..STEP5',
    'basic_use_kor.gif': 'process flowchart with loop: Log Analysis API usage steps STEP1..STEP5',
    'heartbeat_transition.gif': 'state-transition diagram: aheartbeat Ready/Run/Error states',
    'Admin_eng.1.83.1.jpg': 'process flowchart: troubleshooting procedure (check log -> judge -> collect -> analyse)',
    '16-1.png': 'process flowchart: troubleshooting procedure (check log -> judge -> collect -> analyse)',
    'Replication_eng.1.22.1.jpg': 'decision flowchart: replication fail-over with failure branch and retry loop',
    'Replication_eng.1.22.2.jpg': 'process flowchart: fail-over callback sequence (FO_BEGIN/FO_GO/FO_END cases)',
    '4-1.png': 'decision flowchart: replication fail-over with failure branch and retry loop',
    '4-2.png': 'process flowchart: fail-over callback sequence (FO_BEGIN/FO_GO/FO_END cases)',
}


def un(s):
    return s.replace('\\t', '\t').replace('\\n', '\n')


def find_idx(ctx, raw):
    """Return (start, end) of this image's reference inside the context."""
    m = re.search(r'!\[[^\]]*\]\(' + re.escape(raw) + r'\)', ctx)
    if m:
        return m.start(), m.end()
    m = re.search(r'<img[^>]*src="' + re.escape(raw) + r'"[^>]*>', ctx)
    if m:
        return m.start(), m.end()
    return None, None


def classify(r):
    """Return (class, decided_by, rationale)."""
    ctx = un(r['context'])
    raw = r['image_path_raw']
    res = r['image_path_resolved']
    h = r['heading_chain']
    bn = r['basename']
    last_head = h.split(' > ')[-1].strip()

    # 3 - class-E override (vision-verified flowcharts), checked early so it
    #     always wins over the syntax/residual rules.
    if r['ref_id'] in E_REFS:
        rat = E_RATIONALE.get(bn) or E_RATIONALE.get(bn.lower()) \
            or 'process/decision flowchart (vision-verified)'
        return 'E', 'vision', rat

    # 1 - cover page logo / decorative common asset.
    if 'common/' in raw or 'common/' in res:
        return 'B', 'rule-cover', 'cover-page logo, carries no recoverable text'

    s, e = find_idx(ctx, raw)

    # 2 - image sits inside a Markdown table cell: legend symbol or UI icon
    #     whose meaning is in the adjacent cell.
    if s is not None:
        lstart = ctx.rfind('\n', 0, s) + 1
        lend = ctx.find('\n', e)
        imgline = ctx[lstart:(lend if lend >= 0 else len(ctx))]
        if imgline.lstrip().startswith('|'):
            return ('B', 'rule-table-cell',
                    'symbol/icon in a table cell, explained by the adjacent cell')

    # 4 - hint railroad diagram (Hint List section): one railroad per hint,
    #     grammar exists only in the image.
    if re.search(r'Hint List|힌트 목록|힌트 리스트', h):
        return ('C', 'rule-hint',
                'hint railroad diagram, only source of the hint grammar')

    before = ctx[:s] if s is not None else ''
    after = ctx[e:] if s is not None else ''

    # 5 - image followed by a text Syntax/구문 code block: redundant syntax
    #     diagram (class A).
    if after and re.search(r'#+\s*(Syntax|구문)\s*\n+```', after[:450]):
        return ('A', 'rule-syntax-textblock',
                'syntax diagram redundant with the adjacent text Syntax block')

    # last non-empty line before the image
    pl = [l for l in before.split('\n') if l.strip()]
    last = pl[-1].strip() if pl else ''
    last_norm = re.sub(r'\s+', '', last).replace('*', '')

    # 6 - data-type "Syntax Diagram"/"흐름도" page with no text block -> the
    #     railroad is the only grammar (class C).
    if last_head in ('Syntax Diagram', '흐름도'):
        return ('C', 'rule-syntaxdiagram-head',
                'data-type syntax diagram, grammar not given as text')

    # 7 - railroad diagram preceded by a "<symbol> ::=" BNF label.
    if last_norm.endswith('::='):
        return ('C', 'rule-railroad-bnf',
                'railroad diagram for a ::= grammar production, image-only grammar')

    # 8 - image is the first element under a "Syntax"/"구문" heading.
    if re.match(r'#+\s*(Syntax|구문)\s*$', last):
        return ('C', 'rule-railroad-synhead',
                'railroad diagram directly under a Syntax heading, image-only grammar')

    # 9 - reference lives in a section whose leaf heading is Syntax/구문.
    if last_head in ('Syntax', '구문'):
        return ('C', 'rule-railroad-synsection',
                'railroad diagram in a Syntax section, image-only grammar')

    # 10 - residual: conceptual diagram / GUI screenshot / illustration /
    #      architecture or class diagram. Redundant with surrounding prose.
    #      Default validated by a vision sample of ~95 rasters (see audit).
    return ('B', 'rule-residual-conceptual',
            'conceptual/architecture diagram, screenshot or illustration redundant with prose')


def main():
    inv = list(csv.DictReader(open(INV, encoding='utf-8'), delimiter='\t'))

    done = {}
    if os.path.exists(OUT):
        for row in csv.DictReader(open(OUT, encoding='utf-8'), delimiter='\t'):
            done[row['ref_id']] = row

    out_rows = []
    for r in inv:
        rid = r['ref_id']
        if rid in done:
            out_rows.append(done[rid])
            continue
        cls, by, rat = classify(r)
        readable = 'missing' if r['image_path_resolved'].strip() == '' else 'yes'
        out_rows.append({'ref_id': rid, 'class': cls, 'decided_by': by,
                         'rationale': rat, 'raster_readable': readable})

    with open(OUT, 'w', encoding='utf-8', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['ref_id', 'class', 'decided_by',
                                          'rationale', 'raster_readable'],
                           delimiter='\t')
        w.writeheader()
        for row in out_rows:
            w.writerow(row)

    print('classified %d rows -> %s' % (len(out_rows), OUT))
    from collections import Counter
    print('class counts :', dict(Counter(x['class'] for x in out_rows)))
    print('decided_by   :', dict(Counter(x['decided_by'] for x in out_rows)))
    print('raster_readable:', dict(Counter(x['raster_readable'] for x in out_rows)))


if __name__ == '__main__':
    sys.exit(main())
