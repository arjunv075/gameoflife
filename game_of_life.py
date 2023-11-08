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
