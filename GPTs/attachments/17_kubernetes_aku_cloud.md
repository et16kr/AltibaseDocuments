# 17. Kubernetes and AKU

## Applicable Versions

- 7.1: Based on Altibase 7.1 operations, replication, Utilities Manual AKU guidance, and the AKU sample guide. AKU supports up to 4 scalable replicas in the 7.1 Utilities Manual and AKU sample guide.
- 7.3: Based on Kubernetes User's Guide for Altibase, Altibase AKU Sample Guide for Kubernetes, Altibase 7.3 utilities guidance, and Altibase 7.3 release notes. AKU supports up to 6 scalable replicas in the 7.3 documentation.
- 8.1: Based on Altibase 8.1 verified source Kubernetes, AKU, utilities, and release-note guidance. AKU supports up to 6 scalable replicas; the release notes also call out AKU multiple replication configuration support and performance improvements.

## Questions This File Can Answer

- How should Altibase be deployed on Kubernetes?
- Which source-backed container image, `MODE`, environment, volume, ConfigMap, and Service patterns appear in the Altibase Kubernetes guides?
- When should I use a simple `Pod` or `Deployment`, and when should I use a `StatefulSet`?
- What does AKU do during Pod startup, shutdown, scale-up, and scale-down?
- Which Kubernetes objects, ports, persistent storage, probes, and services are needed for AKU?
- What bootstrap steps are needed before the first AKU-managed Pod becomes ready?
- How should Altibase replication be configured when Pod IP addresses are dynamic?
- How can I verify that AKU synchronization and replication reset completed?
- What cautions apply to abnormal Pod termination, master Pod failure, and accumulated replication logs?

## Retrieval Alias Index

Use this compact index before scanning Kubernetes and AKU runbooks. It is intentionally redundant with later headings so lexical retrieval can land on the exact Pod, Deployment, StatefulSet, Service, AKU lifecycle, replication, or cleanup block.

- Aliases and customer wording: Altibase on Kubernetes, container deployment, Pod, Deployment, StatefulSet, headless Service, ConfigMap, PVC, startupProbe, AKU, scale up, scale down, Pod termination, master Pod failure, dynamic Pod IP, Kubernetes replication.
- Exact-token anchors: `Pod`, `Deployment`, `StatefulSet`, `Service`, `ConfigMap`, `PersistentVolumeClaim`, `podManagementPolicy: OrderedReady`, `publishNotReadyAddresses: true`, `startupProbe`, `/tmp/aku_start_completed`, `terminationGracePeriodSeconds`, `MODE=daemon`, `MODE=replication`, `AKU_SERVER_COUNT`, `REPLICATIONS`, `aku -p start`, `aku -p end`, `aku -p clean`, `AKU_REPLICATION_RESET_AT_END`, `AKU started with START option.`, `Replication sync has ended.`, `AKU run successfully.`, `AKU started with END option.`
- Focused routing anchors: AKU lifecycle questions route to `Exact block: AKU purpose and scale-out boundary`, `Exact block: StatefulSet controls for safe startup`, and `Exact block: safe shutdown and abnormal termination`; keep `AKU_SERVER_COUNT`, `1`, `6`, `aku -p start`, `aku -p end`, `OrderedReady`, `startupProbe`, `/tmp/aku_start_completed`, `publishNotReadyAddresses: true`, `terminationGracePeriodSeconds`, `altiEncrypt`, `REPLICATIONS`, and the expected AKU output strings.
- Answer route: use this file for Kubernetes object patterns and AKU lifecycle; use `09_replication_ha_cdc.md` for replication object SQL and unsafe state changes; use `14_utilities_operation_tools.md` for utility command context; use `18_security_ssl_tls.md` for TLS/certificate placement.
- Stop condition: before production or cleanup commands, ask for Altibase version, Kubernetes version, image, storage class, replica count, target tables, backup status, replication state, downtime window, and recovery plan.

## Source Documents

- 7.1: Altibase 7.1 Installation Guide, Administrator's Manual, Replication Manual, Utilities Manual, and Altibase AKU Sample Guide for Kubernetes.
- 7.3: Kubernetes User's Guide for Altibase; Altibase AKU Sample Guide for Kubernetes; Altibase 7.3 Utilities Manual; Altibase 7.3 Release Notes.
- 8.1: Altibase 8.1 verified source Kubernetes User's Guide for Altibase; Altibase AKU Sample Guide for Kubernetes; Utilities Manual; Altibase 8.1 Release Notes.
- Container guide baselines: the Kubernetes User's Guide examples use Kubernetes `v1.20.4` and the Docker Hub image `altibase/altibase`; the AKU sample guide uses Kubernetes `v1.24.2` with an `ubuntu:18.04` sample image and in-container Altibase installation. Treat those as source examples, not a universal support matrix.

## Response Rules

- Answer explanatory text in the user's language.
- Keep SQL object names, SQL statements, property names, command names, Kubernetes object kinds, YAML keys, file names, paths, ports, and error messages literal.
- For 8.1-specific statements, say `Altibase 8.1 verified source`.
- Do not expose internal source labels, repository paths, workstation paths, original image names, or local source-file locations in customer answers.
- Treat example passwords such as `manager` and example accounts such as `SYS` as placeholders. Recommend Kubernetes `Secret` objects or equivalent protected secret handling.
- Before giving production-ready commands, ask for Altibase version, Kubernetes version, container image, storage class, PV/PVC design, license basis, replica count, replication target tables, backup status, downtime window, and recovery plan.
- For destructive operations such as `TRUNCATE`, `ALTER REPLICATION ... RESET`, `aku -p clean`, or manual master-pod recovery, require a backup and an explicit operator decision.
- Do not depend on installer or console images for this topic. Express Kubernetes and AKU guidance as YAML, commands, Mermaid lifecycle flows, field/value descriptions, and expected results.
- The selected sources do not prescribe a cloud-provider-specific runbook for EKS, GKE, AKS, or managed storage classes. For cloud/container production answers, state the Altibase and AKU requirements from this file, ask for the provider/storage/network details, and route provider-specific provisioning to the platform documentation.

