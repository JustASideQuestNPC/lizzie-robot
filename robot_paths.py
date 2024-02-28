from vector import *
from config_vars import *

''' --- Path Nodes --- '''
ROBOT_PATHS = {
    'center->blue': [
        (  0,   0),
        (  0, -18),
        ( 38, -18),
        ( 38, -32),
        ( 38, -47),
        ( 12, -67),
        (-17, -67),
        (-17, -52)
    ],
    'center->green': [
        (  0,   0),
        (  0, -18),
        (-27, -12),
        (-27,   7),
        (-40,  23)
    ],
    'center->red': [
        (  0,   0),
        (  0,  14),
        ( 31,  30),
        ( 41,  46)
    ],
    'center->yellow': [
        (  0,   0),
        (  0, -18),
        ( 38, -18),
        ( 38, -32)
    ],
    'yellow->blue': [
        ( 38, -32),
        ( 38, -47),
        ( 12, -67),
        (-17, -67),
        (-17, -52)
    ],
    'yellow->red': [
        ( 38, -32),
        ( 42, -16),
        ( 41, -46)
    ]
}

# convert coordinate pairs to vectors and add reversed paths
if VERBOSE_LOGGING:
    print('Generating path vectors...', end = '')
# adding to a dictionary while looping through it crashes the program, so we copy all the forward
# paths to their own dictionary and loop through that instead
forward_paths = ROBOT_PATHS.copy()
for name, nodes in forward_paths.items():
    # path names are formatted as '{start color}->{end color}', so we can split them at the arrow to
    # get the start and end color on their own (split() returns a list we can unpack)
    start, end = name.split('->')

    # create vectors
    path_vectors = []
    for i, node in enumerate(nodes):
        path_vectors.append(Vector(node))

    ROBOT_PATHS[name] = path_vectors;
    ROBOT_PATHS[end + '->' + start] = [path_vectors[len(path_vectors) - 1 - i].copy() for i in range(len(path_vectors))]

if VERBOSE_LOGGING:
    print('done\n')