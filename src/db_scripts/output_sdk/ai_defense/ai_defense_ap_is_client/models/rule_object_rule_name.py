from enum import Enum


class RuleObjectRuleName(str, Enum):
    CODE_DETECTION = "Code Detection"
    HARASSMENT = "Harassment"
    HATE_SPEECH = "Hate Speech"
    PCI = "PCI"
    PHI = "PHI"
    PII = "PII"
    PROFANITY = "Profanity"
    PROMPT_INJECTION = "Prompt Injection"
    SEXUAL_CONTENT_EXPLOITATION = "Sexual Content & Exploitation"
    SOCIAL_DIVISION_POLARIZATION = "Social Division & Polarization"
    VIOLENCE_PUBLIC_SAFETY_THREATS = "Violence & Public Safety Threats"

    def __str__(self) -> str:
        return str(self.value)