## Fast Decision Map

```mermaid
flowchart TD
  A[Altibase on Kubernetes question] --> B{Goal}
  B -- Quick single server test --> C[Pod or Deployment]
  B -- Stable network endpoint --> D[Service or headless Service]
  B -- Persistent database files --> E[PV and PVC or volume mount]
  B -- Replicated stateful cluster lifecycle --> F[StatefulSet plus AKU]
  B -- Manual two-node replication demo --> G[Deployment plus Service DNS names]
  B -- First AKU startup blocked --> M[Bootstrap first Pod then aku -p start]
  F --> H{Lifecycle action}
  H -- First pod starts --> I[aku -p start as master pod]
  H -- Scale up or restart slave --> J[aku -p start as slave pod]
  H -- Scale down or terminate slave --> K[aku -p end]
  H -- Remove AKU-managed replication --> L[aku -p clean]
```

## J017 AKU Exact Answer Blocks

Use these blocks when a Kubernetes or AKU answer must preserve the literal lifecycle
controls and unsafe-operation cautions.

Exact block: AKU purpose and scale-out boundary

- Version scope: 7.1 Utilities Manual for 1 to 4 Pods; 7.3 and Altibase 8.1 verified
  source Utilities guidance for 1 to 6 Pods.
- `aku` is the Altibase Kubernetes Utility for Kubernetes `StatefulSet` lifecycle
  operations.
- AKU helps synchronize Altibase data or reset synchronization information as Pods
  start, stop, scale up, or scale down.
- AKU uses Altibase replication among Pods, but it does not provide Altibase data
  scale-out.
- `AKU_SERVER_COUNT` defines the maximum number of Altibase servers or Pods that AKU can
  synchronize. For Altibase 8.1 verified source, the valid range is `1` to `6`.

Exact block: StatefulSet controls for safe startup

- Required StatefulSet control: `podManagementPolicy: OrderedReady`.
- Required Service control: headless Service plus `publishNotReadyAddresses: true`.
- Required probe control: `startupProbe` checking `/tmp/aku_start_completed`.
- Required termination control: sufficiently large `terminationGracePeriodSeconds`.
- Runtime order: start the Altibase server first, then run `aku -p start`.
- Startup safety rule: Pods should be created sequentially so several Pods do not run
  `aku -p start` at the same time.
- Expected startup output anchors include `AKU started with START option.`,
  `Replication sync has ended.`, and `AKU run successfully.` If they are absent, inspect
  AKU logs, StatefulSet ordering, and replication state before forcing progress.

Exact block: safe shutdown and abnormal termination

- Runtime order: `aku -p end` must run before the Altibase server stops and must
  complete before Pod termination.
- Expected shutdown output anchor includes `AKU started with END option.` followed by a
  successful AKU exit before the server stop path continues.
- If `aku -p end` does not complete, or if `AKU_REPLICATION_RESET_AT_END=0` leaves
  replication information, replication information may remain on other Pods.
- Long-lived remaining replication information can cause online logs to accumulate for a
  terminated Pod and can exhaust disk space.
- Cleanup/reset is operator-reviewed work: stop and reset the affected replication
  objects only after backup, topology, and recovery evidence are confirmed.
- Do not delete `/tmp/aku_start_completed`, run `aku -p clean`, or issue
  `ALTER REPLICATION ... RESET` as a blind progress fix.

## Version Differences

Version block: 7.1

- The 7.1 Utilities Manual includes `aku` for StatefulSet-based Pod lifecycle assistance.
- `AKU_SERVER_COUNT` can be set from 1 to 4 in the 7.1 Utilities Manual.
- The AKU sample guide uses an Altibase 7.1 test environment and shows a 4-Pod StatefulSet.
- The Kubernetes User's Guide example uses Kubernetes `v1.20.4`, Docker Hub image `altibase/altibase`, and `MODE=daemon` for simple Pod or Deployment tests; the manual replication example uses `MODE=replication` and `SLAVE_REP_PORT=20301`.
- The AKU sample guide uses Kubernetes `v1.24.2`, `ubuntu:18.04`, a ConfigMap-driven entry script, and per-Pod Altibase homes named from `${HOSTNAME}`.
- The 7.1 Utilities Manual documents comma-separated multiple `REPLICATIONS` blocks for splitting replication targets into separate groups.
- Use `StatefulSet` with `podManagementPolicy: OrderedReady`, a headless `Service`, persistent storage, `startupProbe`, and `terminationGracePeriodSeconds` for AKU-based deployments.
- For simple container tests, a `Pod` or `Deployment` can run the Altibase image with `MODE=daemon`, but that pattern does not provide the AKU lifecycle model by itself.

Version block: 7.3

