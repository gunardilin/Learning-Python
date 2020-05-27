"""This is my first testcode for pytest module."""
import pytest
from nearest import nearest_square

def test_nearest_square_5():
    assert(nearest_square(5) == 4)
    
def test_nearest_square_n12():
    assert(nearest_square(-12) == 0)

def test_nearest_square_9():
    assert(nearest_square(9) == 0)

def test_nearest_square_23():
    assert(nearest_square(23) == 16)