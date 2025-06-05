# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

---

These examples also highlight another theme observed throughout 2024:  
Threat actors are leveraging vulnerabilities within the network appliance’s proprietary OS. Vulnerabilities in these OSs are appealing targets because they potentially allow attackers to leverage one vulnerability to target multiple products running the same OS. These proprietary OSs are often reachable via internet-exposed management interfaces and provide an easily identifiable attack vector, making them increasingly attractive targets.

Chaining two or more vulnerabilities offers attackers additional advantages. First, it allows attackers to achieve their primary objective, unauthenticated RCE, by combining multiple exploits into one seamless attack. These vulnerabilities can often be packaged into a single request or exploit payload with minimal complexity.

Second, exploit chaining undermines the severity score-based patching process that many enterprises follow. While the pre-authentication vulnerabilities receive out-of-band patches and are typically prioritized for deployment, associated post-authentication exploits receive less attention and may be ignored, potentially allowing the exploit to be chained with a different vulnerability at a later date to again achieve RCE. Over time, this approach potentially increases the efficiency of RCE exploit chain development. Unless the vendor addresses the root cause of multiple vulnerabilities, threat actors can repurpose similar techniques and quickly develop alternatives that bypass initial mitigations.

Chaining exploits can complicate efforts to efficiently remediate vulnerabilities. Understanding the combined effects of exploit chaining often requires more analysis in addition to patching vulnerabilities ahead of traditional timelines, potentially resulting in patching fatigue. Security teams typically prioritize patching internet-facing services before other internal processes. However, depending on the specific exploit chain, certain internal-facing vulnerabilities (such as post-authentication flaws) may need to be prioritized, which may strain security teams.

---

## Abusing Legitimate Features Enables Effective Exploitation

Throughout 2024, threat actors combined vulnerability exploitation with legitimate feature abuse to achieve unauthenticated RCE. Microsoft SQL Server’s built-in `xp_cmdshell` was abused in various products to achieve RCE; these included CVE-2023-48788 and CVE-2023-27532. Abusing the legitimate `xp_cmdshell` feature, which is disabled by default because of its known security shortcomings, likely indicates threat actors are attempting to employ living-off-the-land techniques.