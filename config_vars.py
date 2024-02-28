from math import sqrt, atan2, degrees, cos, sin, radians

''' --- Global Config Vars --- '''
VERBOSE_LOGGING      = True     # if True, prints out waaay more data while running
NODE_SIZE            = 0.5      # if the robot is within this many cm of a node, it's at the node
ROBOT_START_POSITION = (0, 0)   # centimeters; (0, 0) is the center
ROBOT_START_HEADING  = 0        # degrees
ROBOT_START_COLOR    = 'center' # 'center', 'red', 'green', 'yellow', or 'blue'
DRIVE_MOTOR_SPEED    = 540      # degrees per second
CARGO_MOTOR_SPEED    = 360      # degrees per second
LEFT_WHEEL_PORT      = 'port.W'
RIGHT_WHEEL_PORT     = 'port.X'
CARGO_MOTOR_PORT     = 'port.Y'
COLOR_SENSOR_PORT    = 'port.Z'
DRIVE_WHEELS         = 'motor pair A'