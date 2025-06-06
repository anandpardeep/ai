# CrowdStrike 2025 Global Threat Report

## Page 10

### Password Spraying Techniques

*   Password spraying techniques evolved significantly in 2024.
*   The China-nexus ORB07 network targeted Entra ID accounts, leveraging a bug in the Resource Owner Password Credentials authentication flow to validate credentials without logging a successful sign-in event.

### Automated Exfiltration

*   The threat actor then performed automated exfiltration of all SharePoint documents.

### Threat Actor Actions

| **Action** | **Time** |
| --- | --- |
| Initial Access | 6 minutes, 42 seconds |
| Actions on Objective | 13 minutes, 42 seconds |

### Figure 14: ORB07 Breakout Time

*   SCATERED SPIDER's diminished operational tempo in 2024 likely accounts for the reduced number of phishing-related cloud intrusions throughout the year.
*   However, some threat actors are using AITM-based phishing, which proxies the phished user's authentication requests to the cloud authentication service being targeted.

### Defense Evasion Trends

*   Similar to other security domains, cloud-conscious threat actors are consistently attempting to evade defender detections and security controls.
*   Indicator removal continues to be the most common defense evasion tactic.

### Threat Actor Tactics

*   This tactic is primarily driven by SCATTERED SPIDER and other adversaries hampering email-based detection of malicious activity.
*   A method used in approximately 75% of cases in which indicators were removed in the first half of 2024 and in 78% of these cases in the second half of 2023.

### Threat Actor Motivations

*   Threat actors are also consistently attempting to evade policy-based security controls implemented by defenders.
*   This is primarily done by implementing alternate MFA methods on compromised identities and bypassing cloud firewall segmentation.

### Ongoing Tactics

*   In addition to these ongoing tactics, 2024 saw the emergence and continued development of more stealthy initial access and credential collection techniques, which enable further defense evasion in cloud intrusions.