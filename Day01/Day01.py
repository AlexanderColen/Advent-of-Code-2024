import os
import re
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day01(BaseDay):
    def build_lists(self) -> (list, list):
        left_list = []
        right_list = []
        for line in self.get_input_lines():
            splits = re.split(r'\s+', line)
            left_list.append(int(splits[0]))
            right_list.append(int(splits[1]))

        left_list.sort()
        right_list.sort()

        return left_list, right_list

    def puzzle_1(self):
        left_list, right_list = self.build_lists()
        total_distance = 0
        for i in range(0, len(left_list)):
            total_distance += abs(left_list[i] - right_list[i])
        print(f'The total distance between the two lists is: {total_distance}')

    def puzzle_2(self):
        left_list, right_list = self.build_lists()
        total_similarity = 0
        for i in left_list:
            total_similarity += i * (right_list.count(i))
        print(f'The total similarity score between the two lists is: {total_similarity}')