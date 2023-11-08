import random
import time
import copy

def create_grid(rows, cols):
    grid = []
    for _ in range(rows):
        row = [random.randint(0, 1) for _ in range(cols)]
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(["." if cell else " " for cell in row]))

def count_neighbours(grid, x, y):
    rows, cols = len(grid), len(grid[0])
    neighbours = [(x-1, y-1), (x-1, y), (x-1, y+1),
                (x, y-1),               (x, y+1),
                (x+1, y-1), (x+1, y), (x+1, y+1)]
    
    count = 0
    for x, y in neighbours:
        if 0 <= x < rows and 0 <= y < cols and grid[x][y] == 1:
            count += 1
    return count
