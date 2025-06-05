# COMMON ATTACK PATHS AND TACTICS  
## IN CLOUD INTRUSIONS

Figure 15 shows the attack paths and tactics that most threat actors employ during a cloud intrusion. Though threat actors may not use all of the displayed techniques in a given intrusion, multiple threat actors with varying motivations have used each technique across various cloud attacks.

Although threat actors have numerous methods to gain initial access, this illustrates the value of valid accounts in a successful cloud intrusion. These allow the threat actor to access the cloud control plane and use several other techniques for persistence, privilege escalation, defense evasion, discovery, collection, and impact.

Once the threat actor has access to a valid account, they often use it to collect more credentials from secured and unsecured sources so that they can access more accounts and further their activity. A valid account also allows them to access and execute commands on cloud-hosted VM infrastructure using tools such as a cloud VM management service, thus enabling them to collect files or deploy malware or ransomware.

Each adversary’s path depends on their goals and the hosting location of their target data. eCrime actors abuse cloud services to efficiently deploy ransomware and increase the deployment’s impact. Cloud-conscious state-nexus actors employ stealthier cloud tactics to gain long-term access to data with a lower risk of detection and meet their collection requirements.