- Altibase 7.3 release notes identify AKU as a utility for synchronizing data or resetting synchronization information when Pods start or terminate in a StatefulSet.
- `AKU_SERVER_COUNT` can be set from 1 to 6 in the 7.3 documentation.
- The 7.3 utilities guidance keeps the same AKU lifecycle model: master pod, slave pod, `aku -p start`, `aku -p end`, `aku -p clean`, and `aku.conf`.
- The 7.3 Utilities Manual documents comma-separated multiple `REPLICATIONS` blocks for splitting replication targets into separate groups.
- The Kubernetes guide shows Pod, Deployment, Service, persistent volume, and manual replication examples. For production-style lifecycle management, prefer the AKU StatefulSet pattern.
- The Kubernetes and AKU sample YAML fields remain example patterns; verify the target Kubernetes version and storage class before using them in production.

Version block: 8.1

- Use the wording `Altibase 8.1 verified source` for 8.1-specific AKU and Kubernetes statements.
- The Altibase 8.1 verified source supports scale-up to 6 nodes.
- The Altibase 8.1 verified source release notes call out multiple replication configuration support in `REPLICATIONS`, and the Utilities Manual keeps the same comma-separated block shape documented for 7.1 and 7.3.
- The Altibase 8.1 verified source release notes mention multi-thread based parallel processing improvements and longer user, table, and partition names for replication targets.
- Encrypted passwords generated by `altiEncrypt` can be used in AKU configuration files in the Altibase 8.1 verified source.
- The selected Altibase 8.1 verified source keeps Kubernetes object examples generic and does not add a managed-cloud provider-specific deployment contract.

## Kubernetes Building Blocks

Building block: `Pod`

- Purpose: smallest Kubernetes execution unit that contains the Altibase container.
- Typical use: simple test or demonstration.
- Key settings: container image, `containerPort: 20300`, and Altibase start mode such as `MODE=daemon`.
- Limitation: a Pod IP is dynamic and Pod-local storage is ephemeral unless persistent volume storage is mounted.

Building block: `Deployment`

- Purpose: create and maintain one or more Pods from a template.
- Typical use: simple Altibase container test or manual replication demonstration.
- Key settings: label selector, Pod template labels, image, exposed ports, and environment variables.
- Limitation: a Deployment does not provide stable ordinal identity like `altibase-sts-0`; use `StatefulSet` for AKU.

Building block: `Service`

- Purpose: provide a stable virtual IP or DNS name for Pods whose Pod IPs can change.
- Typical use: client connection to Altibase port `20300` and replication connection to port `20301`.
- Key settings: `ports`, `targetPort`, and `selector`.
- For StatefulSet and AKU: use a headless Service with `clusterIP: None` and `publishNotReadyAddresses: true`.

Building block: `PV` and `PVC`

- Purpose: preserve Altibase database files and log files beyond container or Pod lifetime.
- Typical use: mount persistent storage to the Altibase home, `dbs`, `logs`, or environment-specific data directories.
- Key settings: storage capacity, access mode, reclaim policy, storage class or explicit backend such as NFS.
- Caution: the sample guide uses NFS, but the production storage backend must be chosen for durability, latency, fencing, backup, and recovery requirements.

Building block: `StatefulSet`

- Purpose: manage stateful Pods with stable ordinal identities and ordered lifecycle behavior.
- Typical use: AKU-managed Altibase Pod lifecycle.
- Key settings: `serviceName`, `replicas`, `podManagementPolicy: OrderedReady`, `startupProbe`, `terminationGracePeriodSeconds`, volume mounts, and `volumeClaimTemplates`.
- Stable host names: Pods are named like `altibase-sts-0`, `altibase-sts-1`; service DNS can be used as `<pod-name>.<service-name>`.

Building block: container image and startup mode

- Simple source examples use the Docker Hub image `altibase/altibase` and set environment variable `MODE=daemon` for an Altibase server test.
- Manual replication source examples expose ports `20300` and `20301`, set `MODE=replication`, and set `SLAVE_REP_PORT=20301`.
- AKU sample examples use a general Linux image, install Altibase into a persistent mount, and run an entry script that sources `set_linux.env` and `set_altibase.env`.
- `ALTIBASE_HOME` can be derived from `${HOSTNAME}`, for example `/ALTIBASE/altibase_home_${MY_POD_NAME}`, so each StatefulSet Pod gets a stable per-host Altibase home.
- For Kubernetes, the AKU sample guide says a hostname-based Altibase license is required; sample hostnames are `altibase-sts-0`, `altibase-sts-1`, `altibase-sts-2`, and `altibase-sts-3`.

## Minimal Kubernetes Patterns

Pattern block: direct Altibase `Pod`

```yaml
apiVersion: v1
kind: Pod
metadata:
  labels:
    app: altibase
  name: altibase-pod
spec:
  containers:
  - image: altibase/altibase
    name: altibase
    ports:
    - containerPort: 20300
      protocol: TCP
    env:
    - name: MODE
      value: daemon
```

Use this only for a simple test. A directly created Pod has no Deployment controller, no stable StatefulSet identity, and no AKU lifecycle management.

Pattern block: simple Altibase `Deployment`

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: altibase-deploy
spec:
  replicas: 1
  selector:
    matchLabels:
      app: altibase
  template:
    metadata:
      labels:
        app: altibase
    spec:
      containers:
      - name: altibase
        image: altibase/altibase
        ports:
        - containerPort: 20300
          protocol: TCP
        env:
        - name: MODE
          value: daemon
```

Verification:

```bash
kubectl create -f altibase-deploy.yaml
kubectl get pod -o wide
kubectl exec -it <pod-name> -- /bin/bash
. set_altibase.env
is
```

Pattern block: NFS-backed volume mounts for simple Deployment

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: altibase-deploy-vol-node1
spec:
  replicas: 1
  template:
    spec:
      containers:
      - name: altibase
        image: altibase/altibase
        volumeMounts:
        - name: altibase-nfs-dbs
          mountPath: /home/altibase/altibase_home/dbs
        - name: altibase-nfs-logs
          mountPath: /home/altibase/altibase_home/logs
        ports:
        - containerPort: 20300
          protocol: TCP
        env:
        - name: MODE
          value: daemon
      volumes:
      - name: altibase-nfs-dbs
        nfs:
          server: <nfs-server>
          path: /path/to/node1/dbs
      - name: altibase-nfs-logs
        nfs:
          server: <nfs-server>
          path: /path/to/node1/logs
```

