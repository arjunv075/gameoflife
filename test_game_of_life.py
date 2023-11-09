import game_of_life

def test_create_random_grid():
    rows = 5
    cols = 5
    grid = game_of_life.create_random_grid(rows, cols)
    assert len(grid) == rows
    for row in grid:
        assert len(row) == cols

def test_print_grid(capsys):
    grid = [
        [True, False, True],
        [False, True, False],
        [True, True, True]
    ]
    expected_output = ".   .\n  .  \n. . .\n"
    game_of_life.print_grid(grid)
    captured = capsys.readouterr()
    assert captured.out == expected_output

def test_count_neighbours():
    grid = [[1, 0, 1],
            [0, 1, 0],
            [1, 1, 1]]
    x, y = 1, 1
    count = game_of_life.count_neighbours(grid, x, y)
    assert count == 5

def test_next_generation():
    current_grid = [[1, 0, 1],
                    [0, 1, 0],
                    [1, 1, 1]]
    expected_grid = [[0, 1, 0],
                     [0, 0, 0],
                     [1, 1, 1]]
    new_grid = game_of_life.next_generation(current_grid)
    assert new_grid == expected_grid
