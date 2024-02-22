''' --- BACKEND STUFF --- '''
from grid import CELL_GRID
# import and setup pygame
import pygame

# display constants
TARGET_FRAME_RATE = 60 # frames per second
GRID_CELL_SIZE = 50 # pixels
WINDOW_WIDTH = len(CELL_GRID[1]) * GRID_CELL_SIZE # pixels
WINDOW_HEIGHT = len(CELL_GRID) * GRID_CELL_SIZE # pixels

# colors
BLACK = '#282A36'
DARK_GRAY = '#44475A'
WHITE = '#FFFFFF'
LIGHT_GRAY = '#6272A4'
CYAN = '#8BE9FD'
GREEN = '#50FA7B'
ORANGE = '#FFB86C'
PINK = '#FF79C6'
PURPLE = '#BD93F9'
RED = '#FF5555'
YELLOW = '#F1FA8C'

robot_display_pos = (4, 0)
cargo_display_pos = (6, 9)
target_display_pos = (9, 2)

loop_paused = False
# used for loop pausing
UNPAUSE_LOOP = pygame.event.custom_type()

def run_loop(loop_function: callable) -> None:
  # make loop paused accessible outside
  global loop_paused

  # start pygame and create a window
  pygame.init()
  screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT)) # create a window
  clock = pygame.time.Clock()
  window_running = True
  loop_function_running = True

  # opens a window and runs the actual code
  while window_running:
    # poll for events and quit if the window was closed
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        window_running = False
      elif event.type == UNPAUSE_LOOP:
        loop_paused = False
        
    # clear everything drawn on the previous frame
    screen.fill(BLACK)
    # loop through the cell grid and draw occupied cells
    y = 0
    for row in CELL_GRID:
      x = 0
      for cell in row:
        if cell == '#':
          pygame.draw.rect(screen, PINK, pygame.Rect(x, y, GRID_CELL_SIZE, GRID_CELL_SIZE))

        x += GRID_CELL_SIZE
      y += GRID_CELL_SIZE

    # run the robot code
    if (loop_function_running and not loop_paused):
      loop_function_running = loop_function()

    # draw the robot's position
    pygame.draw.rect(
      screen,
      GREEN,
      pygame.Rect(
        robot_display_pos[0] * GRID_CELL_SIZE + 10,
        robot_display_pos[1] * GRID_CELL_SIZE + 10,
        GRID_CELL_SIZE - 20,
        GRID_CELL_SIZE - 20)
    )

    # draw the cargo's position
    pygame.draw.rect(
      screen,
      CYAN,
      pygame.Rect(
        cargo_display_pos[0] * GRID_CELL_SIZE + 10,
        cargo_display_pos[1] * GRID_CELL_SIZE + 10,
        GRID_CELL_SIZE - 20,
        GRID_CELL_SIZE - 20)
    )

    # draw the target's position
    pygame.draw.rect(
      screen,
      ORANGE,
      pygame.Rect(
        target_display_pos[0] * GRID_CELL_SIZE + 10,
        target_display_pos[1] * GRID_CELL_SIZE + 10,
        GRID_CELL_SIZE - 20,
        GRID_CELL_SIZE - 20)
    )

    pygame.display.flip() # display everything drawn on this frame
    clock.tick(TARGET_FRAME_RATE) # limit frame rate to the target

    
  # close the window for real
  pygame.quit()
