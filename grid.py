# grid of blocked/unblocked cells - ' ' is an unblocked cell, and '#' is a blocked cell
CELL_GRID = (
  '###     ##',
  '###     ##',
  '##  #     ',
  '##        ',
  '# ##  ##  ',
  '  ##      ',
  '          ',
  '   #  # # ',
  ' # #  #   ',
  '          ',
  '#  ####   ',
  '# ######  ',
  '  ######  ',
  '  ######  ',
  '  ###### #',
)
GRID_WIDTH = len(CELL_GRID[0])
GRID_HEIGHT = len(CELL_GRID)

# returns whether a certain grid cell is open
def cell_is_open(x: int, y: int) -> bool:
  # cells that are outside are considered blocked
  if x < 0 or x >= GRID_WIDTH or y < 0 or y > GRID_HEIGHT:
    return False
  # x and y need to be flipped because of how list indexing works
  return CELL_GRID[y][x] == ' '