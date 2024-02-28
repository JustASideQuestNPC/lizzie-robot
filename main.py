
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

    for i in range(4):
        cargo_color = robot.get_cargo_color()
        await robot.move_to_color(cargo_color)
        await robot.release_cargo()

asyncio.run(main())