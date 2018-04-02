from operator import add, mul

def mario_number(level):
    """Return the number of ways that mario can traverse the
    level where mario can either hop by one digit or two
    digits each turn a level is defined as being an integer
    where a 1 is something mario can step on and 0 is
    something mario cannot step on.
    >>> mario_number(10101)
    1
    >>> mario_number(11101)
    2
    >>> mario_number(100101)
    0
    """
    "***YOUR CODE HERE***"

def if_this_not_that(i_list, this):
    """Define a function which takes a list of integers `i_list` and an integer
    `this`. For each element in `i_list`, print the element if it is larger
    than `this`; otherwise, print the word "that".

    >>> if_this_not_that([1, 2, 3, 4, 5], 3)
    that
    that
    that
    4
    5
    >>> if_this_not_that([10, 9, 8, 7], 8)
    10
    9
    that
    that
    """
    "***YOUR CODE HERE***"

def splice(a, b, k):
    """Return a list of the first k elements of a, then all of b,
    then the rest of a.
    >>> splice([2, 3, 4, 5], [6, 7], 2)
    [2, 3, 6, 7, 4, 5]
    >>> splice([1, 2, 5, 7], [1, 1], 0)
    [1, 1, 1, 2, 5, 7]
    """
    "***YOUR CODE HERE***"

def all_splice(a, b, c):
    """Return a list of all k such that splicing b into a at position k gives c.
    >>> all_splice([1, 2], [3, 4], [1, 3, 4, 2])
    [1]
    >>> all_splice([1, 2, 1, 2], [1, 2], [1, 2, 1, 2, 1, 2])
    [0, 2, 4]
    """
    "***YOUR CODE HERE***"

def ways(start, end, k, ations):
    """Return the number of ways of reaching end from start by taking up to k actions.
    >>> ways(-1, 1, 5, [abs, lambda x: x+2]) # abs(-1) or -1+2, but not abs(abs(-1))
    2
    >>> ways(1, 10, 5, [lambda x: x+1, lambda x: x+4]) # 1+1+4+4, 1+4+4+1, or 1+4+1+4
    3
    >>> ways(1, 20, 5, [lambda x: x+1, lambda x: x+4])
    0
    >>> ways([3], [2, 3, 2, 3], 4, [lambda x: [2]+x, lambda x: 2*x, lambda x: x[:-1]])
    3
    """
    "***YOUR CODE HERE***"