- Purpose: preserve database files and online logs outside the Pod lifecycle.
- Source shape: the Kubernetes User's Guide uses separate NFS paths for `dbs` and `logs`.
- Caution: configure and validate the NFS server, durability, latency, permissions, and backup behavior before treating this as production storage.

Pattern block: fixed Service for a simple Altibase Pod

```yaml
apiVersion: v1
kind: Service
metadata:
  name: altibase-service
spec:
  ports:
  - port: 20300
    targetPort: 20300
  selector:
    app: altibase-deploy-pod1
```

- Use a `Service` because Pod IPs are dynamic and can change when a Deployment recreates a Pod.
- Verify from another Pod with `is -s <service-ip-or-dns> -port 20300 -u <user> -p <password>`.

Pattern block: headless Service for AKU StatefulSet

```yaml
apiVersion: v1
kind: Service
metadata:
  name: altibase-svc
spec:
  type: ClusterIP
  clusterIP: None
  publishNotReadyAddresses: true
  ports:
  - name: service-port
    port: 20300
    targetPort: 20300
  - name: replication-port
    port: 20301
    targetPort: 20301
  selector:
    app: altibase-sts
```

Pattern block: StatefulSet controls that matter for AKU

```yaml
apiVersion: apps/v1
kind: StatefulSet
metadata:
  name: altibase-sts
spec:
  serviceName: altibase-svc
  replicas: 4
  podManagementPolicy: OrderedReady
  template:
    spec:
      terminationGracePeriodSeconds: 60
      containers:
      - name: altibase-sts
        startupProbe:
          exec:
            command:
            - cat
            - /tmp/aku_start_completed
          failureThreshold: 3600
          periodSeconds: 10
        ports:
        - containerPort: 20300
          protocol: TCP
        - containerPort: 20301
          protocol: TCP
```

Why these controls matter:

- `OrderedReady` prevents several Pods from starting AKU at the same time.
- `startupProbe` waits until `aku -p start` creates `/tmp/aku_start_completed`.
- `publishNotReadyAddresses: true` allows Pod DNS records to be published before all Pods are ready.
- `terminationGracePeriodSeconds` must be long enough for `aku -p end` to flush and reset replication before the Pod exits.

## AKU Sample Object Set

Object block: `PersistentVolume`

- Purpose: provide persistent storage for AKU-managed Pods.
- Source sample: four `PersistentVolume` objects, `100Gi` each, `ReadWriteMany`, `persistentVolumeReclaimPolicy: Retain`, backed by NFS.
- Important source note: the sample uses four different NFS paths, but says the same path can also be used because each Pod creates a unique subdirectory using its hostname.
- Production caution: choose the storage backend for durability, latency, fencing, backup, and failure semantics; the selected sources do not validate a specific cloud storage class.

Object block: `ConfigMap`

- Purpose: hold `set_linux.env`, `set_altibase.env`, and `entry_point.sh` in the AKU sample.
- `set_linux.env`: sample Linux tuning commands for limits and kernel parameters; adapt it to the actual Linux image and host policy.
- `set_altibase.env`: sets `MY_POD_NAME=${HOSTNAME}`, `ALTIBASE_HOME=/ALTIBASE/altibase_home_${MY_POD_NAME}`, `ALTIBASE_NLS_USE=UTF8`, `ALTIBASE_PORT_NO=20300`, `ALTIBASE_REPLICATION_PORT_NO=20301`, `ALTIBASE_ADMIN_MODE=1`, `ALTIBASE_REMOTE_SYSDBA_ENABLE=1`, `PATH`, and `LD_LIBRARY_PATH`.
- `entry_point.sh`: sources the environment files, traps `SIGTERM` and `TERM`, runs `aku -p end` before `server stop`, starts Altibase and `aku -p start` when the Pod's `ALTIBASE_HOME` already exists, and otherwise creates the home directory and waits for manual Altibase installation and AKU setup.
- Secret caution: the sample keeps environment scripts in a ConfigMap, but passwords and license material should use `Secret` objects or an equivalent protected secret mechanism.

Object block: AKU `StatefulSet`

- Source sample uses `serviceName: altibase-svc`, `replicas: 4`, `updateStrategy: RollingUpdate`, `podManagementPolicy: OrderedReady`, `terminationGracePeriodSeconds: 60`, an executable `/CONFIGMAP/entry_point.sh`, ports `20300` and `20301`, `startupProbe` on `/tmp/aku_start_completed`, a persistent mount at `/ALTIBASE`, and a read-only ConfigMap mount at `/CONFIGMAP`.
- `volumeClaimTemplates` request persistent storage for each Pod; match `accessModes` and storage size to the chosen storage class.
- The first Pod can remain `0/1 READY` until Altibase is installed, the database is created, `aku.conf` is configured, and `aku -p start` creates `/tmp/aku_start_completed`.

## AKU Overview

Purpose: `aku` is the Altibase Kubernetes Utility. It helps synchronize Altibase data when Pods start, stop, scale up, or scale down in a Kubernetes `StatefulSet`.

Important boundary: AKU supports data replication among Pods. It does not provide Altibase data scale-out.

