from enum import Enum
import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class HorizontalMultiplierEnum(Enum):
    LEFT = -1
    NONE = 0
    RIGHT = 1


class VerticalMultiplierEnum(Enum):
    UP = -1
    NONE = 0
    DOWN = 1


class Day04(BaseDay):
    def search_diagonal(
        self,
        lines: list,
        x: int,
        y: int,
        target: str,
        horizontal_multiplier: HorizontalMultiplierEnum,
        vertical_multiplier: VerticalMultiplierEnum
    ) -> bool:
        valid = True
        for i in range(0, len(target)):
            try:
                x_check = x + (i * horizontal_multiplier.value)
                y_check = y + (i * vertical_multiplier.value)
                if x_check < 0 or y_check < 0:
                    raise IndexError
                if not lines[y_check][x_check] == target[i]:
                    raise IndexError
            except IndexError:
                valid = False
                break

        return valid

    def puzzle_1(self):
        search_lines = self.get_input_lines()
        xmas_count = 0
        search_str = 'XMAS'
        for i in range(0, len(search_lines)):
            for j in range(0, len(search_lines[i])):
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.NONE, VerticalMultiplierEnum.UP):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.NONE, VerticalMultiplierEnum.DOWN):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.LEFT, VerticalMultiplierEnum.UP):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.LEFT, VerticalMultiplierEnum.NONE):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.LEFT, VerticalMultiplierEnum.DOWN):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.RIGHT, VerticalMultiplierEnum.UP):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.RIGHT, VerticalMultiplierEnum.NONE):
                    xmas_count += 1
                if self.search_diagonal(search_lines, j, i, search_str, HorizontalMultiplierEnum.RIGHT, VerticalMultiplierEnum.DOWN):
                    xmas_count += 1

        print(f'There are a total of {xmas_count} occurrences of the word "XMAS"')

    def puzzle_2(self):
        search_lines = self.get_input_lines()
        x_mas_count = 0
        for i in range(0, len(search_lines)):
            for j in range(0, len(search_lines[i])):
                if search_lines[i][j] == 'A':
                    try:
                        if i - 1 < 0 or j - 1 < 0:
                            raise IndexError
                        if ((search_lines[i-1][j-1] == 'M' and search_lines[i+1][j+1] == 'S') \
                                or (search_lines[i-1][j-1] == 'S' and search_lines[i+1][j+1] == 'M')) \
                                and ((search_lines[i-1][j+1] == 'M' and search_lines[i+1][j-1] == 'S') \
                                    or (search_lines[i-1][j+1] == 'S' and search_lines[i+1][j-1] == 'M')):
                            x_mas_count += 1
                    except IndexError:
                        pass

        print(f'There are a total of {x_mas_count} "X"-"MAS" occurrences')
