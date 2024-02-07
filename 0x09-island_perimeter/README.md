Island Perimeter
Task Description
Create a function island_perimeter(grid) that calculates and returns the perimeter of the island described in the given grid.

Function Signature
python
Copy code
def island_perimeter(grid):
    """
    Calculate and return the perimeter of the island described in the grid.

    Parameters:
        grid (List[List[int]]): A list of lists of integers representing the island grid.

    Returns:
        int: The perimeter of the island.
    """
    # Function implementation goes here
Constraints
grid is a list of list of integers.
Each cell in the grid is square, with a side length of 1.
Cells are connected horizontally/vertically (not diagonally).
The grid is rectangular, with its width and height not exceeding 100.
The grid is completely surrounded by water.
There is only one island (or nothing).
The island doesn’t have “lakes” (water inside that isn’t connected to the water surrounding the island).
Input
The grid parameter is a 2D list of integers where:

0 represents water.
1 represents land.
Output
The function should return an integer representing the perimeter of the island.

Implementation Guidelines
The function should calculate the perimeter of the island based on the specified rules.
Use PEP 8 style for the code.
Ensure that the code is well-documented, including function and module-level documentation.
The first line of the script should be #!/usr/bin/python3.
All files should end with a new line.
The README.md file at the root of the project should provide additional information, usage instructions, and any other relevant details about the project.
Importing any module is not allowed.
All modules and functions must be documented.
All files must be executable.
Note: The detailed implementation of the function is not provided in this description, as it is expected to be filled in the code file according to the specified requirements.