Required pieces:

- A Kubernetes `StatefulSet`; do not use AKU as the lifecycle controller for a plain `Deployment`.
- `podManagementPolicy: OrderedReady`.
- A headless Service with `publishNotReadyAddresses: true`.
- Persistent storage for each Pod.
- Altibase server and `aku` running in the same container.
- Same `aku` version and same `aku.conf` values on all Pods.
- `$ALTIBASE_HOME` set and `$ALTIBASE_HOME/bin` in `PATH`.
- Altibase property `ADMIN_MODE` set to `1` before AKU startup work.
- Altibase property `REMOTE_SYSDBA_ENABLE` set to `1`.
- `aku -p start` executed after Altibase server startup succeeds.
- `aku -p end` executed before the Altibase server stops.

Typical container entry flow:

```bash
. /CONFIGMAP/set_linux.env
. /CONFIGMAP/set_altibase.env

trap 'aku -p end; server stop' SIGTERM TERM

server start
aku -p start

while true; do
  sleep 1
done
```

Use environment-specific paths and secret handling; the snippet only shows the lifecycle order.

## AKU Command Syntax

Compact syntax:

```text
aku
  [-h | --help]
  [-v | --version]
  [-i | --info]
  [-p start | -p end | -p clean]
  [--pod start | --pod end | --pod clean]
```

Command block: `aku -i`

- Purpose: display information read from `aku.conf`.
- Outputs: server ID, host, user, password, port, replication port, maximum server count, replication object names, and replication target items.
- Use before changing Pod count to confirm that every Pod has the expected `aku.conf`.

Command block: `aku -p start`

- Purpose: create replication objects, synchronize data when needed, start replication, and create `/tmp/aku_start_completed`.
- Run timing: after Altibase server startup succeeds.
- Master Pod: the first StatefulSet Pod, normally `<statefulset-name>-0`.
- Slave Pod: any later Pod created by scale-up or restart.

Command block: `aku -p end`

- Purpose: flush replication, stop replication, reset replication information when configured, and delete `/tmp/aku_start_completed`.
- Run timing: before stopping the Altibase server and before Pod termination.
- Kubernetes setting: `terminationGracePeriodSeconds` must allow this command to complete.

Command block: `aku -p clean`

- Purpose: delete all AKU-created Altibase replication objects on Pods and delete `/tmp/aku_start_completed`.
- Use only when synchronization between Pods is no longer needed.
- Caution: this is a cleanup operation for AKU-managed replication; require an operator decision and recovery plan.

## Pod Lifecycle Flow

Overall StatefulSet lifecycle:

```mermaid
flowchart TD
  A[StatefulSet creates Pod by ordinal] --> B[Container starts]
  B --> C[Start Altibase server]
  C --> D[Run aku -p start]
  D --> E{AKU completed?}
  E -- No --> F[startupProbe keeps Pod unready]
  F --> D
  E -- Yes --> G[startupProbe succeeds]
  G --> H[Serve workload until termination]
  H --> I[Run aku -p end]
  I --> J[Stop Altibase server and exit]
```

Lifecycle details:

1. Container startup sets the Altibase environment before starting the Altibase server.
2. `aku -p start` creates `/tmp/aku_start_completed` when AKU startup completes; until then, the startup probe keeps the Pod unready.
3. After the startup probe succeeds, the next ordered Pod may start and service traffic plus replication continue.
4. On termination, `aku -p end` flushes, stops, and resets configured replication, then deletes `/tmp/aku_start_completed`.
5. Stop the Altibase server after AKU termination handling finishes.

`aku -p start` on the master Pod:

```mermaid
flowchart TD
  A[Run aku -p start on pod 0] --> B[Read aku.conf]
  B --> C{Does /tmp/aku_start_completed exist?}
  C -- Yes --> D[Stop as duplicate start]
  C -- No --> E[Connect to target Pods]
  E --> F[Create AKU replication objects]
  F --> G{Any target Pod connected?}
  G -- Yes --> H[Start related replication on connected Pods]
  G -- No --> I[No remote replication starts yet]
  H --> J[Create /tmp/aku_start_completed]
  I --> J
  J --> K[AKU exits successfully]
```

`aku -p start` on a new or reset slave Pod:

```mermaid
flowchart TD
  A[Run aku -p start on slave Pod] --> B[Read aku.conf]
  B --> C{Does /tmp/aku_start_completed exist?}
  C -- Yes --> D[Stop as duplicate start]
  C -- No --> E[Connect to target Pods]
  E --> F[Create or reuse AKU replication objects]
  F --> G[TRUNCATE local replication target tables]
  G --> H[Request synchronization from master Pod]
  H --> I[Run replication SYNC from master to slave]
  I --> J[Start related replication on both sides]
  J --> K[Set ADMIN_MODE to 0 on slave]
  K --> L[Create /tmp/aku_start_completed]
  L --> M[AKU exits successfully]
```

`aku -p start` on a slave Pod whose replication information was not reset:

```mermaid
flowchart TD
  A[Run aku -p start on restarted slave Pod] --> B[Read aku.conf]
  B --> C[Connect to target Pods]
  C --> D[Start related replication]
  D --> E{AKU_FLUSH_AT_START}
  E -- 1 --> F[FLUSH local unsent changes]
  F --> G[Request FLUSH or FLUSH WAIT on connected Pods]
  E -- 0 --> H[Skip replication-gap flush]
  G --> I[Set ADMIN_MODE to 0]
  H --> I
  I --> J[Create /tmp/aku_start_completed]
```

`aku -p end` on Pod termination:

