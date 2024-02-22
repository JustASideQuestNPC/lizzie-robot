import display_backend

GRID_CELL_SIZE = 10 # cm, probably

# placeholders for the motor functions
def move_forward(distance: int) -> None:
  print(f'Moving forward {distance * GRID_CELL_SIZE} cm')

def rotate(angle: int) -> None:
  print(f'Rotating {angle} degrees')

class Robot:
  def __init__(self, x: int, y: int) -> None:
    self.x = x
    self.y = y
    self.direction = 'north'

    # update display backend
    display_backend.robot_display_pos = (self.x, self.y)

    self.angles = {
      'north': {
        'north': 0,
        'south': 180,
        'west': 90,
        'east': -90,
        'x': 0,
        'y': -1
      },
      'south': {
        'north': 180,
        'south': 0,
        'west': -90,
        'east': 90,
        'x': 0,
        'y': 1
      },
      'west': {
        'north': -90,
        'south': 90,
        'west': 0,
        'east': 180,
        'x': -1,
        'y': 0
      },
      'east': {
        'north': 90,
        'south': -90,
        'west': 180,
        'east': 0,
        'x': 1,
        'y': 0
      },
    }

  async def move(self, direction: str, distance: int=1) -> None:
    rotate(self.angles[direction][self.direction])
    self.x += self.angles[direction]['x']
    self.y += self.angles[direction]['y']
    move_forward(distance * GRID_CELL_SIZE)
    self.direction = direction

    # update display backend
    display_backend.robot_display_pos = (self.x, self.y)
    
