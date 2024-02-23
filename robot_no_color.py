# version of the robot class without any color_print calls
from vector import *
from robot_paths import *

VERBOSE_LOGGING = True

NODE_SIZE = 0.5 # if the robot is within this many centimeters of a node, it's at the node

class Robot:
  def __init__(self, x, y):
    self.position = Vector(x, y)
    self.heading = 0

  def at_node(self, node: Vector) -> bool:
    delta = node - self.position # Vector
    return delta.mag() < NODE_SIZE
  
  def turn_to_angle(self, angle: int) -> None:
    delta = angle - self.heading
    # motor code here
    self.heading = angle

  def move_forward(self, motor_degrees: int) -> None:
    # motor code here
    pass # keeps python happy; remove this when you add motor code

  def follow_path(self, path_name: str) -> None:
    print(f"Moving along path '{path_name}'")
    path = ROBOT_PATHS[path_name]
    for i, node in enumerate(path):  
      reached_node = False
      while not reached_node:
        if VERBOSE_LOGGING:
          print((
            f'--- Moving to node {i} ---\n'
            f'Node position: {node}\n'
            f'Current position: {self.position}'
          ))

        if self.at_node(node):
          if VERBOSE_LOGGING:
            print('Already at node!\n')
          else:
            print(f'Already at node {i}')
          reached_node = True
        else:
          delta = node - self.position

          # the magnitude will be a float and the motor control functions only take ints,
          # so we'll round to get as close as we can
          mag_cm_raw = delta.mag()
          mag_degrees_raw = mag_cm_raw * 26 # convert to degrees for maximum precision

          mag_degrees_adjusted = round(mag_degrees_raw)
          mag_cm_adjusted = mag_degrees_adjusted / 26
          
          mag_degrees_error = abs(mag_degrees_raw - mag_degrees_adjusted)
          mag_cm_error = mag_degrees_error / 26

          # adjust the heading
          heading_raw = delta.heading()
          heading_adjusted = round(heading_raw)
          heading_error = abs(heading_raw - heading_adjusted)

          if VERBOSE_LOGGING:
            print((
              f'Delta vector: {delta}\n\n'
              f'Raw length: {round(mag_degrees_raw, 3)}° ({round(mag_cm_raw, 3)} cm)\n'
              f'Adjusted length: {mag_degrees_adjusted}° ({round(mag_cm_adjusted, 3)} cm)\n'
              f'Length error: {round(mag_degrees_error, 3)}° ({round(mag_cm_error, 3)} cm)\n\n'
              f'Raw heading: {round(heading_raw, 3)}°\n'
              f'Adjusted heading: {heading_adjusted}°\n'
              f'Heading error: {round(heading_error, 3)}°\n'
            ))

          position_offset = vec_from_polar(mag_cm_adjusted, heading_adjusted)
          if VERBOSE_LOGGING:
            print(f'Adjusted vector: {position_offset}')

          print(f'Moving to node {i}...', end='')
          self.turn_to_angle(heading_adjusted)
          self.move_forward(mag_degrees_adjusted)
          print('done')

          # update position
          self.position += position_offset

          if VERBOSE_LOGGING:
            print((
              f'Final position: {self.position}\n'
              f'Final error: {round((node - self.position).mag(), 3)} cm'
            ))

          # we're probably at the node, but check again just to be safe
          if self.at_node(node):
            if VERBOSE_LOGGING:
              print('Position on target, moving to next node\n')
            reached_node = True
          elif VERBOSE_LOGGING:
             print('Position off target, retrying current node\n')

    # find the final error now that we've reached the end of the path
    end_node = ROBOT_PATHS[path_name][-1]
    print('--- Pathing complete! ---')
    if VERBOSE_LOGGING:
      print((
        f'Target position: {end_node}\n'
        f'Actual position: {self.position}\n'
        f'Error: {round((end_node - self.position).mag(), 3)}'
      ))
            