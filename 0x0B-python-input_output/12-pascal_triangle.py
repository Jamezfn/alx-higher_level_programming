#!/usr/bin/python3
"""Pascal's Triangle"""
def pascal_triangle(n):
    """Returns a list of lists of integers"""
    if n <= 0:
        return []
    triangle = []
    for i in range(n):
        if i == 0:
            triangle.append([1])
        else:
            prev = triangle[i - 1]
            row = [1]
            for j in range(1, i):
                row.append(prev[j - 1] + prev[j])
            row.append(1)
            triangle.append(row)

    return triangle
