# GenAI Supports Social Engineering

LLMs and genAI models that create photorealistic imagery can generate convincing content at scale with minimal expertise. These tools can support social engineering efforts or IO. Despite the relative novelty of genAI, CrowdStrike has identified several examples of adversaries using it.

## Social Engineering

Operators associated with DPRK-nexus adversary FAMOUS CHOLLIMA obtain positions at companies worldwide under fake personas, occasionally using genAI tools to socially engineer recruiters during the job application process. They also create fictitious LinkedIn profiles with genAI-created text and fake profile images. During interviews, many FAMOUS CHOLLIMA candidates provide answers likely derived from external sources. LLMs likely support these interviews by rapidly generating plausible responses.

GenAI is also used for BEC and fraud. In February 2024, unidentified threat actor(s) used public footage of a target company’s chief financial officer and other employees to create credible deepfake video clones and socially engineer the victim into transferring 25.6 million USD to the threat actor(s). In May 2024, industry reporting indicated threat actors had impersonated the CEO of an international professional services entity and attempted to solicit fraudulent payments. The threat actor also appeared to have used genAI to clone the CEO’s voice and attempted to persuade the call recipient to transfer funds.

The relationship between genAI and social engineering is also evidenced by the evolving focus of mobile malware. Since late 2023, the **GoldPickaxe** malware has been employed to steal biometric facial data from iOS and Android devices throughout the Asia Pacific (APAC) region. The malware, which cannot bypass authentication, captures images and videos to generate deepfake videos or perform face-swap operations.

Academic research further highlights the appeal of LLMs for social engineering. LLMs can generate phishing email content or credential harvesting websites at least as well as humans. A 2024 study of phishing email click-through rates indicated LLM-generated phishing messages had a significantly higher click-through rate (54%) than likely human-written phishing messages (12%).[^1] A separate 2024 study found detection rates for LLM-generated phishing pages were comparable to those for human-created phishing pages.[^2]

| Study              | LLM-Generated Click-Through Rate | Human-Written Click-Through Rate |
|--------------------|----------------------------------|----------------------------------|
| 2024 Phishing      | 54%                              | 12%                              |

[^1]: [https://arxiv.org/pdf/2412.00586](https://arxiv.org/pdf/2412.00586)
[^2]: [https://arxiv.org/pdf/2310.19181v2](https://arxiv.org/pdf/2310.19181v2)