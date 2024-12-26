import os
import re
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day03(BaseDay):
    def puzzle_1(self):
        multiplication_total = 0
        for memory_line in self.get_input_lines():
            for match in re.finditer(r'(?<=mul\()\d{1,3},\d{1,3}(?=\))', memory_line):
                x, y = match.group().split(',')
                multiplication_total += int(x) * int(y)
        print(f'The total sum of all the multiplications is {multiplication_total}')
