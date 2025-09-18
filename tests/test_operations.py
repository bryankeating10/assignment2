import pytest
from app.operations import add, subtract, multiply, division

# Positive Tests
def test_addition_positive():
	"""Test addition with positive numbers."""
	assert add(2, 3) == 5