# CrowdStrike 2025 Global Threat Report

## Customer Database Compromise Campaign

Microsoft 365 has become a popular target for cloud-conscious threat actors. SharePoint and Outlook were accessed in 22% and 17%, respectively, of relevant intrusions in the first half of 2024. Scattered Spider often uses strings such as password manager, server inventory, and VPN instructions to search compromised SharePoint tenants and mailboxes for data that will aid further account compromise and lateral movement to on-premises systems.

Many organizations do not audit the data that employees upload to cloud-based storage repositories (such as SharePoint) or transmit internally via email, making these resources valuable targets for adversaries seeking to pivot within victim environments.

Threat actors can also leverage access to SaaS tooling to facilitate downstream targeting of third parties. In 2024, Scattered Spider obtained API keys to a commercial SMS distribution application from a compromised email inbox. The adversary subsequently used the application to send more than 700,000 SMS messages containing links to AITM phishing and cryptocurrency drainer pages.

The eCrime threat actor tracked in industry reporting as Atlas Lion adeptly abuses SaaS applications in their gift card fraud campaigns. Similar to Scattered Spider, Atlas Lion often gains initial access via SMS phishing (smishing), typically obtaining Microsoft 365 credentials. They use their access to compromised mailboxes to perform internal phishing in support of lateral movement. Atlas Lion uses access to HR-related SaaS applications to identify employees who have direct access to gift card resources and then searches for gift card-related strings across SSO-enabled applications, including Microsoft 365, chat platforms, and code repositories.

Malicious access to SaaS applications does not always follow a broader network compromise. In April 2024 and May 2024, a threat actor conducted a widely reported data theft and extortion campaign targeting customers of a data warehousing platform. To access customer database instances that did not require MFA or other controls such as network access policies, the threat actor leveraged compromised credentials obtained from information stealer logs that were widely available in eCrime channels and marketplaces.

This campaign targeted only the organizations' database instances, and no lateral movement or malicious activity impacting other applications or systems was observed. Threat actors could apply this tradecraft to steal data from other public-facing databases or cloud storage platforms not secured by MFA.

Adversaries will highly likely continue to target SaaS applications in 2025. This assessment is made with moderate confidence based on the proliferation of eCrime activity targeting SSO accounts and other relevant identities throughout 2024.