# Tree definition

def tree(label, branches=[]):
    """Construct a tree with the given label value and a list of branches."""
    for branch in branches:
        assert is_tree(branch), 'branches must be trees'
    return [label] + list(branches)

def label(tree):
    """Return the label value of a tree."""
    return tree[0]

def branches(tree):
    """Return the list of branches of the given tree."""
    return tree[1:]

def is_tree(tree):
    """Returns True if the given tree is a tree, and False otherwise."""
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in branches(tree):
        if not is_tree(branch):
            return False
    return True

def is_leaf(tree):
    """Returns True if the given tree's list of branches is empty, and False
    otherwise.
    """
    return not branches(tree)

def print_tree(t, indent=0):
    """Print a representation of this tree in which each node is
    indented by two spaces times its depth from the root.

    >>> print_tree(tree(1))
    1
    >>> print_tree(tree(1, [tree(2)]))
    1
      2
    >>> numbers = tree(1, [tree(2), tree(3, [tree(4), tree(5)]), tree(6, [tree(7)])])
    >>> print_tree(numbers)
    1
      2
      3
        4
        5
      6
        7
    """
    print('  ' * indent + str(label(t)))
    for b in branches(t):
        print_tree(b, indent + 1)

def copy_tree(t):
    """Returns a copy of t. Only for testing purposes.

    >>> t = tree(5)
    >>> copy = copy_tree(t)
    >>> t = tree(6)
    >>> print_tree(copy)
    5
    """
    return tree(label(t), [copy_tree(b) for b in branches(t)])

"""REQUIRED QUESTIONS"""

def sum_of_nodes(t):
    """
    >>> t = tree(9, [tree(2), tree(4, [tree(1)]), tree(4, [tree(7), tree(3)])])
    >>> sum_of_nodes(t) # 9 + 2 + 4 + 4 + 1 + 7 + 3 = 30
    30
    """
    "*** YOUR CODE HERE ***"

def map(fn, seq):
    """Applies fn onto each element in seq and returns a list.

    >>> map(lambda x: x*x, [1, 2, 3])
    [1, 4, 9]
    """
    "*** YOUR CODE HERE ***"

def filter(pred, seq):
    """Keeps elements in seq only if they satisfy pred.

    >>> filter(lambda x: x % 2 == 0, [1, 2, 3, 4])
    [2, 4]
    """
    "*** YOUR CODE HERE ***"

def reduce(combiner, seq):
    """Combines elements in seq using combiner.

    >>> reduce(lambda x, y: x + y, [1, 2, 3, 4])
    10
    >>> reduce(lambda x, y: x * y, [1, 2, 3, 4])
    24
    >>> reduce(lambda x, y: x * y, [4])
    4
    """
    "*** YOUR CODE HERE ***"

def sublist(lst):
    """Returns all sublists of the input lst.

    >>> sublist([])
    [[]]
    >>> sublist([1])
    [[], [1]]
    >>> sublist([1,2,3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    "*** YOUR CODE HERE ***"

"""OPTIONAL QUESTION"""

def sublist_oneline(lst, result=[[]]):
    """Try 1 line coding with sublist!s

    >>> sublist([])
    [[]]
    >>> sublist([1])
    [[], [1]]
    >>> sublist([1,2,3])
    [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
    """
    "*** YOUR CODE HERE ***"
