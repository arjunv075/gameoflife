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

def next_generation(current_grid):
    rows, cols = len(current_grid), len(current_grid[0])
    new_grid = copy.deepcopy(current_grid)

    for x in range(rows):
        for y in range(cols):
            cell = current_grid[x][y]
            neighbours = count_neighbours(current_grid, x, y)

            if cell == 1:
                if neighbours < 2 or neighbours > 3:
                    new_grid[x][y] = 0
            else:
                if neighbours == 3:
                    new_grid[x][y] = 1

    return new_grid

def main(rows, cols, generations):
    grid = create_grid(rows, cols)
    print_grid(grid)

    for generation in range(generations):
        time.sleep(0.2)
        grid = next_generation(grid)
        print("\033c")
        print_grid(grid)

if __name__ == "__main__":
    rows = 20 
    cols = 20  
    generations = 10  
    main(rows, cols, generations)