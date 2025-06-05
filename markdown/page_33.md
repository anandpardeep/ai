# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

## Cloud Control Plane: Common Cloud Intrusion Attack Paths and Tactics

| **Stage**             | **Tactics / Techniques**                                                                                       | **Sub-Techniques & Outcomes**                              |
|-----------------------|----------------------------------------------------------------------------------------------------------------|------------------------------------------------------------|
| **INITIAL ACCESS**    | Phishing<br>Employ public-facing service                                                                      | Phish for credentials<br>Actor accesses a valid account    |
|                       | Valid account                                                                                                 |                                                            |
|                       |                                                                                                                |                                                            |
| **EXECUTION**         | Cloud command line tools                                                                                      | Command line tools from compromised VMs with stolen credentials |
|                                                                                                                                        |                                                            |
| **CREDENTIAL ACCESS** | Credentials managers<br>Stored credentials<br>Unsecured credentials<br>Virtual machine-based credential extraction | Credentials in SaaS solutions<br>Access to new accounts    |
|                                                                                                                                        |                                                            |
| **PRIVILEGE ESCALATION** | Add identity to admin groups and roles                                                                         | Privilege escalation                                       |
| **PERSISTENCE**       | Add alternate authentication mechanisms<br>Add credentials to service principal or application<br>Add SSH key to VM | User identity persistence<br>Programmatic identities persistence<br>Host-based persistence (Malware deployment) |
| **DEFENSE EVASION**   | Impair email or cloud logging-based detection<br>Tamper with identity or virtual network policies               | Detection evasion<br>Security control evasion              |
| **DISCOVERY**         | Enumerate identities, groups, and roles<br>Enumerate VMs and storage solutions                                 | Identity enumeration<br>Infrastructure and storage enumeration |
| **COLLECTION**        | Download data from SaaS solutions<br>Download data through cloud control plane                                 | SaaS collection<br>Cloud infrastructure collection         |
| **IMPACT**            | Create new resources for later use                                                                             | Resource hijacking (Mining software deployment)<br>Data encryption/extortion (Ransomware deployment)   |

> Figure 15. Common cloud intrusion attack paths and tactics