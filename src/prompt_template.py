def build_refactor_prompt(code: str, language: str) -> str:
    """
    Builds the Chain-of-Thought prompt used to analyze and refactor code.
    """
    prompt = f"""
You are an expert software engineer specializing in {language}.

Your task is to analyze and refactor the provided code so that it follows
clean code practices and SOLID principles.
Follow these steps carefully:

Step 1 — Code Analysis
Explain what the code does and describe its current structure.

Step 2 — Identify Problems
List issues related to:
- readability
- maintainability
- naming
- duplication
- SOLID violations
- missing documentation

Step 3 — Refactoring Plan
Explain how the code should be improved.

Step 4 — Refactored Code
Provide a clean and improved version of the code.

Requirements for the refactored code:
- follow SOLID principles
- improve naming conventions
- add proper documentation (Docstrings or JSDoc)
- improve formatting and structure
- keep the original functionality

Return your response in EXACTLY the following format — do not deviate:

### Code Analysis
<analysis>

### Problems Found
<issues>

### Refactoring Plan
<plan>

### Refactored Code
```python
<improved code>
```

Here is the code to analyze:
{code}
"""
    return prompt