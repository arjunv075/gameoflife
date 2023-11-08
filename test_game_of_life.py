import game_of_life

def test_create_grid():
    rows = 5
    cols = 5
    grid = game_of_life.create_grid(rows, cols)
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
