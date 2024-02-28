
import config_vars 
from argparse import ArgumentParser # won't be used in the robot

parser = ArgumentParser()
parser.add_argument('-q', '--quiet_logging', action='store_false')
args = parser.parse_args()

config_vars.VERBOSE_LOGGING = args.quiet_logging

from robot import *

robot = Robot(
    config_vars.ROBOT_START_POSITION,
    config_vars.ROBOT_START_HEADING,
    config_vars.ROBOT_START_COLOR
)
robot.move_to_color('blue')