HW_SOURCE_FILE = 'hw02.py'

from operator import add, mul

def square(x):
    return x * x

def triple(x):
    return 3 * x

def identity(x):
    return x

def increment(x):
    return x + 1

def product(n, term):
    """Return the product of the first n terms in a sequence.

    n    -- a positive integer
    term -- a function that takes one argument

    >>> product(3, identity) # 1 * 2 * 3
    6
    >>> product(5, identity) # 1 * 2 * 3 * 4 * 5
    120
    >>> product(3, square)   # 1^2 * 2^2 * 3^2
    36
    >>> product(5, square)   # 1^2 * 2^2 * 3^2 * 4^2 * 5^2
    14400
    """
    "*** YOUR CODE HERE ***"

# The identity function, defined using a lambda expression!
identity = lambda k: k

def factorial(n):
    """Return n factorial for n >= 0 by calling product.

    >>> factorial(4)
    24
    >>> factorial(6)
    720
    >>> from construct_check import check
    >>> check(HW_SOURCE_FILE, 'factorial', ['Recursion', 'For', 'While'])
    True
    """
    "*** YOUR CODE HERE ***"

def make_adder(n):
    """Return a function that takes an argument K and returns N + K.

    >>> add_three = make_adder(3)
    >>> add_three(1) + add_three(2)
    9
    >>> make_adder(1)(2)
    3
    """
    "*** YOUR CODE HERE ***"
    return "***LAMBDA FUNCTION***"

def has_seven(k):
    """Returns True if at least one of the digits of k is a 7, False otherwise.

    >>> has_seven(3)
    False
    >>> has_seven(7)
    True
    >>> has_seven(2734)
    True
    >>> has_seven(2634)
    False
    >>> has_seven(734)
    True
    >>> has_seven(7777)
    True
    """
    "*** YOUR CODE HERE ***"

def summation(n, term):
    """Return the sum of the first n terms in the sequence defined by term.
    Implement using recursion! DO NOT USE 'WHILE' or 'FOR'

    >>> summation(5, lambda x: x * x * x) # 1^3 + 2^3 + 3^3 + 4^3 + 5^3
    225
    >>> summation(9, lambda x: x + 1) # 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
    54
    >>> summation(5, lambda x: 2**x) # 2^1 + 2^2 + 2^3 + 2^4 + 2^5
    62
    """
    "*** YOUR CODE HERE ***"

def weirdfib(n):
    """Return the nth weirdfibonacci number where the sequence starts with
    three ones. The weirdfibonacci adds three previous numbers in the sequence
    and place it next. Implement using recursion!
    Ex) 1, 1, 1, 3, 5, 9, 17, ...

    >>> weirdfib(1)
    1
    >>> weirdfib(3)
    1
    >>> weridfib(7)
    17
    >>> weridfib(20)
    46499
    """
    "*** YOUR CODE HERE ***"
