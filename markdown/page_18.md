# Help Desk Social Engineering

In addition to vishing, multiple eCrime threat actors are increasingly adopting help desk social engineering tactics. In these campaigns, threat actors call a targeted organization’s IT help desk and impersonate a legitimate employee, attempting to persuade a help desk agent to reset passwords and/or multifactor authentication (MFA) for the relevant account.

Since early 2023, [SCATTERED SPIDER](#) has used this technique to gain access to single sign-on (SSO) accounts and cloud-based application suites. Multiple eCrime actors adopted this technique in 2024. Several relevant cases targeted academic and healthcare entities; in these incidents, threat actors subsequently used the compromised identity to exfiltrate data from cloud-based software as a service (SaaS) applications or modify employee payroll data.

IT help desks often require employees seeking password and MFA resets to provide their full name, date of birth, employee ID, and manager name or answer a previously determined security question. However, eCrime actors attempting to socially engineer help desk personnel often accurately respond to these questions. Much of this information is not necessarily privileged and can be found in public resources and social media sites. Identity data that is typically confidential, such as a Social Security number, is often advertised in underground markets.

In most help desk social engineering incidents, calls were made outside the victim’s local business hours. This is likely because it enables the threat actor to maintain longer access to the compromised account before the legitimate owner reports suspicious activity.

Threat actors using this technique often register their own device for MFA to enable persistent access to compromised accounts. They also often manually delete emails from compromised mailboxes related to suspicious account activity or configure mail transport rules to redirect relevant emails to a folder other than the main inbox.

Over the past year, several eCrime actors have openly recruited callers on popular eCrime forums. The advertisements are usually for English-speaking callers with knowledge of RMM tooling and experience conducting remote sessions. Some eCrime actors have also sought effective methods for spoofing phone numbers or encrypting calls to ensure caller IDs can be edited and appear more legitimate. This activity suggests phone-oriented social engineering will be a credible threat in 2025 as demand for these capabilities increases.

---

## How to Mitigate Help Desk Social Engineering

| Mitigation Strategy                                                                                       |
| -------------------------------------------------------------------------------------------------------- |
| Require video authentication with government identification for employees who call to request self-service password resets |
| Train help desk employees to exercise caution when taking password and MFA reset request phone calls made outside of business hours, particularly if an unusually high number of requests is made in a short time frame or if the caller purports to be calling on behalf of a colleague |
| Use additional, non-push-based authentication factors such as FIDO2 to prevent account compromise         |
| Monitor for more than one user registering the same device or phone number for MFA                        |