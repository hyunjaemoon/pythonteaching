from operator import add , mul

def combine(n, f, result):
    """Implement the combine function, which takes a non-negative integer n,
    a two-argument function f, and a number result. It applies f to the first
    digit of n and the result of combining the rest of the digits of n by
    repeatedly applying f (see the doctests).
    If n has no digits (because it is zero), combine returns result

    >>> combine (3 , mul , 2) # mul (3 , 2)
    6
    >>> combine (43 , mul , 2) # mul (4 , mul (3 , 2))
    24
    >>> combine (6502 , add , 3) # add (6 , add (5 , add (0 , add (2 , 3)))
    16
    >>> combine (239 , pow , 0) # pow (2 , pow (3 , pow (9 , 0)))
    8
    """
    "*** YOUR CODE HERE***"

def count_stair_ways(n):
    """I want to go up a flight of stairs that has n steps.
    I can either take 1 or 2 steps each time. How many different
    ways can I go up this flight of stairs? Write a function
    count_stair_ways that solves this problem for me.
    Assume n is positive.

    >>> count_stair_ways(3)        # 1 + 2, 2 + 1, 1 + 1 + 1
    3
    >>> count_stair_ways(1)        # There is 1 way to partition 1 step
    1
    >>> count_stair_ways(5)
    8
    >>> count_stair_ways(8)
    34
    """
    "*** YOUR CODE HERE***"

def count_k(n, k):
    """Consider a special version of the count_stairways problem,
    where instead of taking 1 or 2 steps, we are able to take up to
    and including k steps at a time.

    >>> count_k(3, 3)          # 3, 2 + 1, 1 + 2, 1 + 1 + 1
    4
    >>> count_k(4, 4)
    8
    >>> count_k(10, 3)
    273
    >>> count_k(300, 1)        # Only one step at a time
    1
    """
    "*** YOUR CODE HERE***"

def kbonacci(n, k):
    """ A k-bonacci sequence starts with K-1 zeros and then a one.
    Each subsequent element is the sum of the previous K elements.
    The 2-bonacci sequence is the standard Fibonacci sequence.
    The 3-bonacci and 4-bonacci sequences each start with the
    following ten elements:

    n               : 0 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 , 9 , ...
    kbonacci (n , 2): 0 , 1 , 1 , 2 , 3 , 5 , 8 , 13 , 21 , 35 , ...
    kbonacci (n , 3): 0 , 0 , 1 , 1 , 2 , 4 , 7 , 13 , 24 , 44 , ...
    kbonacci (n , 4): 0 , 0 , 0 , 1 , 1 , 2 , 4 , 8 , 15 , 29 , ...

    >>> kbonacci (1 , 4)
    0
    >>> kbonacci (3 , 4)
    1
    >>> kbonacci (9 , 4)
    29
    >>> kbonacci (4 , 2)
    3
    >>> kbonacci (8 , 2)
    21
    """
    "*** YOUR CODE HERE***"
