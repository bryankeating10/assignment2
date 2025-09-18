import pytest
from app.operations import add, subtract, multiply, division

# Positive Tests
def test_addition_positive():
	"""Test addition with positive numbers."""
	assert add(2, 3) == 5

def test_subtraction_positive():
	"""Test subtraction with positive numbers."""
	assert subtract(5, 2) == 3

def test_multiplication_positive():
	"""Test multiplication with positive numbers."""
	assert multiply(4, 5) == 20

def test_division_positive():
	"""Test division with positive numbers."""
	assert division(10, 2) == 5

# Negative Tests
def test_addition_negative():
	"""Test addition with negative numbers."""
	assert add(-2, -3) == -5

def test_subtraction_negative():
	"""Test subtraction with negative numbers."""
	assert subtract(-5, -2) == -3

def test_multiplication_negative():
	"""Test multiplication with negative numbers."""
	assert multiply(-4, -5) == 20

def test_division_negative():
	"""Test division with negative numbers."""
	assert division(-10, -2) == 5

# Division by Zero Test
def test_division_by_zero():
	"""Test division by zero."""
	with pytest.raises(ValueError, match="Division by zero is not allowed"):
		division(5, 0)