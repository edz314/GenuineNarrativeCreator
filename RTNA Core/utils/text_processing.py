# core/utils/text_processing.py

import re

def clean_text(text: str) -> str:
    """
    Cleans and formats text for better readability.

    Args:
        text: The input text string.

    Returns:
        The cleaned and formatted text string.
    """

    # Remove extra whitespace
    text = ' '.join(text.split())

    # Capitalize the first letter of sentences
    text = re.sub(r'(?<!\w\.\w.)(?<![A-Z][a-z]\.)(?<=\.|\?)\s', lambda match: match.group(0).upper(), text)

    return text

def format_narrative(text: str, line_width: int = 80) -> str:
    """
    Formats a narrative text by wrapping lines to a specified width.

    Args:
        text: The input narrative text.
        line_width: The maximum width of a line.

    Returns:
        The formatted narrative text with wrapped lines.
    """

    words = text.split()
    lines = []
    current_line = ""

    for word in words:
        if len(current_line + word) <= line_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    if current_line:
        lines.append(current_line.strip())

    return "\n".join(lines)