```mermaid
flowchart TD
  A[Run aku -p end before server stop] --> B[Read aku.conf]
  B --> C[Connect to Pods related to current Pod]
  C --> D{AKU_FLUSH_AT_END}
  D -- 1 --> E[ALTER REPLICATION replication_name FLUSH ALL]
  D -- 0 --> F[Skip flush]
  E --> G[Request ALTER REPLICATION replication_name STOP on related Pods]
  F --> G
  G --> H{AKU_REPLICATION_RESET_AT_END}
  H -- 1 --> I[Request ALTER REPLICATION replication_name RESET]
  H -- 0 --> J[Leave replication information]
  I --> K[Delete /tmp/aku_start_completed]
  J --> K
  K --> L[AKU exits then stop Altibase server]
```

## `aku.conf` Essentials

Property block: Kubernetes identity

- `AKU_STS_NAME`: StatefulSet name. Maximum length is 63 bytes.
- `AKU_SVC_NAME`: Service name. Maximum length is 63 bytes.
- `AKU_SERVER_COUNT`: maximum number of Altibase servers synchronized by AKU. For 7.1 use 1 to 4. For 7.3 and Altibase 8.1 verified source use 1 to 6.

Property block: Altibase connection

- `AKU_SYS_PASSWORD`: password for the `SYS` user. Use protected secret handling; in Altibase 8.1 verified source, encrypted passwords generated by `altiEncrypt` can be used in AKU configuration files.
- `AKU_PORT_NO`: Altibase service port, default `20300`.
- `AKU_REPLICATION_PORT_NO`: Altibase replication port, default `20301`.
- `AKU_QUERY_TIMEOUT`: timeout for SQL executed by AKU.
- `AKU_QUERY_RETRY_COUNT`: retry count for failed AKU SQL.
- `AKU_QUERY_RETRY_DELAY_MSEC`: retry delay in milliseconds.

Property block: startup and shutdown behavior

- `AKU_ADDRESS_CHECK_COUNT`: number of connection attempts used to check whether the current Pod DNS address is registered and inter-Pod communication is possible.
- `AKU_FLUSH_AT_START`: when `1`, AKU removes replication gaps during `aku -p start` by using `FLUSH`; when `0`, it does not.
- `AKU_FLUSH_TIMEOUT_AT_START`: wait time for `FLUSH WAIT`; when `0`, AKU performs `FLUSH`.
- `AKU_DELAY_START_COMPLETE_TIME`: delay after slave synchronization and before changing `ADMIN_MODE` to `0`.
- `AKU_FLUSH_AT_END`: when `1`, `aku -p end` removes replication gaps with `FLUSH ALL`; when `0`, it does not.
- `AKU_REPLICATION_RESET_AT_END`: when `1`, `aku -p end` resets replication information; when `0`, it leaves replication information.

Property block: replication targets

- `REPLICATIONS/REPLICATION_NAME_PREFIX`: prefix for replication object names created by AKU. Maximum prefix length is 37 bytes.
- `REPLICATIONS/SYNC_PARALLEL_COUNT`: number of sender or receiver threads used for replication sync. Valid range is 1 to 100 in the 7.1, 7.3, and Altibase 8.1 verified source Utilities guidance.
- Replication target format: `[user_name].[table_name]` or `[user_name].[table_name] PARTITION [partition_name]`.
- Multiple `REPLICATIONS` blocks can be defined with comma-separated configuration blocks in 7.1, 7.3, and Altibase 8.1 verified source. Keep this separate from the replica-count limit: 7.1 supports `AKU_SERVER_COUNT` 1 to 4, while 7.3 and Altibase 8.1 verified source support 1 to 6.

Example `REPLICATIONS` block:

```properties
REPLICATIONS = (
  REPLICATION_NAME_PREFIX = AKU_REP
  SYNC_PARALLEL_COUNT     = 1
  (
    SYS.T1,
    SYS.T2 PARTITION P1,
    SYS.T3
  )
)
```

Example multiple `REPLICATIONS` blocks:

```properties
REPLICATIONS = (
  REPLICATION_NAME_PREFIX = AKU_REP1
  SYNC_PARALLEL_COUNT     = 1
  (
    SYS.T1,
    SYS.T2 PARTITION P1,
    SYS.T3
  )
),
(
  REPLICATION_NAME_PREFIX = AKU_REP2
  SYNC_PARALLEL_COUNT     = 1
  (
    SYS.T4,
    SYS.T5,
    SYS.T6
  )
),
(
  REPLICATION_NAME_PREFIX = AKU_REP3
  SYNC_PARALLEL_COUNT     = 1
  (
    SYS.T7,
    SYS.T8,
    SYS.T9
  )
)
```

Replication object naming rule:

```text
<REPLICATION_NAME_PREFIX>_<smaller Pod ordinal><larger Pod ordinal>
```

Example with `AKU_SERVER_COUNT=4` and `REPLICATION_NAME_PREFIX=AKU_REP`:

- `altibase-sts-0` has `AKU_REP_01`, `AKU_REP_02`, and `AKU_REP_03`.
- `altibase-sts-1` has `AKU_REP_01`, `AKU_REP_12`, and `AKU_REP_13`.
- `altibase-sts-2` has `AKU_REP_02`, `AKU_REP_12`, and `AKU_REP_23`.
- `altibase-sts-3` has `AKU_REP_03`, `AKU_REP_13`, and `AKU_REP_23`.

Caution: do not manually create, drop, or modify replication objects created by AKU except during an explicit recovery procedure.

## Manual Replication With Kubernetes Service Names

Use Service DNS names instead of Pod IP addresses because Pod IPs are dynamic.

