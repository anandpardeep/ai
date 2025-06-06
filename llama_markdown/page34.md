# Enterprising Vulnerability Exploitation

In 2024, threat actors continued to target devices in the network periphery, where traditional EDR visibility is often limited. Exploiting unmanaged internet-exposed hosts, particularly network appliances, remained a popular initial access vector throughout 2024. Network appliances are attractive targets for many threat actors due to their unresolved security shortcomings and often deliberate exposure. Many exploits observed in 2024 demonstrate that threat actors are leveraging previously established attack vectors and components to repeatedly exploit the same products.

Attackers almost certainly prefer to target vulnerabilities that directly allow for unauthenticated remote code execution (RCE) and seek to improve their chances of success with creative and resourceful approaches. In 2024, attackers increasingly achieved RCE using two layered approaches:

*   **Chaining exploits**: Combining two or more exploits to compose an attack sequence, which increases their capabilities and impact on the target systems.
*   **Abusing legitimate features**: Exploiting often-enabled initial access, attackers sometimes rely on product features, such as integrated command shells, to enable RCE.

## Methods to Achieve Remote Code Execution

| **Method** | **Description** |
| --- | --- |
| **Exploit A** |  |
| **Exploit B** |  |
| **Exploit Chaining: Exploit A and Exploit B** |  |

## Initial Compromise

*   **Abusing Legitimate Features, Such as Integrated Command Shells**

## Exploit Chaining

In November 2024, two notable incidents exemplified the effectiveness of exploit chains. Multiple unattributed threat actors chained a bypass vulnerability (CVE-2024-0012) and privilege escalation vulnerability (CVE-2024-9474) in the Management Web Interface of Palo Alto Networks PAN-OS software. The same month, CrowdStrike Services investigated a separate campaign in which China-nexus adversary OPERATOR PANDA likely chained two Cisco IOS vulnerabilities - a privilege escalation vulnerability (CVE-2023-20198) and a command injection vulnerability (CVE-2023-20273) - to target U.S. telecom and professional services entities.