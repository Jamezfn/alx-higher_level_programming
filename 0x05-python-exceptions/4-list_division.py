#!/usr/bin/python3
"""Divide a list"""
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by element 2 lists."""
    new_list = []
    for i in range(list_length):
        try:
            a = my_list_1[i]
            b = my_list_2[i]
            if not isinstance(a, (float, int)) or not isinstance(b, (float, int)):
                raise TypeError
            res = a / b
        except TypeError:
            print("wrong type")
            res = 0
        except ZeroDivisionError:
            print("division by 0")
            res = 0
        except IndexError:
            print("out of range")
            res = 0
        finally:
            new_list.append(res)
    return new_list
