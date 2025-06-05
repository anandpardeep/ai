# Vulnerability Research and Exploitation

GenAI models are both a target and enabler of exploit-related activity. As with CNO, LLMs can accelerate vulnerability research and testing by potentially speeding up development timelines. However, confirmed evidence of LLM-aided vulnerability exploit development, and exploitation of LLMs in the wild, remains rare.

In 2024, Iran-nexus actors were among the most notable groups seeking genAI support in the vulnerability landscape. Iranian government initiatives aspire to leverage AI to develop assistants and enable patching systems for domestic networks. Moreover, Iran’s government aims to use LLMs in vulnerability research and exploit development.

Threat actors’ interest in genAI-enabled exploit development is further evidenced by observed activity in April 2024. An unattributed threat actor likely used genAI to develop an alleged exploit for a command injection vulnerability in GlobalProtect PAN-OS Gateway (CVE-2024-3400). While the exploit was ultimately ineffective, CrowdStrike Intelligence observed exploitation attempts as threat actors attempted to rapidly repurpose LLM-generated exploits in the wild.

Alternatively, threat actors and researchers are exploring potential attack vectors associated with vulnerabilities within genAI models. Techniques such as prompt injection may potentially circumvent access controls, achieve code execution, or raise the potential for unintentional disclosure of sensitive information. Further, genAI platforms with external resources can introduce vulnerabilities typically associated with many web applications, such as server-side request forgery and SQL injection.

# Cloud-Conscious Threat Actors

Cloud-conscious adversaries are beginning to explore genAI and LLMs for their operations. As cloud adoption expands and genAI becomes more integrated into services such as Azure AI Foundry (formerly Azure AI Studio),[^3] threat actors will likely begin exploiting genAI services for data theft, model manipulation, unauthorized access, and other malicious purposes.

CrowdStrike Intelligence expects cloud-conscious threat actors with varied skill levels will increasingly exploit technical vulnerabilities and misconfigurations in the growing genAI-driven cloud ecosystem. They will seek to abuse AI services, and services that customers integrate using AI, to acquire data of strategic interest.

---

## CASE HIGHLIGHT: LLMJACKING

> LLMJacking involves threat actors exploiting stolen cloud credentials to access AI services to fuel an expanding criminal market for unauthorized LLM queries. In Q2 2024, an unknown threat actor compromised a North American consulting victim. In this operation, the threat actor prepared for LLMJacking by listing available foundational machine learning (ML) models for a cloud-based AI service. For unavailable models, the threat actor attempted to gain access by leveraging an API that enables users to request permission for restricted machine learning models by submitting a justification.
>
> In a separate Q4 2024 campaign, a threat actor compromised a North America-based technology company and similarly attempted to use the same API to obtain access to models hosted on the cloud platform. In both cases, the threat actors likely intended to resell ML model access to other threat actors seeking to use the models for malicious purposes.

---

[^3]: [https://azure.microsoft.com/en-us/blog/build-your-own-copilot-with-microsoft-azure-ai-studio/](https://azure.microsoft.com/en-us/blog/build-your-own-copilot-with-microsoft-azure-ai-studio/)