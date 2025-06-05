# 2024 Vishing Detections

| Month | Vishing Detections |
|-------|--------------------|
| JAN   | 2                  |
| FEB   | 5                  |
| MAR   | 3                  |
| APR   | 10                 |
| MAY   | 20                 |
| JUN   | 9                  |
| JUL   | 11                 |
| AUG   | 10                 |
| SEP   | 33                 |
| OCT   | 55                 |
| NOV   | 64                 |
| DEC   | 93                 |

**442% Increase, H1 vs. H2 2024**

*Figure 6. Vishing intrusions detected by CrowdStrike OverWatch per month, 2024*

---

In vishing campaigns, threat actors call targeted users and attempt to persuade them to download malicious payloads, establish remote support sessions, or enter their credentials to adversary-in-the-middle (AITM) phishing pages. In most 2024 vishing campaigns, threat actors impersonated IT support staff, calling targeted users under the pretext of resolving connectivity or security issues.

Throughout 2024, CrowdStrike Intelligence tracked at least six similar but likely distinct campaigns in which threat actors posing as IT staff called their targets and attempted to persuade them into establishing remote support sessions, often using Microsoft Quick Assist. In many cases, calls were made via Microsoft Teams from external tenants.

At least four of these campaigns leveraged spam bombing — sending thousands of spam emails to targeted users’ email addresses — as a pretext for the vishing call. The [CrowdStrike Falcon® Complete Next-Gen MDR](https://www.crowdstrike.com/) and CrowdStrike OverWatch teams observed a significant increase in these campaigns in the second half of 2024, detecting several relevant intrusions each day. eCrime adversary CURKY SPIDER is behind one of these campaigns, with relevant intrusions culminating in Black Basta ransomware deployment.

The long-standing Russia-based eCrime adversary [CHATTY SPIDER](https://www.crowdstrike.com/) continued to employ callback phishing as an initial access vector in data theft and extortion campaigns. In callback phishing, threat actors typically begin by sending a lure email to targeted users, often regarding an imminent charge or overdue payment. This prompts users to initiate a phone interaction. CHATTY SPIDER primarily targets the legal and insurance sectors and has demanded ransoms up to 8 million USD. Several eCrime actors used callback phishing to gain initial access in 2024, including one campaign that used it to install a remote support tool.

Brazil-based eCrime adversary [PLUMP SPIDER](https://www.crowdstrike.com/) exclusively targeted Brazil-based organizations throughout 2024 with attempts to conduct wire fraud. PLUMP SPIDER uses vishing calls to direct targeted users to sites hosting remote support and RMM tools such as RustDesk and Supremo. After gaining access, they compromise the victim’s payment systems to perform fraudulent financial transfers. In addition to targeting unwitting users, the adversary has reportedly attempted to recruit insiders at targeted organizations.