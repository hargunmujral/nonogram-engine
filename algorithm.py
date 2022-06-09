# Creating a nonogram solver

verticalBar1 = [[3], [2], [1, 2], [1], [4]]
horizontalBar1 = [[1], [3], [1, 1], [3, 1], [3]]
grid = [ ['O']*5 for i in range(5)]

# note that 'X' represents a filled cell, 'O' represents an empty cell and
# '-' represents a cell that cannot be filled


def quickSet(vertical: list, horizontal: list, grid: list):
    # these are the quick sets to be used in the algorithm

    # vertical quick set
    for idx, list in enumerate(vertical):
        if list == [3, 1]:
            grid[idx] = ['X', 'X', 'X', '-', 'X']
        elif list == [1, 3]:
            grid[idx] = ['X', '-', 'X', 'X', 'X']
        elif list == [4]:
            for i in range (1, 4):
                grid[idx][i] = 'X'
        elif list == [3]:
            grid[idx][2] = 'X'
        elif list == [1, 2]:
            grid[idx][3] = 'X'
        elif list == [2, 1]:
            grid[idx][1] = 'X'

    # horizontal quick set
    for idx, list in enumerate(horizontal):
        if list == [3, 1]:
            for i in range(0 ,5):
                if i == 3:
                    grid[i][idx] = '-'
                else:
                    grid[i][idx] = 'X'
        elif list == [1, 3]:
            for i in range(0 ,5):
                if i == 2:
                    grid[i][idx] = '-'
                else:
                    grid[i][idx] = 'X'
        elif list == [4]:
            for i in range(0 ,5):
                if i % 4 == 1:
                    grid[i][idx] = '-'
                else:
                    grid[i][idx] = 'X'
        elif list == [3]:
            grid[2][idx] = 'X'
        elif list == [1, 2]:
            grid[3][idx] = 'X'
        elif list == [2, 1]:
            grid[1][idx] = 'X'

            
quickSet(verticalBar1, horizontalBar1, grid)
print(grid)