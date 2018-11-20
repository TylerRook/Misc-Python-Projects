"""
Tyler Rook

Description: A program for checking a basic matrix equality.
"""

def getMatrix_3x3(string):
    """
    Takes a string and returns a 3x3 2d list
    """
    
    matrix = [[], [], []]
    l=list(map(int, string.split()))

    for value in range(9):
    # This splits the values in the list up according to
    # which row they should be in.
        if value <= 2:
            matrix[0].append(l[value])
        elif value <= 5:
            matrix[1].append(l[value])
        elif value <= 8:
            matrix[2].append(l[value])
    
    return matrix

def check_equals15(matrix):
    """
    Checks to see if rows, columns, and diagonals of a 2d list equal 15
    """

    for row in matrix:
    # This checks whether or not the sum of the elements
    # in each row equal 15.
        t_row=0
        for item in row:
            t_row += item
        if t_row != 15:
            return False
        
    for column in range(3):
    # This checks whether or not the sum of the elements
    # in each column equal 15.
        t_column = 0
        for row in matrix:
            t_column += row[column]
        if t_column != 15:
            return False
        
    t_slantForward = 0
    t_slantBackward = 0
    backwardCount = 0
    forwardCount = 2
    
    for row in matrix:
    # This checks whether or not the sum of the elements
    # in both diagonal lines equal 15.
        t_slantForward += row[forwardCount]
        forwardCount -= 1
        t_slantBackward += row[backwardCount]
        backwardCount += 1
    if t_slantBackward != 15:
        return False
    elif t_slantForward != 15:
        return False
    else: return True

def check_numDifferent(string):
    """
    Examines if a string of integers has no repeating numbers within 1-9
    """

    numbers = list(map(int, string.split()))
    for number in range(len(numbers)):
        # This makes sure all the numbers are in the domain.
        if numbers[number] > 9 or numbers[number] < 1:
            return False
        #This makes sure that there are no repeating numbers.
        for otherNumber in range(len(numbers)):
            if numbers[number] == numbers[otherNumber] and \
               number != otherNumber:
                return False
    return True
    
def main():
    f=open("input.txt", "r")
    for line in f:
        matrix = getMatrix_3x3(line)
        if check_numDifferent(line) and check_equals15(matrix):
            print ('valid')
        else:
            print ('invalid')

main()
