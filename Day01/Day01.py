import sys
import os


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay
import re

class Day01(BaseDay):
    def puzzle_1(self):
        left_list = []
        right_list = []
        for line in self.get_input_lines():
            splits = re.split(r'\s+', line)
            left_list.append(int(splits[0]))
            right_list.append(int(splits[1]))

        left_list.sort()
        right_list.sort()

        total_distance = 0
        for i in range(0, len(left_list)):
            total_distance += abs(left_list[i] - right_list[i])
        print(f'The total distance between the two lists is: {total_distance}')
