# Implementing 2048-game logics
import random


def start_game():
    mat = []
    for i in range(4):
        mat.append([0]*4)
    return mat

def adding_2_randomly(mat):
    # we will get a random number from 0 to 3, both are included
    row = random.randint(0,3)
    col = random.randint(0,3)
    while (mat[row][col] != 0):
        row = random.randint(0,3)
        col = random.randint(0,3)
    mat[row][col] = 2
    return mat

def current_state(mat):
    # 'WIN' case
    # Anywhere 2048 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 2048:
                return 'WON'

    # 'Not Over' case
    # Anywhere 0 is present
    for i in range(4):
        for j in range(4):
            if mat[i][j] == 0:
                return 'Game Not Over'

    # Every Row and Column except the last row and last column
    for i in range(3):
        for j in range(3):
            if (mat[i][j] == mat[i][j+1]) or (mat[i][j] == mat[i+1][j]):
                return 'Game Not Over'

    # Last row and last column
    for i in range(3):
        if (mat[3][i] == mat[3][i+1]) or (mat[i][3] == mat[i+1][3]):
            return 'Game Not Over'

    return 'LOST'

# compress the matrix
# make all the values/non-empty one side and all the zeros/empty cells on one side, so that it will be easy for merging them.
def compress(mat):
    changed = False
    new_mat = []
    for i in range(4):
        new_mat.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if mat[i][j] != 0:
                new_mat[i][pos] = mat[i][j]
                if pos != j:
                    changed = True
                pos += 1
    return new_mat,changed

# merge function merges the 2 values if they are equal.
def merge(mat):
    changed = False
    for i in range(4):
        for j in range(3):
            if mat[i][j] == mat[i][j+1] and mat[i][j] != 0:
                mat[i][j] = mat[i][j] * 2
                mat[i][j+1] = 0
                changed = True
    return mat,changed

# making elements in each row reverse that is, [1,2,3,4] to [4,3,2,1]
def reverse(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[i][4-j-1])
    return  new_mat

# making a transpose of a matrix that is, changing row to column and column to row
# ex: [[1,2,3],[4,5,6],[7,8,9]] to [[1,4,7],[2,5,8],[3,6,9]]
def transpose(mat):
    new_mat = []
    for i in range(4):
        new_mat.append([])
        for j in range(4):
            new_mat[i].append(mat[j][i])
    return new_mat

# a function to make a move upwards
def move_up(mat):
    new_mat = transpose(mat)
    new_mat,changed1 = compress(new_mat)
    new_mat,changed2 = merge(new_mat)
    changed = changed1 or changed2
    new_mat,temp = compress(new_mat)
    final_mat = transpose(new_mat)
    return final_mat,changed

# function to move down
def move_down(mat):
    new_mat = transpose(mat)
    new_rev_mat = reverse(new_mat)
    new_mat,changed1 = compress(new_rev_mat)
    new_mat,changed2 = merge(new_mat)
    changed = changed1 or changed2
    new_mat,temp = compress(new_mat)
    final_rev_mat = reverse(new_mat)
    final_mat = transpose(final_rev_mat)
    return final_mat,changed

# function to move right
def move_right(mat):
    new_mat = reverse(mat)
    new_mat,changed1 = compress(new_mat)
    new_mat,changed2 = merge(new_mat)
    changed = changed1 or changed2
    new_mat,temp = compress(new_mat)
    final_mat = reverse(new_mat)
    return final_mat,changed

# function to move left
def move_left(mat):
    new_mat,changed1 = compress(mat)
    new_mat,changed2 = merge(new_mat)
    changed = changed1 or changed2
    final_mat,temp = compress(new_mat)
    return final_mat,changed






