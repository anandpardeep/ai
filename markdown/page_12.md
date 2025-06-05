# CROWDSTRIKE 2025 GLOBAL THREAT REPORT

---

## Breakout Time: The Race Against Adversaries

Once adversaries gain initial access, their next objective is to “break out” and move laterally from the initial foothold to high-value assets. The speed of this “breakout time” determines how fast a defender must respond to reduce the costs and damages associated with an intrusion.

In 2024, the average breakout time for interactive eCrime intrusions fell to 48 minutes, down from 62 minutes in 2023. Alarmingly, the fastest breakout was recorded at just 51 seconds — meaning defenders may have less than a minute to detect and respond before attackers establish deeper control.

This rapid escalation in breakout time reinforces the need for:

- **Real-time threat detection** to identify and halt intrusions before they spread
- **Identity and access controls** to prevent adversaries from leveraging valid credentials
- **Proactive threat hunting** to identify pre-attack behaviors and block adversary movements early

---

## CASE STUDY

### CURLY SPIDER’s Social Engineering Attack

In 2024, [CURLY SPIDER](#) emerged as one of the fastest and most adaptive eCrime adversaries, executing high-speed, hands-on intrusions. In this case, the adversary attempted to achieve their objectives without even needing to break out to another device. The entire attack chain — from initial user interaction and social engineering to introducing a backdoor account to establish persistence — took under four minutes.

This incident would have been prevented by the CrowdStrike Falcon sensor with proper prevention policies. Regardless, within minutes, CrowdStrike OverWatch threat hunters saw the suspicious activity, notified the customer, and eliminated the threat.

---

### How CURLY SPIDER Operates

This adversary relies heavily on social engineering for initial access. In some cases, the following will occur:

- A user will receive a large volume of spam emails impersonating charities, newsletters, or financial offers
- Shortly after, a caller posing as help desk or IT support claims the spam is caused by malware or outdated spam filters
- The user is instructed to join a remote session using an RMM tool, such as Microsoft Quick Assist or TeamViewer, with the attacker guiding them through the installation if the tool is not already present; in this case, the adversary chose Quick Assist to establish control