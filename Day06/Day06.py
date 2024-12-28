import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day06(BaseDay):
    def is_coordinate_in_bounds(self, coordinate: list, grid: list) -> bool:
        return coordinate[0] >= 0 \
               and coordinate[1] >= 0 \
               and coordinate[0] < len(grid[0]) \
               and coordinate[1] < len(grid)

    def puzzle_1(self):
        grid = self.get_input_lines()

        guard_position = None
        obstacle_coordinates = []
        coordinates_visited = []
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == '#':
                    obstacle_coordinates.append([x,y])
                elif grid[y][x] == '^':
                    guard_position = [x, y]
                    coordinates_visited.append([x,y])

        patrolling = True
        direction = '^'
        while patrolling:
            new_coordinate = guard_position
            # North
            if direction == '^':
                new_coordinate = [guard_position[0], guard_position[1] - 1]
            # East
            elif direction == '>':
                new_coordinate = [guard_position[0] + 1, guard_position[1]]
            # South
            elif direction == '<':
                new_coordinate = [guard_position[0] - 1, guard_position[1]]
            # West
            elif direction == 'v':
                new_coordinate = [guard_position[0], guard_position[1] + 1]

            patrolling = self.is_coordinate_in_bounds(new_coordinate, grid)

            if patrolling:
                if new_coordinate not in obstacle_coordinates:
                    guard_position = new_coordinate
                    if new_coordinate not in coordinates_visited:
                        coordinates_visited.append(new_coordinate)
                else:
                    if direction == '^':
                        direction = '>'
                    elif direction == '>':
                        direction = 'v'
                    elif direction == 'v':
                        direction = '<'
                    elif direction == '<':
                        direction = '^'

        print(f'The distinct positions visited by the guards is {len(coordinates_visited)}.')
