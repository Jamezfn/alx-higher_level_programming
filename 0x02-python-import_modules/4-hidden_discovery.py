#!/usr/bin/python3
"""Who are you?"""
if __name__ == "__main__":
    """Prints all names defined in a file"""
    import hidden_4
    names = dir(hidden_4)
    filter_name = []
    for name in names:
        if not name.startswith('__'):
            filter_name.append(name)
    print(filter_name)
