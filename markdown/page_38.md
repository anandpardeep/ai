Whether threat actors have used either bypass in 2024 is unknown. However, these vulnerabilities underscore that circumventing mitigations from earlier patches to target the same vulnerable components is often trivial.

These trends highlight threat actors’ evolving tactics and the challenges involved in effectively addressing vulnerabilities. Much of the exploitation activity discussed in this report occurred after the vulnerabilities were publicly disclosed and patches became available.

> ### REDUCING THE RISK OF VULNERABILITY EXPLOITATION
> 
> Diligently applying vendor patches and other applicable mitigations/workarounds against known vulnerabilities will reduce the risk of exploitation. [CrowdStrike Falcon® Exposure Management](https://www.crowdstrike.com/platform/endpoint-security/) can help customers gain complete attack surface visibility and prioritize vulnerability management to reduce intrusion risk and patching fatigue.
> 
> To prevent zero-day vulnerability exploitation, security teams can implement a defense-in-depth approach to detect and remediate malicious activity before an attacker can reach their objectives. For example, applying network-level access controls to limit server exposure to trusted remote hosts can help reduce potential threats, and periodically ensuring applicable logs are correctly collected and stored for later analysis can help facilitate incident response.
>
> Other best practices — such as server/application isolation and sandboxing, network segmentation, and adherence to least-privilege principles — can help prevent or limit the impact of malicious activity as well as protect against zero-day and n-day exploitation. Using extended detection and response (XDR) technology, such as [CrowdStrike Falcon® Insight XDR](https://www.crowdstrike.com/platform/endpoint-security/), as an additional layer of detection and protection on servers hosting public-facing applications can also reduce response times.\[4\]

---

## Network Perimeter Device Targeting

In 2024, threat actors continued to target devices on the network periphery, frequently leveraging industry vulnerability research — including disclosures, technical blogs, and POC exploits — to support their malicious activities. This focus on perimeter devices, both opportunistic and targeted, highlighted their appeal to adversaries and underscored the urgent need for enhanced defender visibility and protection.

The breadth and scope of compromised Palo Alto Networks perimeter devices exemplify threat actors’ persistence, objectives, and imagination in perimeter device exploitation.

Since November 14, 2024, or earlier, at least one unidentified threat actor has chained an authentication bypass vulnerability (CVE-2024-0012) with a privilege escalation vulnerability (CVE-2024-9474) in the Management Web Interface of Palo Alto Networks’ PAN-OS software. The vulnerabilities’ public disclosure and subsequent industry reporting almost certainly prompted additional threat actors to adopt the CVE-2024-0012 and CVE-2024-9474 exploit chain.

---

\[4\]: https://www.crowdstrike.com/platform/endpoint-security/