import re
from pathlib import Path

def remove_fields_from_bib(input_file: str, output_file: str, fields: list[str]) -> None:
    """
    Remove specified fields (e.g., 'url', 'issn') from all BibTeX entries in a .bib file.
    Also cleans up blank lines before closing braces.
    """
    bib_text = Path(input_file).read_text(encoding="utf-8")

    for field in fields:
        # Regex to remove lines like 'field = {...}' or 'field = "..."'
        pattern = rf'^\s*{field}\s*=\s*[{{"].*?[}}"],?\s*$'
        bib_text = re.sub(pattern, '', bib_text, flags=re.MULTILINE | re.IGNORECASE)

    # Remove blank lines before a closing brace }
    bib_text = re.sub(r'\n\s*\n(\s*})', r'\n\1', bib_text)

    # Collapse triple+ newlines into doubles
    bib_text = re.sub(r'\n{3,}', '\n\n', bib_text)

    Path(output_file).write_text(bib_text, encoding="utf-8")
    print(f"Removed {fields} from {input_file}, saved as {output_file}")


if __name__ == "__main__":
    # Example usage: change these as needed
    input_file = "references.bib"
    output_file = "references_cleaned.bib"
    fields_to_remove = ["url"]   # add any fields you want removed

    remove_fields_from_bib(input_file, output_file, fields_to_remove)
