# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

Password spraying techniques evolved significantly in 2024. For example, the China-nexus ORB07 network targeted Entra ID accounts, leveraging a bug in the Resource Owner Password Credentials authentication flow to validate credentials without logging a successful sign-in event. The threat actor then performed automated exfiltration of all SharePoint documents (Figure 14).

| Error: Invalid | Error: Valid | Successful Login | Automated Exfiltration |
|----------------|-------------|------------------|------------------------|
|                |             |                  |                        |

| Initial Access: 6 minutes, 4 seconds | Actions on Objective: 13 minutes, 42 seconds |
|--------------------------------------|----------------------------------------------|

*Figure 14. ORB07 breakout time*

SCATTERED SPIDER's diminished operational tempo in 2024 likely accounts for the reduced number of phishing-related cloud intrusions throughout the year. However, some threat actors are using AITM-based phishing, which proxies the phished user’s authentication requests to the cloud authentication service being targeted. This allows the threat actor to prompt the user for an MFA token as well, circumventing one of the primary cloud account security controls.

## Defense Evasion Trends

Similar to other security domains, cloud-conscious threat actors are consistently attempting to evade defender detections and security controls. [Indicator removal](#) continues to be the most common defense evasion tactic. This tactic is primarily driven by SCATTERED SPIDER and other adversaries hampering email-based detection of malicious activity, a method used in approximately 75% of cases in which indicators were removed in the first half of 2024 and in 78% of these cases in the second half of 2023.

Threat actors are also consistently attempting to evade policy-based security controls implemented by defenders. This is primarily done by implementing alternate MFA methods on compromised identities and bypassing cloud firewall segmentation.

In addition to these ongoing tactics, 2024 saw the emergence and continued development of more stealthily initial access and credential collection techniques, which enable further defense evasion in cloud intrusions.