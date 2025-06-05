# Continuing the Discovery, Rediscovery, and Circumvention Trend

Threat actors continued to focus on previously established attack vectors and targeted similar components to achieve exploitation in 2024, continuing a trend first observed in the CrowdStrike 2023 Global Threat Report. In several 2024 incidents, threat actors leveraged their expertise in particular products to exploit those devices via one or more zero-day vulnerabilities.

For example, in September 2024, an unknown threat actor exploited and chained a zero-day file disclosure vulnerability (CVE-2024-21287) to obtain plaintext credentials. This allowed them to target a deserialization vulnerability (CVE-2024-20953) to compromise and execute code. Though CVE-2024-20953 had been disclosed prior to this incident, neither an exploit nor substantive technical details were publicly available. Despite this, an unknown threat actor successfully reproduced a functional n-day exploit for CVE-2024-20953 and chained it with a zero-day vulnerability (CVE-2024-21287). This incident indicates the threat actor had specialized product knowledge, which allowed them to identify a new vulnerability and ultimately compromise these devices and conduct follow-on malicious activity.

Another example of threat actors using previously established attack vectors involves the Windows local privilege escalation vulnerabilities in the **mks­srv** driver. During the Pwn2Own Vancouver event in March 2023, the offensive security company Synacktiv exploited a logical vulnerability in the **mks­srv** driver (CVE-2023-29360) to escalate privileges to **SYSTEM**. Since then, this previously overlooked attack surface has drawn the attention of security researchers and threat actors, resulting in at least 16 vulnerability disclosures since August 2023.

## mks­srv Vulnerabilities Discovery Timeline

| Date               | Event                                                                                          |  Exploited in the Wild  |
|--------------------|------------------------------------------------------------------------------------------------|:-----------------------:|
| March 23, 2023     | Synacktiv exploits zero-day vulnerability (CVE-2023-29360) during Pwn2Own Vancouver           |        ✔                |
| September 12, 2023 | Microsoft discloses CVE-2023-36802                                                            |                         |
| March 20, 2024     | DEVCORE exploits zero-day vulnerability (CVE-2024-35250) during Pwn2Own Vancouver             |        ✔                |
| June 11, 2024      | Microsoft discloses five related vulnerabilities                                              |                         |
| July 9, 2024       | Microsoft discloses four related vulnerabilities                                              |                         |
| August 13, 2024    | Microsoft discloses four related vulnerabilities                                              |                         |
| September 10, 2024 | Microsoft discloses CVE-2024-38245                                                            |                         |
| October 8, 2024    | Microsoft discloses CVE-2024-43554                                                            |                         |
| October 13, 2024   | Industry researcher releases POC exploit for CVE-2024-35250 based on DEVCORE’s research       |                         |
| October 15, 2024   | CrowdStrike Intelligence observes first CVE-2024-35250 sample in the wild                      |        ✔                |
| November 21, 2024  | Unknown actor attempts to execute CVE-2024-35250 exploit                                      |        ✔                |

**Key:**  
✔ = Exploited in the wild

*Figure 17. mks­srv vulnerabilities discovery timeline*