#!/usr/bin/env python3
'''
island_perimeter(grid): returns the perimeter of the island 
described in the grid.
'''

def island_perimeter(grid):
    ''' returns the perimeter of the island'''
    perimeter = 0
    height = len(grid)
    width = len(grid[0])
    for i in range(height):
        for j in range(width):
            if (grid[i][j] == 1):
                perimeter += 4
                if grid[i][j-1] == 1:
                    perimeter -= 2
                if grid[-i][j] == 1:
                    perimeter -= 2
            else:
                pass
    return perimeter
