# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

On October 9, 2024, Palo Alto Networks disclosed five vulnerabilities (CVE-2024-9463, CVE-2024-9464, CVE-2024-9465, CVE-2024-9466, and CVE-2024-9467) affecting Expedition versions prior to 1.2.96. Expedition, which runs under the Linux OS, hosts and primarily facilitates a customer's transition from a supported vendor (Check Point, Cisco, and Juniper) to Palo Alto Networks firewalls. The vendor's disclosure statement acknowledged an attacker could exploit these vulnerabilities to read Expedition database contents and/or write arbitrary files to temporary storage locations.

On the same day, the industry source that discovered CVE-2024-9464, CVE-2024-9465, and CVE-2024-9466 released a technical blog providing exploitation guidance for all three vulnerabilities as well as CVE-2024-5910, which was previously disclosed by Palo Alto Networks in July 2024.

Within 24 hours of disclosure, CrowdStrike Intelligence captured HTTP requests consistent with CVE-2024-5910, CVE-2024-9463, and CVE-2024-9465 exploitation. Threat actors' initial post-exploitation activities — including cryptomining, malware deployment, and basic reconnaissance — were common for opportunistic exploitation activity. However, on October 18, 2024, CrowdStrike Intelligence observed CVE-2024-5910 exploitation that likely originated from two IP addresses connected to a China-nexus ORB network (Figure 19).

---

## 2024 Palo Alto CVE Exploitation Timeline

| Date    | Event Description                                             | CVE(s)                       |
|---------|--------------------------------------------------------------|------------------------------|
| Jul 10  | Public Disclosure                                            |                              |
| Oct 9   | Technical Blog, First POC                                    |                              |
| Oct 9   | Public Disclosure                                            | CVE-2024-9463, 9464, 9465, 9466, 9467 |
| Oct 9   | Public Disclosure, Technical Blog, First POC                 | CVE-2024-9464, 9465, 9466    |
| Oct 10  | First Observed Exploitation                                  | CVE-2024-5910, 9463, 9465    |
| Oct 10  | First POC                                                    | CVE-2024-9464, 9465, 9466    |
| Oct 11  | Technical Blog                                               |                              |
| Oct 11  | First Observed Exploitation                                  | CVE-2024-9466                |
| Oct 12  | First Observed Exploitation                                  | CVE-2024-9464                |
| Oct 14  | First Observed Remediation Attempts                          |                              |
| Oct 18  | First ORB(NB) Exploitation                                   | CVE-2024-5910                |

**Key:**  
- ![#FF5757](https://via.placeholder.com/15/FF5757/000000?text=+) CVE-2024-5910  
- ![#51C9E4](https://via.placeholder.com/15/51C9E4/000000?text=+) CVE-2024-9465  
- ![#FF8C57](https://via.placeholder.com/15/FF8C57/000000?text=+) CVE-2024-9463  
- ![#A5D6DC](https://via.placeholder.com/15/A5D6DC/000000?text=+) CVE-2024-9466  

*Figure 19. 2024 Palo Alto CVE exploitation timeline*

---

Each of the Palo Alto Networks vulnerabilities described in this section provides the necessary information and/or privileges to facilitate malicious activity on victim networks. In particular, threat actors almost certainly leveraged these vulnerabilities with the intent to eventually compromise Palo Alto Networks firewalls, which are attractive targets because they are often placed in front of the demilitarized zone (DMZ) or local area networks (LANs). Compromising such devices can allow attackers to achieve the following objectives:

- Easily conduct lateral movement across the victim’s network
- Monitor, divert, or detect network traffic
- Accept or drop specific network traffic