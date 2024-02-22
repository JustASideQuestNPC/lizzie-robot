import display_backend
from robot import *

''' --- robot code starts here --- '''
# import motor
# import other stuff

# constants
MOTOR_SPEED = 720 # degrees per second

# motor ports
LEFT_WHEEL = 'port.A'
RIGHT_WHEEL = 'port.B'

moves = (
  'north',
  'north',
  'east',
  'west',
  'north',
  'south',
  'west'
)

robot = Robot(5, 5)
# not async because async functions require extra backend code on my end
# it's the same code otherwise
# for backend reasons, this returns True if it should continue running on the
# next frame
async def main() -> bool:
  # pair left and right wheels to motor pair 1
  
  for move in moves:
    await robot.move(move)

  return False # for backend stuff
  

# run the window loop using our main function; this shouldn't be part of the robot code
display_backend.run_loop(main)