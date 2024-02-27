from math import sqrt, atan2, degrees, cos, sin, radians

''' --- Global Config Vars --- '''
VERBOSE_LOGGING   = True # if True, prints out waaay more data while running
NODE_SIZE         = 0.5 # if the robot is within this many centimeters of a node, it's at the node
LEFT_WHEEL_PORT   = 'port.W'
RIGHT_WHEEL_PORT  = 'port.X'
CARGO_MOTOR_PORT  = 'port.Y'
COLOR_SENSOR_PORT = 'port.Z'
DRIVE_WHEELS      = 'motor pair A'