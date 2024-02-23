from vector import *

ROBOT_PATHS = {
  'center->blue': (
    Vector(0, 0),
    Vector(0, -10),
    Vector(-17, -52)
  )
}
# add reversed paths
ROBOT_PATHS['blue->center'] = ROBOT_PATHS['center->blue'][::-1]
# if the robot is within this many centimeters of a node, it's at the node
NODE_SIZE = 0.5