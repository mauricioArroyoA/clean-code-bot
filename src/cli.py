import click
from groq import Groq
from prompt_template import build_refactor_prompt
from security import detect_prompt_injection, sanitize_code
from parser import extract_refactored_code
from language_detector import detect_language
from file_utils import read_code_file, generate_output_path

@click.command()
@click.argument("file_path", type=click.Path(exists=True))
def main(file_path):
    code = read_code_file(file_path)
    language = detect_language(file_path)
    code = sanitize_code(code)

    if detect_prompt_injection(code):
        click.echo("\nPotential prompt injection detected!")
        click.echo("Aborting request for security reasons.\n")
        return

    client = Groq(
        api_key="GROQ_API_KEY"
    )
    prompt = build_refactor_prompt(code, language)
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    response_text = response.choices[0].message.content
    refactored_code = extract_refactored_code(response_text)
    output_path = generate_output_path(file_path)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(refactored_code)

    click.echo(f"\n💾 Refactored code saved to: {output_path}")


if __name__ == "__main__":
    main()