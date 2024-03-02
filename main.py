
import config_vars 
import asyncio
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('-q', '--quiet_logging', action='store_false')
args = parser.parse_args()

config_vars.VERBOSE_LOGGING = args.quiet_logging

from robot import *

async def main() -> None:
    robot = Robot(
        config_vars.ROBOT_START_POSITION,
        config_vars.ROBOT_START_HEADING,
        config_vars.ROBOT_START_COLOR
    )

    await robot.move_to_color('blue')

asyncio.run(main())