Deployment pattern:

- Create one Deployment per Altibase replication node.
- Mount persistent storage for `dbs` and `logs` on each node.
- Expose container ports `20300` and `20301`.
- Set `MODE=replication` and `SLAVE_REP_PORT=20301` in the Altibase container environment.
- Create one Service per node, selecting the matching Pod label and exposing both `service-port` `20300` and `replication-port` `20301`.
- In `CREATE REPLICATION`, use the other node's Service DNS name instead of a Pod IP address.

Example on node 1:

```sql
CREATE TABLE t1 (c1 INTEGER PRIMARY KEY, c2 INTEGER);

CREATE REPLICATION rep1
WITH 'altibase-svc-node2', 20301
FROM sys.t1 TO sys.t1;

ALTER REPLICATION rep1 START;
```

Example on node 2:

```sql
CREATE TABLE t1 (c1 INTEGER PRIMARY KEY, c2 INTEGER);

CREATE REPLICATION rep1
WITH 'altibase-svc-node1', 20301
FROM sys.t1 TO sys.t1;

ALTER REPLICATION rep1 START;
```

Verification:

```sql
INSERT INTO t1 VALUES (1, 1);
SELECT * FROM t1;
```

For AKU-managed StatefulSets, configure replication targets in `aku.conf` and let AKU create and operate the replication objects.

## AKU StatefulSet Procedure

1. Prepare persistent storage for each Pod. The sample guide uses multiple NFS-backed `PersistentVolume` objects, but any storage type that meets persistence and performance requirements can be used.
2. Obtain hostname-based Altibase licensing for the StatefulSet Pod names, for example `altibase-sts-0` through `altibase-sts-3` in the 4-Pod sample.
3. Prepare a ConfigMap or image content for environment setup and an entry script. The entry script must run `aku -p end` on `SIGTERM` before `server stop`.
4. Set the Altibase environment. At minimum, configure `ALTIBASE_HOME`, `ALTIBASE_NLS_USE`, `ALTIBASE_PORT_NO`, `ALTIBASE_REPLICATION_PORT_NO`, `ALTIBASE_ADMIN_MODE=1`, `ALTIBASE_REMOTE_SYSDBA_ENABLE=1`, `PATH`, and `LD_LIBRARY_PATH` as appropriate for the image.
5. Create a headless Service with `clusterIP: None`, `publishNotReadyAddresses: true`, and ports `20300` and `20301`.
6. Create a StatefulSet with `podManagementPolicy: OrderedReady`, persistent volume claim templates, a `startupProbe` that checks `/tmp/aku_start_completed`, and sufficient `terminationGracePeriodSeconds`.
7. Install Altibase and create the database on the first Pod if the persistent Altibase home is not already initialized.
8. Create application tables that will be listed in the AKU replication targets.
9. Copy `aku.conf.sample` to `aku.conf` and configure StatefulSet name, Service name, replica count, ports, password handling, startup/shutdown behavior, and `REPLICATIONS`.
10. Start Altibase server, then run `aku -p start` on each Pod as it becomes eligible under ordered startup.
11. Confirm that every Pod reaches `READY` and that `aku -i` reports the expected server and replication information.

First-Pod bootstrap shape from the sample guide:

```bash
kubectl exec -it altibase-sts-0 -- bash
. /CONFIGMAP/set_altibase.env
server create utf8 utf8
server start
is -sysdba
```

Inside `iSQL`, create the target tables that will be listed in `REPLICATIONS`, then exit. Copy and edit `aku.conf`, then start AKU:

```bash
cd $ALTIBASE_HOME/conf
cp aku.conf.sample aku.conf
aku -p start
```

Expected result: `aku -p start` reports master Pod startup and creates `/tmp/aku_start_completed`, allowing the StatefulSet startup probe to make `altibase-sts-0` ready and continue ordered Pod creation. Repeat the Altibase installation, database creation, table creation, `aku.conf`, and `aku -p start` setup for later Pods unless the image and persistent home already contain that work.

## Verification Cookbook

Check Kubernetes objects:

```bash
kubectl get sts -o wide
kubectl get pod -o wide
kubectl get svc -o wide
kubectl get pv,pvc -o wide
```

Check the AKU startup gate:

```bash
kubectl exec -it <pod-name> -- test -f /tmp/aku_start_completed
kubectl exec -it <pod-name> -- aku -i
```

Check Altibase access inside a Pod:

```bash
kubectl exec -it <pod-name> -- bash
. /CONFIGMAP/set_altibase.env
is
```

Check AKU-created replication state:

```sql
SELECT REPLICATION_NAME, XSN
FROM SYSTEM_.SYS_REPLICATIONS_;
```

Interpretation:

- `XSN = -1` means replication information is reset or initialized for that replication object.
- A non-`-1` `XSN` means replication information remains. This can be normal while replication is active, but after an intended scale-down reset it can indicate incomplete termination handling.

Check replicated data after scale-up:

```sql
INSERT INTO t1 VALUES (2, 2);
SELECT * FROM t1;
```

Scale operations:

```bash
kubectl scale sts altibase-sts --replicas=3
kubectl scale sts altibase-sts --replicas=4
```

After scale-down, inspect remaining Pods for replication objects related to the removed Pod and confirm that reset state matches the planned `AKU_REPLICATION_RESET_AT_END` behavior.

## Troubleshooting And Cautions

Issue block: Pod remains unready during first StatefulSet creation

- Likely cause: `startupProbe` is waiting for `/tmp/aku_start_completed`.
- Check: connect to the first Pod, source the Altibase environment, create or start the Altibase server, configure `aku.conf`, and run `aku -p start`.
- Expected result: AKU creates `/tmp/aku_start_completed`, the Pod becomes ready, and the next ordered Pod can start.

