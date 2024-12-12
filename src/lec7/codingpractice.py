
#Link Class is given!
class Link:
    """A linked list.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.first
    1
    >>> s.rest
    Link(2, Link(3))
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is Link.empty:
            return 'Link({})'.format(self.first)
        else:
            return 'Link({}, {})'.format(self.first, repr(self.rest))

    def __str__(self):
        """Returns a human-readable string representation of the Link

        >>> s = Link(1, Link(2, Link(3, Link(4))))
        >>> str(s)
        '<1 2 3 4>'
        >>> str(Link(1))
        '<1>'
        >>> str(Link.empty)  # empty tuple
        '()'
        """
        string = '<'
        while self.rest is not Link.empty:
            string += str(self.first) + ' '
            self = self.rest
        return string + str(self.first) + '>'

    def __eq__(self, other):
        """Compares if two Linked Lists contain same values or not.

        >>> s, t = Link(1, Link(2)), Link(1, Link(2))
        >>> s == t
        True
        """
        if self is Link.empty and other is Link.empty:
            return True
        if self is Link.empty or other is Link.empty:
            return False
        return self.first == other.first and self.rest == other.rest

def list_to_link(lst):
    """Takes a Python list and returns a Link with the same elements.

    >>> link = list_to_link([1, 2, 3])
    >>> link
    'Link(1, Link(2, Link(3)))'
    """
    "***YOUR CODE HERE***"

def link_to_list(link):
    """Takes a Link and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> link_to_list(link)
    [1, 2, 3, 4]
    >>> link_to_list(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"

def remove_all(link , value):
    """Remove all the nodes containing value. Assume there exists some
    nodes to be removed and the first element is never removed.

    >>> l1 = Link(0, Link(2, Link(2, Link(3, Link(1, Link(2, Link(3)))))))
    >>> remove_all(l1, 2)
    >>> l1
    Link(0, Link(3, Link(1, Link(3))))
    >>> remove_all(l1, 3)
    >>> l1
    Link(0, Link(1))
    """
    "*** YOUR CODE HERE ***"

def linked_sum(lnk, total):
    """Return the number of combinations of elements in lnk that
    sum up to total .
    >>> # Four combinations : 1 1 1 1 , 1 1 2 , 1 3 , 2 2
    >>> linked_sum (Link(1, Link(2, Link(3, Link(5)))), 4)
    4
    >>> linked_sum(Link(2, Link(3, Link(5))), 1)
    0
    >>> # One combination : 2 3
    >>> linked_sum(Link(2, Link(4, Link(3))), 5)
    1
    """
    "*** YOUR CODE HERE ***"

def has_cycle(s):
    """
    >>> has_cycle(Link.empty)
    False
    >>> a = Link(1, Link(2, Link(3)))
    >>> has_cycle(a)
    False
    >>> a.rest.rest.rest = a
    >>> has_cycle(a)
    True
    """
    "*** YOUR CODE HERE ***"
