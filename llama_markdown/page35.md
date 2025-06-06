**CROWDSTRIKE 2025 GLOBAL THREAT REPORT**

**Page 10**

**Abusing Legitimate Features Enables Effective Exploitation**

Throughout 2024, threat actors combined vulnerability exploitation with legitimate feature abuse to achieve unauthorized RCE. Microsoft SQL Server's built-in xp_cmdshell was abused in various products to achieve RCE; these included CVE-2023-48788 and CVE-2023-27532. Abusing the legitimate xp_cmdshell feature, which is disabled by default because of its known security shortcomings, likely indicates threat actors are attempting to employ living-off-the-land techniques.

**Threat Actors Abuse Legitimate Features to Achieve Unauthorized RCE**

| **Vulnerability** | **Product** | **CVE** |
| --- | --- | --- |
| SQL Server | Microsoft SQL Server | CVE-2023-48788 |
| SQL Server | Microsoft SQL Server | CVE-2023-27532 |

**Abuse of Legitimate Features Enables Effective Exploitation**

Threat actors are increasingly using legitimate features to achieve unauthorized RCE. This trend is expected to continue in 2025, as threat actors seek to exploit vulnerabilities in software and hardware to gain unauthorized access to systems and data.

**Recommendations**

* **Disable xp_cmdshell**: Disable the xp_cmdshell feature on all Microsoft SQL Server installations to prevent abuse.
* **Monitor for suspicious activity**: Monitor for suspicious activity on your systems and networks to detect potential exploitation attempts.
* **Keep software up-to-date**: Keep all software and hardware up-to-date with the latest security patches and updates to prevent exploitation of known vulnerabilities.

By following these recommendations, organizations can reduce the risk of exploitation and protect their systems and data from unauthorized access.