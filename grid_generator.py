IMAGE_PATH = 'grid images/maze-01.png'
GRID_WIDTH = 16
GRID_HEIGHT = 16
# if at least this fraction of a block's pixels are black, the cell is blocked (i.e., a threshold of
# 0.5 means that any cells where at least half of the pixels are black are blocked)
BLOCKED_THRESHOLD = 0.5

# set to False if your terminal is printing weird characters at the start and end of lines
COLOR_PRINT_ENABLED = True


from math import floor
import sys # for exiting without throwing messy errors

def color_print(text: str, color: str) -> None:
  if COLOR_PRINT_ENABLED:
    # ansi codes have been around since the 70s and will make *almost* any terminal print in color
    code = 39
    if color == 'red':
      code = 31
    elif color == 'green':
      code = 32
    elif color == 'blue':
      code = 36
    print(f'\x1b[{code}m{text}\x1b[39m')

try:
  from PIL import Image
except ImportError:
  color_print(("Pillow is not installed (or could not be found)!\nRun 'pip install pillow' in the "
               "terminal to install it."), 'red')
  sys.exit()

print('Loading source image...', end='')
with Image.open(IMAGE_PATH) as image:
  color_print('done', 'green')
  if GRID_WIDTH > image.width or GRID_HEIGHT > image.height:
    color_print((f'The grid cannot be larger than the source image! (Grid was {GRID_WIDTH}x'
                 f'{GRID_HEIGHT}, image was {image.width}x{image.height})'), 'red')
    
  block_width = floor(image.width / GRID_WIDTH)
  block_height = floor(image.height / GRID_HEIGHT)

  color_print((f'Grid size is {GRID_WIDTH}x{GRID_HEIGHT}\n'
               f'Image size is {image.width}x{image.height}\n'
               f'Block size is {block_width}x{block_height}'), 'blue')

  grid = []
  closed_cells = 0
  open_cells = 0
  for y in range(GRID_HEIGHT):
    row = ''
    for x in range(GRID_WIDTH):
      block = image.crop((
        x * block_width,
        y * block_height,
        x * block_width  + block_width,
        y * block_height+ block_height
      ))

      black_pixels = 0
      total_pixels = 0
      for py in range(block.height):
        for px in range(block.width):
          total_pixels += 1
          if block.getpixel((px, py)) == (0, 0, 0):
            black_pixels += 1

      if black_pixels / total_pixels >= BLOCKED_THRESHOLD:
        row += '#'
        closed_cells += 1
      else:
        row += ' '
        open_cells += 1

    grid.append(row)
  
  color_print('Grid created successfully', 'green')
  print((f'Total cells: {open_cells + closed_cells}\n'
         f'Open cells: {open_cells}\n'
         f'Closed cells: {closed_cells}'))

  color_print(f'--- START OF CODE BLOCK ---', 'green')
  # print a formatted grid
  print((f'GRID_WIDTH = {GRID_WIDTH}\n'
         f'GRID_HEIGHT = {GRID_HEIGHT}\n'
          'CELL_GRID = ('))
  for i, row in enumerate(grid):
    print(f"    '{row}'{',' if i < len(grid) - 1 else ''}")
  print(')')
  color_print(f'--- END OF CODE BLOCK ---', 'green')