# **CROWDSTRIKE 2025 GLOBAL THREAT REPORT**

---

## Steps and Techniques Used by CURY SPIDER, CHATTY SPIDER, and PLUMP SPIDER

| Step    | CURY SPIDER                                                                   | CHATTY SPIDER                                                        | PLUMP SPIDER                                                                                             |
|---------|-------------------------------------------------------------------------------|----------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| **STEP 1** | CURY SPIDER spam bombs the victim                                             | CHATTY SPIDER sends phishing email to the victim                      | PLUMP SPIDER calls the victim posing as IT support (vishing)                                             |
| **STEP 2** | CURY SPIDER calls the victim posing as IT support (vishing)                   | Victim calls in response to CHATTY SPIDER's email                     |                                                                                                          |
|           |                                                                               |                                                                      |                                                                                                          |
|           | **Victim downloads RMM tool, providing these adversaries with access**        |                                                                      |                                                                                                          |
|           | Quick Access, TeamViewer                                                      | Zoho Assist, Atera, SuperOps, Syncro                                  | SoftEther VPN, Ammyy Admin, DWAgent, HopToDesk, RustDesk, Supremo, TeamViewer                            |
| **STEP 3** |                                                                               |                                                                      | PLUMP SPIDER obtains valid credentials from the victim                                                    |
| **STEP 4** | CURY SPIDER deploys tools for persistence, including a custom backdoor        | CHATTY SPIDER downloads WinSCP and/or Rclone to the victim system     | PLUMP SPIDER introduces reconnaissance tooling                                                            |
| **STEP 5** | CURY SPIDER performs reconnaissance, including for security software          | CHATTY SPIDER exfiltrates sensitive data to C2 infrastructure         | PLUMP SPIDER performs a fraudulent transaction from victim payment system                                 |
| **STEP 6** | CURY SPIDER exfiltrates data to C2 infrastructure                             | CHATTY SPIDER emails the victim with extortion demand                 |                                                                                                          |
| **STEP 7** | CURY SPIDER provides access to the victim to other actors, including BGH adversary WANDERING SPIDER |                                                                      |                                                                                                          |

---

**Figure 7.** CURY SPIDER, CHATTY SPIDER, and PLUMP SPIDER use vishing for initial access