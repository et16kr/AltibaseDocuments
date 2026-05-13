# 17. Kubernetes and AKU

## Applicable Versions

- 7.1: Based on base product manuals; dedicated Kubernetes guidance requires separate confirmation.
- 7.3: Based on AKU support and Kubernetes guidance.
- 8.1: Based on Altibase 8.1 verified source and Kubernetes/AKU guidance.

## Questions This File Can Answer

- What should be considered when deploying Altibase on Kubernetes?
- What role does AKU perform?
- What is the data synchronization procedure during Pod startup and shutdown?
- How should replication and storage be considered in container environments?

## Source Documents

- 7.1: Base operations and replication manuals.
- 7.3: Kubernetes User's Guide for Altibase; Altibase AKU Sample Guide for Kubernetes; Altibase 7.3 Release Notes.
- 8.1: Altibase 8.1 verified source Kubernetes User's Guide for Altibase; Altibase AKU Sample Guide for Kubernetes.

## Core Guidance

- Kubernetes answers should explain StatefulSet, PV/PVC, Pod lifecycle, AKU start/end, and replication initialization or synchronization together.
- Cross-reference AKU-related commands with the operations utilities document.

## Version Differences

- 7.1: Treat Kubernetes guidance as requiring separate confirmation beyond the base 7.1 product manuals.
- 7.3: Use 7.3 AKU and Kubernetes guidance where supported.
- 8.1: Use Altibase 8.1 verified source for Kubernetes and AKU guidance.

## Conversion TODO

- Separate YAML and command examples by purpose.
- Convert Pod startup and shutdown flows to Mermaid flowcharts.
