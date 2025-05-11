#!/usr/bin/pyrhon3
"""Load, add, save"""
import sys

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

def main():
    """Adds all arguments to a Python list, and then save them to a file."""
    filename = "add_item.json"
    try:
        items = load_from_json_file(filename)
    except Exception:
        items = []
    save_to_json_file(items, filename)

if __name__ == '__main__':
    main()
