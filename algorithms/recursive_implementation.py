"""Module for recursive factorial implementation"""


def factorial(number):
    """Recursive function to count factorial
    Args: number: int
    Return: number!: int
    """
    if not isinstance(number, int):
        raise TypeError('Function accept only integers')
    if number < 0:
        raise ValueError('Function accept only positive numbers')
    if number in (0, 1):
        return 1
    else:
        return number * factorial(number - 1)