Issue block: First Pod is running but waiting for manual Altibase setup

- Likely cause: the AKU sample `entry_point.sh` found that `${ALTIBASE_HOME}` did not exist, created the directory, and printed the required manual steps instead of starting Altibase.
- Check: run `. /CONFIGMAP/set_altibase.env`, verify `ALTIBASE_HOME`, install Altibase if needed, create the database, create target tables, configure `aku.conf`, and run `aku -p start`.
- Expected result: the persistent Altibase home exists, `server start` succeeds, `aku -p start` creates `/tmp/aku_start_completed`, and the startup probe marks the Pod ready.

Issue block: `aku -p start` reports duplicate execution

- Likely cause: `/tmp/aku_start_completed` already exists.
- Check: verify whether AKU was already completed for this Pod and whether the Pod restart path is valid.
- Do not delete the file just to force progress unless the replication state and recovery plan are clear.

Issue block: Scale-up Pod does not receive expected data

- Check Service DNS names and ports `20300` and `20301`.
- Check that `AKU_STS_NAME`, `AKU_SVC_NAME`, `AKU_SERVER_COUNT`, and `REPLICATIONS` are identical where required.
- Check whether the slave Pod was treated as a reset/new slave or as a restart with existing replication information.
- If replication information was not reset, `TRUNCATE` and SYNC from the master are skipped; `AKU_FLUSH_AT_START` controls replication-gap flushing.

Issue block: Scale-down leaves online logs accumulating

- Likely cause: a Pod was force-terminated before `aku -p end` completed, or `AKU_REPLICATION_RESET_AT_END=0` left replication information.
- Risk: other Pods may retain online logs needed for replication to the terminated Pod, eventually exhausting disk space.
- Corrective SQL for the affected replication object:

```sql
ALTER REPLICATION replication_name STOP;
ALTER REPLICATION replication_name RESET;
```

Issue block: Master Pod failure during `aku -p start`

- Risk condition: one or more slave Pods are running, and the master Pod has lost some or all replication object information for running slave Pods.
- Recovery outline:
  1. Select one slave Pod as the recovery basis.
  2. Run `aku -p end` to terminate all other slave Pods.
  3. Synchronize data from the selected slave Pod to the master Pod.
  4. Start replication on the master Pod.
  5. Retry `aku -p start`.
- This is a high-risk recovery path. Require a backup, support plan, and explicit operator approval before issuing production commands.

Issue block: Master Pod storage corruption

- AKU does not recover data corruption caused by storage corruption in the master Pod.
- Use storage-level recovery, Altibase backup/recovery procedures, or a validated replica-based recovery plan.

Issue block: cloud or container platform uncertainty

- The selected sources show generic Kubernetes objects, Docker Hub image examples, NFS examples, and an AKU sample with `ubuntu:18.04`; they do not validate a specific managed Kubernetes service, storage class, ingress/load balancer, or secret backend.
- Ask for the Kubernetes provider, version, node OS, image build, storage class, network policy, Service exposure model, backup plan, and hostname-license basis.
- Keep the Altibase requirements fixed: ports `20300` and `20301`, persistent database/log storage, stable Service DNS for replication, protected secrets, `OrderedReady` for AKU, and `aku -p end` before server shutdown.

## Customer Answer Templates

Template: explain AKU

```text
AKU is the Altibase Kubernetes Utility. It is used with Kubernetes StatefulSets to synchronize Altibase data when Pods start and to flush, stop, and optionally reset replication when Pods terminate. It supports replication among Pods, but it is not an Altibase data scale-out feature.
```

Template: production readiness checklist

```text
Before deploying Altibase with AKU, confirm the Altibase version, Kubernetes provider and version, container image, storage backend, StatefulSet replica count, hostname-based license, Service DNS design, ports 20300 and 20301, replication target tables, backup and recovery plan, and secret handling for SYS credentials.
```

Template: lifecycle order

```text
The container should start Altibase first, then run aku -p start. Kubernetes startupProbe should wait for /tmp/aku_start_completed. On termination, the container should run aku -p end before server stop, and terminationGracePeriodSeconds must be long enough for AKU to finish.
```

Template: first AKU Pod bootstrap

```text
If the first StatefulSet Pod is Running but not Ready, check whether /tmp/aku_start_completed is missing because Altibase has not yet been installed or initialized in the persistent home. Source the Altibase environment, create or start the server, create the replication target tables, configure aku.conf, then run aku -p start so the startupProbe can succeed.
```

## Attachment Cross-References

- Use `02_administration_operations.md` for startup, shutdown, backup, recovery, archive log, and tablespace operations around Kubernetes incidents.
- Use `06_data_dictionary_performance_views.md` for SQL checks that verify server, session, tablespace, replication, and runtime state from a Pod.
- Use `09_replication_ha_cdc.md` for replication object design, state interpretation, failover, gap handling, and CDC context behind AKU.
- Use `18_security_ssl_tls.md` for secrets, listener exposure, certificate, TLS, audit, and security policy decisions in Kubernetes deployments.

## Residual Scope

- Kubernetes examples are limited to Altibase and AKU behavior from the selected source set. Production platform design still needs environment-specific review for storage, fencing, backup, secrets, licensing, observability, and Kubernetes version support.
- The selected sources do not provide provider-specific EKS, GKE, AKS, cloud load balancer, managed storage, or secret-manager procedures. Use this attachment for Altibase/AKU requirements and request the platform-specific design details before giving production commands.
