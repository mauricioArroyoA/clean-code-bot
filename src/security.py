import re

SUSPICIOUS_PATTERNS = [
    r"ignore previous instructions",
    r"system prompt",
    r"execute shell",
    r"run command",
    r"delete file",
    r"access system",
    r"bypass security",
]


def detect_prompt_injection(code: str) -> bool:
    """
    Detects suspicious prompt injection patterns inside the code.
    Returns True if a potential injection is found.
    """

    code_lower = code.lower()
    for pattern in SUSPICIOUS_PATTERNS:
        if re.search(pattern, code_lower):
            return True

    return False


def sanitize_code(code: str) -> str:
    """
    Basic sanitization of user input.
    Removes suspicious control characters.
    """

    sanitized = code.replace("\x00", "")
    return sanitized