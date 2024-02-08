#!/usr/bin/python3
'''
island_perimeter(grid): returns the perimeter of the island
described in the grid.
'''


def island_perimeter(grid):
    ''' returns the perimeter of the island'''
    perimeter = 0
    column = len(grid)
    row = len(grid[0])
    assert (1 <= row and column <= 100), "length must be between 1 an 100"
    for i in range(column):
        for j in range(row):
            assert (grid[i][j] == 0) or (grid[i][j] == 1),\
                "grid numbers must be 0 or 1"
            if (grid[i][j] == 1):
                perimeter += 4
                if grid[i][j-1] == 1:
                    perimeter -= 2
                if grid[i-1][j] == 1:
                    perimeter -= 2
            else:
                pass
    return perimeter
