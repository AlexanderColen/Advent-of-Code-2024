import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day07(BaseDay):
    def attempt_operator(self, values: list, operator: str, desire: int) -> bool:
        if any([value > desire for value in values]):
            return False

        calculated_value = 0
        if operator == '+':
            calculated_value = values[0] + values[1]
        elif operator == '*':
            calculated_value = values[0] * values[1]

        if len(values) - 2 == 0:
            return calculated_value == desire

        new_values = [calculated_value]
        for value in values[2:]:
            new_values.append(value)

        return self.attempt_operator(
            values=new_values,
            operator='+',
            desire=desire
        ) or self.attempt_operator(
            values=new_values,
            operator='*',
            desire=desire
        )

    def puzzle_1(self):
        input_data = self.get_input_lines()

        calibration_result = 0
        for line in input_data:
            desire, values = line.split(': ')
            desire = int(desire)
            values = [int(value) for value in values.strip().split(' ')]

            if self.attempt_operator(values=values, operator='+', desire=desire) \
                    or self.attempt_operator(values=values, operator='*', desire=desire):
                calibration_result += desire

        print(f'The total calibration result with + and * is {calibration_result}.')
