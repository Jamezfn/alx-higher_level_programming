#!/usr/bin/python3

if __name__ == "__main__":
    """Prints all the names defined by the compiled module hidden_4.pyc"""
    import hidden_4

    names = dir(hidden_4)
    filter_names = []
    for name in names:
        if not name.startswith("__"):
            filtered_namesappend(name)
    print(filter_names)
