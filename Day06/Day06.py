import copy
import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class InfiniteLoopException(Exception):
    pass


class Day06(BaseDay):
    def build_grid(self) -> list:
        input_data = self.get_input_lines()
        return [list(row) for row in input_data]

    def is_coordinate_in_bounds(self, coordinate: list, grid: list) -> bool:
        return 0 <= coordinate[0] < len(grid[0]) and 0 <= coordinate[1] < len(grid)

    def simulate_guard_patrol(self, grid: list) -> list:
        guard_position = None
        obstacle_coordinates = []
        coordinates_visited = []
        detailed_visits = []
        for y in range(0, len(grid)):
            for x in range(0, len(grid[y])):
                if grid[y][x] == '#':
                    obstacle_coordinates.append([x, y])
                elif grid[y][x] == '^':
                    guard_position = [x, y]
                    coordinates_visited.append(guard_position)
                    detailed_visits.append([guard_position, '^'])

        patrolling = guard_position is not None
        direction = '^'
        while patrolling:
            new_coordinate = guard_position
            new_direction = direction
            # North
            if direction == '^':
                new_coordinate = [guard_position[0], guard_position[1] - 1]
                new_direction = '>'
            # East
            elif direction == '>':
                new_coordinate = [guard_position[0] + 1, guard_position[1]]
                new_direction = 'v'
            # South
            elif direction == 'v':
                new_coordinate = [guard_position[0], guard_position[1] + 1]
                new_direction = '<'
            # West
            elif direction == '<':
                new_coordinate = [guard_position[0] - 1, guard_position[1]]
                new_direction = '^'

            patrolling = self.is_coordinate_in_bounds(new_coordinate, grid)

            if patrolling:
                if new_coordinate not in obstacle_coordinates:
                    guard_position = new_coordinate
                    if guard_position not in coordinates_visited:
                        coordinates_visited.append(guard_position)

                    new_detailed_visit = [guard_position, direction]
                    if new_detailed_visit not in detailed_visits:
                        detailed_visits.append(new_detailed_visit)
                    else:
                        raise InfiniteLoopException
                else:
                    direction = new_direction

        return coordinates_visited

    def puzzle_1(self):
        grid = self.build_grid()

        print(f'The distinct positions visited by the guards is {len(self.simulate_guard_patrol(grid))}.')

    def puzzle_2(self):
        grid = self.build_grid()

        initial_route_coordinates = self.simulate_guard_patrol(grid)

        infinite_loop_obstacles = []
        for coordinate in initial_route_coordinates:
            try:
                new_grid = copy.deepcopy(grid)
                y = coordinate[1]
                x = coordinate[0]
                new_grid[y][x] = '#'
                self.simulate_guard_patrol(new_grid)
            except InfiniteLoopException:
                infinite_loop_obstacles.append(coordinate)

        print(f'There are {len(infinite_loop_obstacles)} different positions to place an obstacle to create an infinite loop.')
