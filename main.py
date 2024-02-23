import robot
from color_print import color_print
from argparse import ArgumentParser # won't be used in the robot

parser = ArgumentParser()
parser.add_argument('-q', '--quiet_logging', action='store_false')
args = parser.parse_args()

robot.VERBOSE_LOGGING = args.quiet_logging

robot = robot.Robot(0, 0)
robot.follow_path('center->blue')