import game_of_life

def test_create_grid():
    rows = 5
    cols = 5
    grid = game_of_life.create_grid(rows, cols)
    assert len(grid) == rows
    for row in grid:
        assert len(row) == cols