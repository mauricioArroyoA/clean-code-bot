import os

def read_code_file(file_path: str) -> str:
    """
    Reads a code file and returns its contents.
    """

    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        raise RuntimeError(f"Error reading file: {e}")
    

def generate_output_path(input_path: str) -> str:
    """
    Generates the output file path by appending `_after`
    before the file extension.
    """

    directory = os.path.dirname(input_path)
    filename = os.path.basename(input_path)
    name, ext = os.path.splitext(filename)
    new_filename = f"{name}_after{ext}"
    return os.path.join(directory, new_filename)