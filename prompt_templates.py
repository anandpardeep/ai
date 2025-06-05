# prompt_templates.py

class PromptTemplates:
    @staticmethod
    def image_summary_prompt() -> str:
        return (
            "This image is from a cybersecurity threat report (CrowdStrike). "
            "If the image contains meaningful text, extract and summarize it. "
            "Ignore decorations, logos, mascots, or background illustrations. "
            "Only describe it if it conveys actual content useful to a security analyst. "
            "If it appears to be a logo, mascot, background art, or contains no meaningful content, respond with exactly: 'NA'."
        )

    @staticmethod
    def bla_bla() -> str:
        return "This is another prompt we might need later..."
