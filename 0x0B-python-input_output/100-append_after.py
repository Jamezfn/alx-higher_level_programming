#!/usr/bin/python3
"""Search and update"""
def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing a specific string"""
    with open(filename, 'r', encoding='utf-8') as f:
        lines = file.readlines()
    with open(filename, 'w' encoding='utf-8') as f:
        for line in lines:
            file.write(line)
            if search_string in line:
                f.write(new_string)
