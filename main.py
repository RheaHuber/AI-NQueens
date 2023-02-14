# Constrained N-Queens Solver
# Reads input file input.csv which contains a square table with the location of one queen
# Returns a table with N number of un-threatened queens or prints "no solution"
# where N is the number of rows in the original table

# Load input data
inputData = open("input.csv", "rt")

# Goal number of queens and board dimensions
N = 0
# Stacks of queen positions (to find most recently added queens)
stackSize = 0
queenRows = []
queenColumns = []
# Arrays of queen positions (to find queen positions quickly)
fullRows = []
fullCols = []

# Find N and first queen
row = 0
column = 0
for line in inputData:
    for x in line:
        if x == ',':
            column += 1
        elif x == '1':
            queenRows.append(row)
            queenColumns.append(column)
            stackSize += 1
    N += 1
    row += 1
    column = 0

# Close input file
inputData.close()

# Fill queen arrays
for x in range(N):
    fullRows.append(-1)
    fullCols.append(-1)
fullRows[queenRows[0]] = queenColumns[0]
fullCols[queenColumns[0]] = queenRows[0]

# Define diagonal checker function
# Returns 1 if a collision is found, 0 otherwise
def checkDiagonalCollision():
    # Check down-right diagonal
    R = row + 1
    C = column + 1
    while R < N and C < N:
        if fullRows[R] == C:
            return 1
        R += 1
        C += 1
    # Check down-left diagonal
    R = row + 1
    C = column - 1
    while R < N and C > -1:
        if fullRows[R] == C:
            return 1
        R += 1
        C -= 1
    # Check up-right diagonal
    R = row - 1
    C = column + 1
    while R > -1 and C < N:
        if fullRows[R] == C:
            return 1
        R -= 1
        C += 1
    # Check up-left diagonal
    R = row - 1
    C = column - 1
    while R > -1 and C > -1:
        if fullRows[R] == C:
            return 1
        R -= 1
        C -= 1
    # All diagonals clear
    return 0


# Main backtracking loop
# Loop through each empty row
row = 0
column = 0
while row < N:
    # If row is unoccupied, proceed
    if fullRows[row] == -1:
        # Loop through each empty position in this row
        while column < N:
            # If position is unoccupied, proceed
            if fullCols[column] == -1:
                # Check diagonals
                if checkDiagonalCollision() == 0:
                    # Valid queen position found, record position and push onto stacks
                    fullRows[row] = column
                    fullCols[column] = row
                    queenRows.append(row)
                    queenColumns.append(column)
                    stackSize += 1
                    break
            # No valid position in row
            if column == (N - 1):
                while column == (N - 1):
                    # No queens removable from the stack
                    if stackSize == 1:
                        print("No solution")
                        exit(0)
                    # Pop previous queen off the stack and return to that position
                    row = queenRows.pop()
                    column = queenColumns.pop()
                    stackSize -= 1
                    fullRows[row] = -1
                    fullCols[column] = -1
                    # If previous queen was at the end of its row, repeat
            column += 1
    row += 1
    column = 0

# Print out solution
outputData = open("solution.csv", "w")
row = 0
for row in range(N):
    for column in range(N):
        if fullRows[row] == column:
            outputData.write("1")
        else:
            outputData.write("0")
        if column < (N - 1):
            outputData.write(",")
    outputData.write("\n")

# Close the output file
outputData.close()
