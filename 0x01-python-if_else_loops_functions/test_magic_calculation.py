#!/usr/bin/python3
from magic_calculation import magic_calculation

def test_magic_calculation():
    # Test cases with expected results
    assert magic_calculation(1, 2, 3) == 3, "Test case 1 failed"
    assert magic_calculation(2, 1, 3) == 3, "Test case 2 failed"
    assert magic_calculation(2, 2, 1) == 3, "Test case 3 failed"
    assert magic_calculation(3, 2, 1) == 5, "Test case 4 failed"
    assert magic_calculation(1, 2, 1) == 1, "Test case 5 failed"
    
    print("All test cases passed")

if __name__ == "__main__":
    test_magic_calculation()

