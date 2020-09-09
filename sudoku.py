import time

#We establish the set of possible values for each cell in the puzzle
subtract_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

#We check the row for possible values
def check_horizontal(i, j):
    return subtract_set - set(container[i])

#We check the column for possible values
def check_vertical(i, j):
    ret_set = []
    #We gather the cells in the column
    for x in range(9):
        ret_set.append(container[x][j])
    return subtract_set - set(ret_set)

#We check the square for possible values
def check_square(i, j):
    first = [0, 1, 2]
    second = [3, 4, 5]
    third = [6, 7, 8]
    find_square = [first, second, third]
    #We find the cooridnates of the cells in the respective square
    for l in find_square:
        if i in l:
            row = l
        if j in l:
            col = l
    return_set = []
    #We gather the cells in the entire square
    for x in row:
        for y in col:
            return_set.append(container[x][y])
    return subtract_set - set(return_set)

#We compute the final set of possible values for an empty cell
def get_poss_vals(i, j):
    poss_vals = list(check_square(i, j) \
                     .intersection(check_horizontal(i, j)) \
                     .intersection(check_vertical(i, j)))
    return poss_vals

#The explicit solver iterates through every square and fills up empty cells where possible
def explicit_solver(container):
    #The stump count checks if the explicit solver fills any empty cells
    stump_count = 1
    for i in range(9):
        for j in range(9):
            if container[i][j] == 0:
                poss_vals = get_poss_vals(i, j)
                #The cell is filled in only when there is one possible value
                if len(poss_vals) == 1:
                    container[i][j] = list(poss_vals)[0]
                    stump_count = 0
    return container, stump_count

#The implicit solver considers the possible values of the rest of the row/column/square
#We then subtract this from the complete list of possible values to fill in cells left empty by the explicit solver
def implicit_solver(i, j, container):
    if container[i][j] == 0:
        poss_vals = get_poss_vals(i, j)

        #We check the row for possible values
        row_poss = []
        for y in range(9):
            if y == j:
                continue
            if container[i][y] == 0:
                for val in get_poss_vals(i, y):
                    row_poss.append(val)
        if len(set(poss_vals) - set(row_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(row_poss))[0]

        #We check the column for possible values
        col_poss = []
        for x in range(9):
            if x == i:
                continue
            if container[x][j] == 0:
                for val in get_poss_vals(x, j):
                    col_poss.append(val)
        if len(set(poss_vals) - set(col_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(col_poss))[0]

        #We check the square for possible values
        first = [0, 1, 2]
        second = [3, 4, 5]
        third = [6, 7, 8]
        find_square = [first, second, third]
        for l in find_square:
            if i in l:
                row = l
            if j in l:
                col = l
        square_poss = []
        for x in row:
            for y in col:
                if container[x][y] == 0:
                    for val in get_poss_vals(x, y):
                        square_poss.append(val)
        if len(set(poss_vals) - set(square_poss)) == 1:
            container[i][j] = list(set(poss_vals) - set(square_poss))[0]
    return container

#Main code

#We input sudoku puzzle as a list of lists
container = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
             [5, 2, 0, 0, 0, 0, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 3, 1],
             [0, 0, 3, 0, 1, 0, 0, 8, 0],
             [9, 0, 0, 8, 6, 3, 0, 0, 5],
             [0, 5, 0, 0, 9, 0, 6, 0, 0],
             [1, 3, 0, 0, 0, 0, 2, 5, 0],
             [0, 0, 0, 0, 0, 0, 0, 7, 4],
             [0, 0, 5, 2, 0, 6, 3, 0, 0]]

#We register the time at which we begin our computation
start = time.time()
zero_count = 0
#We count the number of zeroes in the input sudoku puzzle
for l in container:
    for v in l:
        if v == 0:
            zero_count += 1

#We display the number of cells that we need to fill in
print(f'There are {zero_count} moves I have to make!')
print()

solving = True

while solving:
    #Solver portion
    container, stump_count = explicit_solver(container)

    #Loop breaking portion
    zero_count = 0
    for l in container:
        for v in l:
            if v == 0:
                zero_count += 1
    #If there are no more zeroes in the container, the puzzle is solved
    if zero_count == 0:
        print(container)
        solving = False
    #If the explicit solver does not make any moves, we call the implicit solver
    if stump_count > 0:
        for i in range(9):
            for j in range(9):
                container = implicit_solver(i, j, container)

#The sudoku puzzle is now solved
print(container)
print('That took', time.time() - start, 'seconds!')


#***END OF CODE***