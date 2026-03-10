import os

EXTENSION_LANGUAGE_MAP = {
    ".py": "Python",
    ".js": "JavaScript",
    ".ts": "TypeScript",
    ".java": "Java",
    ".php": "PHP",
    ".cs": "C#",
    ".cpp": "C++",
    ".c": "C",
    ".go": "Go",
    ".rb": "Ruby"
}


def detect_language(file_path: str) -> str:
    """
    Detects programming language based on file extension.
    """

    _, ext = os.path.splitext(file_path)
    return EXTENSION_LANGUAGE_MAP.get(ext, "Unknown")