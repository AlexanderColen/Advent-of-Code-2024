import os
import re
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day03(BaseDay):
    def calculate_multiplications(self, memory_line: str) -> int:
        multiplication_total = 0
        for match in re.finditer(r'(?<=mul\()\d{1,3},\d{1,3}(?=\))', memory_line):
            x, y = match.group().split(',')
            multiplication_total += int(x) * int(y)
        return multiplication_total

    def puzzle_1(self):
        multiplication_total = 0
        for memory_line in self.get_input_lines():
            multiplication_total += self.calculate_multiplications(memory_line)
        print(f'The total sum of all the multiplications is {multiplication_total}')

    def puzzle_2(self):
        multiplication_total = 0
        skip = False
        for memory_line in self.get_input_lines():
            while len(memory_line) > 0:
                if skip:
                    match = re.search(r'do\(\)', memory_line)
                    if match is not None:
                        memory_line = memory_line[match.span()[1]:]
                        skip = False
                    else:
                        memory_line = ''
                else:
                    match = re.search(r"don't\(\)", memory_line)
                    if match is not None:
                        multiplication_total += self.calculate_multiplications(memory_line[0:match.span()[0]])
                        memory_line = memory_line[match.span()[1]:]
                        skip = True
                    else:
                        # No match here at the end means that we want to calculate the last batch before we empty it.
                        multiplication_total += self.calculate_multiplications(memory_line[0:])
                        memory_line = ''

        print(f'The total sum of all the multiplications is {multiplication_total}')
