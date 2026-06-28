"""Tests for src/calculator.py"""

import pytest
from src.calculator import add, subtract, multiply, divide


class TestAdd:
    """Tests for the add() function."""

    def test_add_positive_integers(self):
        assert add(2, 3) == 5

    def test_add_negative_integers(self):
        assert add(-2, -3) == -5

    def test_add_mixed_signs(self):
        assert add(-2, 3) == 1
        assert add(2, -3) == -1

    def test_add_floats(self):
        assert add(1.5, 2.5) == 4.0

    def test_add_zero(self):
        assert add(0, 5) == 5
        assert add(5, 0) == 5
        assert add(0, 0) == 0

    def test_add_large_numbers(self):
        assert add(1e10, 1e10) == 2e10

    def test_add_negative_and_positive(self):
        assert add(-100, 100) == 0

    def test_add_returns_float_type(self):
        result = add(1.0, 2.0)
        assert isinstance(result, float)


class TestSubtract:
    """Tests for the subtract() function."""

    def test_subtract_positive_integers(self):
        assert subtract(5, 3) == 2

    def test_subtract_negative_integers(self):
        assert subtract(-5, -3) == -2

    def test_subtract_mixed_signs(self):
        assert subtract(-5, 3) == -8
        assert subtract(5, -3) == 8

    def test_subtract_floats(self):
        assert subtract(5.5, 2.5) == 3.0

    def test_subtract_zero(self):
        assert subtract(5, 0) == 5
        assert subtract(0, 5) == -5
        assert subtract(0, 0) == 0

    def test_subtract_equal_values(self):
        assert subtract(5, 5) == 0
        assert subtract(-3, -3) == 0

    def test_subtract_order_matters(self):
        assert subtract(3, 5) == -2
        assert subtract(5, 3) == 2


class TestMultiply:
    """Tests for the multiply() function."""

    def test_multiply_positive_integers(self):
        assert multiply(3, 4) == 12

    def test_multiply_negative_integers(self):
        assert multiply(-3, -4) == 12

    def test_multiply_mixed_signs(self):
        assert multiply(-3, 4) == -12
        assert multiply(3, -4) == -12

    def test_multiply_by_zero(self):
        assert multiply(5, 0) == 0
        assert multiply(0, 5) == 0
        assert multiply(0, 0) == 0

    def test_multiply_floats(self):
        assert multiply(2.5, 4.0) == 10.0

    def test_multiply_by_one(self):
        assert multiply(5, 1) == 5
        assert multiply(1, 5) == 5

    def test_multiply_large_numbers(self):
        assert multiply(1e6, 1e6) == 1e12

    def test_multiply_negative_and_positive(self):
        assert multiply(-1, 5) == -5


class TestDivide:
    """Tests for the divide() function."""

    def test_divide_positive_integers(self):
        assert divide(10, 2) == 5.0

    def test_divide_negative_integers(self):
        assert divide(-10, -2) == 5.0

    def test_divide_mixed_signs(self):
        assert divide(-10, 2) == -5.0
        assert divide(10, -2) == -5.0

    def test_divide_floats(self):
        assert divide(7.5, 2.5) == 3.0

    def test_divide_by_one(self):
        assert divide(5, 1) == 5.0
        assert divide(1, 1) == 1.0

    def test_divide_returns_float(self):
        result = divide(5, 2)
        assert isinstance(result, float)

    def test_divide_by_zero_raises_zerodivisionerror(self):
        with pytest.raises(ZeroDivisionError):
            divide(5, 0)

    def test_divide_zero_by_number(self):
        assert divide(0, 5) == 0.0

    def test_divide_small_numbers(self):
        assert divide(1, 3) == pytest.approx(0.3333333333, rel=1e-6)

    def test_divide_large_numbers(self):
        assert divide(1e10, 1e5) == 1e5
