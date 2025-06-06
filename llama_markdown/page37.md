# CrowdStrike 2025 Global Threat Report

## Page 10

### Disclosing a Vulnerability

Disclosing a vulnerability, particularly one acknowledged as exploited in the wild, highlights potentially viable mechanisms for future exploitation. For example, in September 2024, CrowdStrike Intelligence observed multiple POST requests consistent with exploiting a direct request vulnerability in Apache OFBiz (CVE-2024-45195). These POST requests mirrored CVE-2024-45195 exploitation guidance that a well-known industry source had published two weeks earlier. CVE-2024-45195 results from the option to desynchronize the requestURI and overrideViewUri variables in the RequestHandler component of the OFBiz Java application logic.

### CVE-2024-45195

CVE-2024-45195 is similar to earlier vulnerabilities (CVE-2024-32113, CVE-2024-36104, and CVE-2024-38856) that also exploited desynchronization capabilities to allow unauthorized users to bypass authentication mechanisms. Though the vendor has provided multiple patches and several industry sources have publicly discussed these vulnerabilities, the core flaw persists and allows attackers to manipulate the controller-view state.

### Fancy Bear

Separately, in January 2024, CrowdStrike Intelligence assessed threat actors had almost certainly leveraged CVE-2023-29324 in recent spear-phishing operations. CVE-2023-29324 bypasses Microsoft's mitigations for a previously disclosed Microsoft Outlook vulnerability (CVE-2023-23397), which Fancy Bear has very likely exploited since at least March 2022 to target organizations in multiple regions and sectors. The same researcher who discovered the initial bypass (CVE-2023-29324) later found another bypass (CVE-2023-35384).

### Universal Naming Convention

An attacker can trigger both bypasses by inserting a Universal Naming Convention (UNC) path into either a Server Message Block (SMB) or WebDAV share on an attacker-controlled server into the MAPI property named PidLidReminderFileParameter (Figure 18).

| **Vulnerability** | **Description** |
| --- | --- |
| CVE-2024-45195 | Direct request vulnerability in Apache OFBiz |
| CVE-2024-32113 | Desynchronization vulnerability in OFBiz |
| CVE-2024-36104 | Desynchronization vulnerability in OFBiz |
| CVE-2024-38856 | Desynchronization vulnerability in OFBiz |
| CVE-2023-29324 | Bypass for Microsoft Outlook vulnerability |
| CVE-2023-23397 | Microsoft Outlook vulnerability |
| CVE-2023-35384 | Bypass for Microsoft Outlook vulnerability |

### Figure 18

Figure 18 shows an example of how an attacker can trigger both bypasses by inserting a UNC path into either an SMB or WebDAV share on an attacker-controlled server into the MAPI property named PidLidReminderFileParameter.