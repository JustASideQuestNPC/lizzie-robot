from vector import *
from config_vars import *

ROBOT_PATHS = {
    'center->blue': [
        Vector(0, 0),
        Vector(0, -10),
        Vector(-17, -52)
    ]
}

# add reversed paths
if VERBOSE_LOGGING:
    print('Generating reversed paths...', end = '')
# adding to a dictionary while looping through it crashes the program, so we copy all the forward
# paths to their own dictionary and loop through that instead
forward_paths = ROBOT_PATHS.copy()
for name, nodes in forward_paths.items():
    # path names are formatted as '{start color}->{end color}', so we can split them at the arrow to
    # get the start and end color on their own (split() returns a list we can unpack)
    start, end = name.split('->')

    # reverse the path manually because SPIKE python only supports slices with a step of 1
    reversed = []
    for i in range(len(nodes)):
        reversed.append(nodes[len(nodes) - 1 - i])

    ROBOT_PATHS[end + '->' + start] = reversed
if VERBOSE_LOGGING:
    print('done\n')