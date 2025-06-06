# SaaS Exploitation Likely to Continue

In 2025, enterprising adversaries will undoubtedly continue to seek advanced exploitation opportunities across multiple domains, specifically cloud-based SaaS applications, to access sensitive data and conduct lateral movement. With many organizations migrating data from on-premises systems to cloud-based services, adversaries are expected to continue to adapt their tradecraft accordingly. Throughout 2024, CrowdStrike Intelligence observed several eCrime and targeted intrusion adversaries leverage access to cloud-based SaaS applications to obtain data to facilitate lateral movement, extortion, and downstream targeting of third parties. SaaS exploitation will therefore be a threat to watch in 2025.

## SaaS Exploitation Techniques

| Technique | Description |
| --- | --- |
| SMS Distribution Application | Enables threat actors to distribute smishing messages to third parties. |
| Compromised SSO Identity | Allows threat actors to access sensitive data and conduct lateral movement. |
| Document Management and Storage Application | Enables threat actors to identify sensitive data for exfiltration. |
| Credential Management Application | Enables threat actors to compromise privileged accounts. |

## Figure 20: SaaS Exploitation Techniques

In most relevant cases, threat actors accessed SaaS applications after compromising an SSO identity. eCrime adversary SCATTERED SPIDER has employed this tactic since at least 2022. After gaining access to an SSO account, SCATTERED SPIDER often tests access to all available SSO-integrated applications, particularly those used for chat and video conferencing, credential management, customer relationship management, document management and storage, productivity and ticketing, and security.

In many intrusions, the adversary searched these applications for the following information:

*   Account credentials and network architecture documentation to conduct lateral movement
*   Cyber insurance and revenue information to inform extortion demands