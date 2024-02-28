# version of the robot class without any color_print calls
from vector import *
from robot_paths import *
from config_vars import *
from random import shuffle

# dummy colors for testing control flow
cargo_colors = ['red', 'green', 'blue', 'yellow']
color_index = 0
shuffle(cargo_colors)

''' --- Main Robot Class --- '''
class Robot:
    def __init__(self, position: tuple[float, float], heading: float, color: str):
        self.position = Vector(position)
        self.heading = heading
        self.current_color = color # what color (or the center) we're currently at

    def at_node(self, node: Vector) -> bool:
        delta = node - self.position
        return delta.mag() < NODE_SIZE
    
    async def turn_to_angle(self, angle: int) -> None:
        delta = angle - self.heading
        # motor code here
        self.heading = angle

    async def move_forward(self, motor_degrees: int) -> None:
        # motor code here
        pass # keeps python happy; remove this when you add motor code

    async def release_cargo(self) -> None:
        print('Releasing cargo...', end='')
        # motor code here
        print('done')

    def get_cargo_color(self) -> str:
        if False: # check if the color sensor is recieving too little light here
            raise RuntimeError('Cannot detect cargo color!')
        # replace this with a color sensor check
        global cargo_colors
        global color_index
        color = cargo_colors[color_index]
        color_index += 1
        return color

    # follows a node path; raises an error if the color is unreachable
    async def move_to_color(self, target_color=str) -> None:
        path_name = self.current_color + '->' + target_color
        # if a direct path doesn't exist, try to work around it
        if path_name not in ROBOT_PATHS:
            # if the target is the center or we're at the center, give up and crash
            if self.current_color == 'center' or target_color == 'center':
                raise RuntimeError("Target color '{tc}' is unreachable from this position ({cc})!"
                      .format(tc = target_color, cc=self.current_color))
            # otherwise, try to reach it via the center
            else:
                print((
                    "No direct path exists from current position ({cc}) to target position '{tc}'; "
                    'attempting to reach it via the center.')
                    .format(cc = self.current_color, tc = target_color)
                )
                # catch the status codes from the two move calls and only return them if they failed
                await self.move_to_color('center')
                await self.move_to_color(target_color)
                return

        # normally we'd use f strings, but SPIKE python uses an older version of python that doesn't
        # support them 
        print("Moving along path '{pn}'".format(pn = path_name))
        path = ROBOT_PATHS[path_name]

        for i, node in enumerate(path):
            if VERBOSE_LOGGING:
                print((
                    '--- Moving to node {i} ---\n'
                    'Node position: {n}\n'
                    'Current position: {p}')
                    .format(i = i, n = node, p = self.position)
                )

            if self.at_node(node):
                if VERBOSE_LOGGING:
                    print('Already at node!\n')
                else:
                    print('Already at node {i}'.format(i = i))
                continue # end this iteration of the loop and go straight to the next node

            delta = node - self.position

            # the magnitude will be a float and the motor control functions only take ints, so
            # we'll round to get as close as we can
            mag_cm_raw = delta.mag()
            mag_degrees_raw = mag_cm_raw * 23 # convert to degrees for maximum precision

            mag_degrees_adjusted = round(mag_degrees_raw)
            mag_cm_adjusted = mag_degrees_adjusted / 23

            # adjust the heading
            heading_raw = delta.heading()
            heading_adjusted = round(heading_raw)

            
            position_offset = vec_from_polar(mag_cm_adjusted, heading_adjusted)

            if VERBOSE_LOGGING:
                mag_degrees_error = abs(mag_degrees_raw - mag_degrees_adjusted)
                mag_cm_error = mag_degrees_error / 23
                heading_error = abs(heading_raw - heading_adjusted)
                print((
                    'Delta vector: {d}\n\n'
                    'Raw length: {v0}° ({v1} cm)\n'
                    'Adjusted length: {mda}° ({v2} cm)\n'
                    'Length error: {v3}° ({v4} cm)\n'
                    'Raw heading: {v5}°\n'
                    'Adjusted heading: {ha}°\n'
                    'Heading error: {v6}°\n'
                    'Adjusted vector: {po}\n')
                    .format(d = delta, v0 = round(mag_degrees_raw, 3), v1 = round(mag_cm_raw, 3),
                            mda = mag_degrees_adjusted, v2 = round(mag_cm_adjusted, 3),
                            v3 = round(mag_degrees_error, 3), v4 = round(mag_cm_error, 3),
                            v5 = round(heading_raw, 3), ha = heading_adjusted,
                            v6 = round(heading_error, 3), po=position_offset)
                )

            print('Moving to node {i}...'.format(i = i), end = '')
            await self.turn_to_angle(heading_adjusted)
            await self.move_forward(mag_degrees_adjusted)
            print('done')

            # update position
            self.position += position_offset

            if VERBOSE_LOGGING:
                print((
                    'Expected position: {t}\n'
                    'Final position: {p}\n'
                    'Final error: {e} cm\n')
                    .format(t = node, p = self.position, e = round((node - self.position).mag(), 3))
                )

        # find the final error now that we've reached the end of the path
        if VERBOSE_LOGGING:
            end_node = ROBOT_PATHS[path_name][-1]
            print('--- Pathing complete! ---')
            print((
                'Target position: {en}\n'
                'Actual position: {p}\n'
                'Error: {v0} cm')
                .format(en = end_node, p = self.position,
                        v0 = round((end_node - self.position).mag(), 3))
            )
        
        self.current_color = target_color