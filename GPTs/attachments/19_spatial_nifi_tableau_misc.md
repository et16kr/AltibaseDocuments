# 19. Spatial, NiFi, Tableau, and Miscellaneous Integrations

## Applicable Versions

- 7.1: Based on Spatial SQL and base integration documents.
- 7.3: Based on Spatial SQL, altiShapeLoader, NiFi, and Tableau guidance.
- 8.1: Based on Altibase 8.1 verified source Spatial and integration documents.

## Questions This File Can Answer

- How are Spatial SQL and the GEOMETRY type used?
- How are Shapefiles imported or exported?
- What is the procedure for connecting Altibase from NiFi?
- How is Altibase data queried from Tableau?

## Source Documents

- 7.1: Altibase 7.1 Spatial SQL Reference.
- 7.3: Altibase 7.3 Spatial SQL Reference; altiShapeLoader User's Manual; NiFi User's Guide for Altibase; Tableau User's Guide for Altibase.
- 8.1: Altibase 8.1 verified source Spatial SQL Reference; altiShapeLoader User's Manual; NiFi User's Guide for Altibase; Tableau User's Guide for Altibase.

## Core Guidance

- Spatial answers should consider the GEOMETRY type, SRID, WKT/WKB/EWKB, spatial functions, and load/export tools together.
- For NiFi and Tableau, prioritize connection properties, drivers, procedures, and error handling over screenshots.

## Version Differences

- 7.1: Use 7.1 Spatial SQL behavior and base integration guidance for 7.1 answers.
- 7.3: Include 7.3 Spatial SQL, altiShapeLoader, NiFi, and Tableau guidance when relevant.
- 8.1: Use Altibase 8.1 verified source for Spatial and integration guidance.

## Conversion TODO

- Organize spatial functions by `Function Name`, `Purpose`, `Input`, `Output`, and `Example`.
- Build import/export cookbook entries for altiShapeLoader procedures.
- Replace NiFi and Tableau screenshots with descriptive procedures.
