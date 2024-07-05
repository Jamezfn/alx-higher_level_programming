#!/usr/bin/python3
''' Defines peak-finding algorithm'''

def find_peak(list_of_int):
    '''Return peak in a list of unsorted int'''
    if not list_of_int:
        return None

    def find_peak_util(arr, low, high):
        mid = (low + high) // 2

        # If mid is the peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]

        # If the left neighbor is greater, move to the left half
        if mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)

        # If the right neighbor is greater, move to the right half
        return find_peak_util(arr, mid + 1, high)

    return find_peak_util(list_of_int, 0, len(list_of_int) - 1)

# Test cases
if __name__ == "__main__":
    test_cases = [
        [1, 2, 4, 6, 3],
        [4, 2, 1, 2, 3, 1],
        [2, 2, 2],
        [],
        [-2, -4, 2, 1],
        [4, 2, 1, 2, 2, 2, 3, 1]
    ]

    for test in test_cases:
        print(find_peak(test))
