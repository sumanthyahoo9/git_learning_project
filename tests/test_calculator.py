"""Unit tests for the calculator module."""
# tests/test_calculator.py
import pytest
from src.calculator import Calculator


class TestCalculator:
    """Module to test the calculator class."""

    def setup_method(self):
        """Initialize test fixtures before each test method."""
        self.calc = Calculator()

    def test_add(self):
        """Test addition functionality."""
        assert self.calc.add(2, 3) == 5
        assert self.calc.add(-1, 1) == 0
        assert self.calc.add(0, 0) == 0

    def test_subtract(self):
        """Test subtraction functionality."""
        assert self.calc.subtract(5, 3) == 2
        assert self.calc.subtract(1, 1) == 0
        assert self.calc.subtract(0, 5) == -5

    def test_multiply(self):
        """Test multiplication functionality."""
        assert self.calc.multiply(2, 3) == 6
        assert self.calc.multiply(-2, 3) == -6
        assert self.calc.multiply(0, 5) == 0

    def test_divide(self):
        """Test division functionality."""
        assert self.calc.divide(6, 2) == 3
        assert self.calc.divide(5, 2) == 2.5
        with pytest.raises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        """Test power functionality."""
        assert self.calc.power(2, 3) == 8
        assert self.calc.power(2, 0) == 1
        assert self.calc.power(0, 5) == 0
