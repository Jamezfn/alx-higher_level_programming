#!/usr/bin/python3
"""Text indentation"""
def text_indentation(text):
    """Prints a text with 2 new lines after each of these characters: ., ?"""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    i = 0
    length = len(text)
    buffer = ''
    while i < length:
        ch = text[i]
        buffer += ch
        if ch in ['.', '?', ':']:
            print(buffer.strip())
            buffer = ""
            print()
        elif ch == '\n':
            if buffer.strip():
                print(buffer.strip())
            else:
                print()
            buffer = ''
        i += 1
    if buffer.strip():
        print(buffer.strip(), end='')
