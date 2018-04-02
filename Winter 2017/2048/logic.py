
from random import *

#######
#Task 1a#
#######

#Question 1
def new_game(n):
    """Returns a nxn matrix with all entries of zeros

    Purpose: To initiate the 2048 game!

    >>> new_game(1)
    [[0]]
    >>> new_game(2)
    [[0, 0], [0, 0]]
    >>> new_game(3)
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    """
    "***YOUR CODE HERE***"

###########
# Task 1b #
###########

#Question 2
def add_two_fixed(mat):
    """Mutate and Return a modified matrix 'mat' with the number 2 added to
    the matrix. It is important that you must mutate the input mat.

    Purpose: After each move, a block '2' must be added to continue the game.

    IMPORTANT NOTE: Although the original 2048 game adds the number 2 randomly,
    it is impossible to check the accuracy of the code for randomness. So I
    would suggest adding the number 2 as you encounter the smallest row with
    a zero entry. Check the test cases to make more sense.

    IMPORTANT NOTE 2: DO MODIFY THE INPUT MAT

    >>> add_two_fixed([[0]])
    [[2]]
    >>> add_two_fixed([[2, 2, 2], [2, 2, 2], [2, 2, 0]])
    [[2, 2, 2], [2, 2, 2], [2, 2, 2]]
    >>> add_two_fixed([[2, 0, 2], [0, 2, 2], [2, 2, 2]])
    [[2, 2, 2], [0, 2, 2], [2, 2, 2]]
    >>> add_two_fixed([[0, 0], [0, 0]])
    [[2, 0], [0, 0]]
    """
    "***YOUR CODE HERE***"

#The function add_two will be the one that will be used for the puzzle.py demonstration.
def add_two(mat):
    a=randint(0,len(mat)-1)
    b=randint(0,len(mat)-1)
    while(mat[a][b]!=0):
        a=randint(0,len(mat)-1)
        b=randint(0,len(mat)-1)
    mat[a][b]=2
    return mat


###########
# Task 1c #
###########


#Question 3
def game_state(mat):
    """Return either 'win', 'not over', or 'lose' based on the matrix given.
    The description of the condition are as followed:

    'win': If you have at least 1 entry with 2048, you will return 'win'
    'not over': 1. If there exists a same number on subsequent rows or columns, you will return 'not over'
                2. If there exists a zero entry, you will return 'not over'
    'lose': If either 'win' or 'not over' conditions are not satisfied, you will return 'lose'
    Check the test cases to make more sense

    Purpose: After each move, the game can decide whether you've finished the game or not.

    >>> game_state([[0, 0, 0, 0],[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 2048]])
    'win'
    >>> game_state([[2, 4, 2, 4],[4, 2, 2048, 2], [4, 2, 2, 2], [4, 4, 2, 4]])
    'win'
    >>> game_state([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 8, 8]])
    'not over'
    >>> game_state([[2, 4, 2, 4], [4, 0, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]])
    'not over'
    >>> game_state([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 8], [4, 2, 4, 8]])
    'not over'
    >>> game_state([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 2]])
    'lose'
    """
    "***YOUR CODE HERE***"

###########
# Task 2a #
###########

def reverse(mat):
    """Return a new matrix where each row is flipped in reverse.

    Purpose: Based on your movements, (up, down, left, right), We will be using
    reverse and transpose functions so that we could unify the merge and cover_up
    functions later on. For better understanding please check the up, down, left,
    and right implementation on the very bottom of logic.py

    IMPORTANT NOTE: DO NOT MODIFY THE INPUT MAT

    >>> reverse([[3, 2, 1], [6, 5, 4], [9, 8 ,7]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> reverse([[1, 0], [0, 2]])
    [[0, 1], [2, 0]]
    """
    "***YOUR CODE HERE***"

###########
# Task 2b #
###########

def transpose(mat):
    """ Return a new matrix, which is a transpose of the input mat.

    Purpose: same as reverse

    IMPORTANT NOTE: DO NOT MODIFY THE INPUT MAT

    >>> transpose([[1, 3], [2, 4]])
    [[1, 2], [3, 4]]
    >>> transpose([[1, 0, 0], [0, 1, 0], [0, 0, 1]])
    [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
    >>> transpose([[1, 4, 7], [2, 5, 8], [3, 6, 9]])
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    """
    "***YOUR CODE HERE***"

##########
# Task 3 #
##########

def cover_up(mat):
    """Return a tuple of a matrix and a boolean. For a matrix, you will push
    all the entries to the left. For a boolean, you will put True if at least
    one number is pushed. A tuple is a sequence of immutable Python objects,
    use round parentheses: (1, 2) or ([1], True)

    Purpose: Based on the user input, the matrix will change its entries by
    pushing and merging. You will implement the pushing part here. By having
    the boolean, you can decide whether the user input does nothing or something.

    IMPORTANT NOTE: DO NOT MODIFY THE INPUT MAT

    >>> cover_up([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], False)
    >>> cover_up([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 0]])
    ([[2, 4, 2, 4], [4, 2, 4, 2], [2, 4, 2, 4], [4, 2, 4, 0]], False)
    >>> cover_up([[2, 0, 4, 0], [2, 0, 2, 0], [0, 4, 0, 8], [2, 0, 8, 0]])
    ([[2, 4, 0, 0], [2, 2, 0, 0], [4, 8, 0, 0], [2, 8, 0, 0]], True)
    >>> cover_up([[2, 0, 2, 0], [0, 0, 0, 16], [2, 4, 0, 0], [0, 0, 16, 0]])
    ([[2, 2, 0, 0], [16, 0, 0, 0], [2, 4, 0, 0], [16, 0, 0, 0]], True)
    """
    "***YOUR CODE HERE***"

def merge(mat):
    """Return a tuple of a matrix and a boolean. For a matrix, you will merge
    the numbers that are next to each other and place it on the left. For a boolean,
    you will put True if at least one number is merged.

    Purpose: Similar to cover_up, you will implement the merging part here.

    IMPORTANT NOTE: DO MODIFY THE INPUT MAT

    >>> merge([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ([[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], False)
    >>> merge([[2, 2, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]])
    ([[4, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], True)
    >>> merge([[2, 2, 2, 2], [4, 4, 4, 2], [2, 0, 2, 0], [2, 0, 0, 2]])
    ([[4, 0, 4, 0], [8, 0, 4, 2], [2, 0, 2, 0], [2, 0, 0, 2]], True)
    >>> merge([[2, 4, 0, 0], [2, 0, 0, 0], [4, 2, 0, 0], [2, 4, 2, 0]])
    ([[2, 4, 0, 0], [2, 0, 0, 0], [4, 2, 0, 0], [2, 4, 2, 0]], False)
    """
    "***YOUR CODE HERE***"

#I didn't have time to create test cases for questions below, so I've provided
#the codes below. Please understand the purpose of the functions below.
def up(game):
        print("up")
        # return matrix after shifting up
        game=transpose(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=transpose(game)
        return (game,done)

def down(game):
        print("down")
        game=reverse(transpose(game))
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=transpose(reverse(game))
        return (game,done)

def left(game):
        print("left")
        # return matrix after shifting left
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        return (game,done)

def right(game):
        print("right")
        # return matrix after shifting right
        game=reverse(game)
        game,done=cover_up(game)
        temp=merge(game)
        game=temp[0]
        done=done or temp[1]
        game=cover_up(game)[0]
        game=reverse(game)
        return (game,done)
