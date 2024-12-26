import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day02(BaseDay):
    def puzzle_1(self):
        safe_reports = 0
        for report in self.get_input_lines():
            levels = [int(i) for i in report.split(' ')]
            previous = levels[0]
            change = None  # True = increasing, False = decreasing
            unsafe = False
            for level in levels[1:]:
                difference = abs(level - previous)
                if difference < 1 or difference > 3:
                    unsafe = True
                    break

                if change is None:
                    change = level > previous
                else:
                    if (change and level < previous) \
                            or (not change and level > previous):
                        unsafe = True
                        break

                previous = level

            if not unsafe:
                safe_reports += 1
        print(f'There are {safe_reports} safe reports.')
