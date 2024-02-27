
import config_vars 
from argparse import ArgumentParser # won't be used in the robot

parser = ArgumentParser()
parser.add_argument('-q', '--quiet_logging', action='store_false')
parser.add_argument('-n', '--no_color', action='store_true')
args = parser.parse_args()

config_vars.VERBOSE_LOGGING = args.quiet_logging

# import the correct file based on whether we want color or not
if args.no_color:
    import robot_no_color as robot # change the namespace name so the same code still works
else:
    import robot

robot = robot.Robot(0, 0)
robot.follow_path('center->blue')