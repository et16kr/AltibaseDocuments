# 18. Security and SSL/TLS

## Applicable Versions

- 7.1: Based on Altibase 7.1 SSL/TLS guidance.
- 7.3: Based on Altibase 7.3 SSL/TLS guidance and OpenSSL 3.0.8.
- 8.1: Based on Altibase 8.1 verified source SSL/TLS guidance and replication SSL.

## Questions This File Can Answer

- How is an SSL/TLS connection configured?
- What is the certificate and server/client configuration flow?
- What OpenSSL 3.0.8 support exists in 7.3?
- How is 8.1 replication SSL configured?

## Source Documents

- 7.1: Altibase 7.1 SSL/TLS User's Guide.
- 7.3: Altibase 7.3 SSL/TLS User's Guide; Altibase 7.3 Release Notes.
- 8.1: Altibase 8.1 verified source SSL/TLS User's Guide; Altibase 8.1 Release Notes.

## Core Guidance

- SSL/TLS answers should be split into certificate preparation, server properties, client connection options, and verification procedures.
- Answer replication SSL together with the replication document.

## Version Differences

- 7.1: Use 7.1 SSL/TLS guidance for 7.1 server and client configuration.
- 7.3: Include OpenSSL 3.0.8 support and related 7.3 SSL/TLS changes.
- 8.1: Use Altibase 8.1 verified source for SSL/TLS and replication SSL guidance.

## Conversion TODO

- Convert certificate creation, placement, and configuration procedures into checklists.
- Decompose properties and connection options into item-level explanations.
