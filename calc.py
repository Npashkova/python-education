"""This module contains calculator."""


class Calculator:
    """Calculate numbers."""
    def __init__(self, number_1, number_2):
        """Constructor"""
        self.number_1 = number_1
        self.number_2 = number_2

    def add(self):
        """Add numbers."""
        return self.number_1 + self.number_2

    def subtract(self):
        """Subtract numbers."""
        return self.number_1 - self.number_2

    def multiply(self):
        """Multiply numbers."""
        return self.number_1 * self.number_2

    def divide(self):
        """Divide numbers."""
        return self.number_1 / self.number_2


numbers_1 = Calculator(35, 7)
print(numbers_1.add())
