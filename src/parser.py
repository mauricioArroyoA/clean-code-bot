import re

def extract_refactored_code(response_text: str) -> str:
    """
    Extracts the refactored code block from the LLM response.
    """
    pattern = r"### Refactored Code\s*```(?:\w+)?\n([\s\S]*?)```"
    match = re.search(pattern, response_text)
    if match:
        return match.group(1).strip()

    return ""