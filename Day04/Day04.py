import os
import re
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day04(BaseDay):
    def puzzle_1(self):
        search_lines = self.get_input_lines()
        xmas_count = 0
        # Diagonal up-left
        # Diagonal up-right
        # Diagonal down-left
        # Diagonal down-right
        # Left + Right
        for line in search_lines:
            xmas_count += line.count('SAMX')
            xmas_count += line.count('XMAS')
        # Up + Down
        for i in range(0, len(search_lines)):
            for j in range(0, len(search_lines[i])):
                # TODO: In here also do the checks for diagonal up nested in the up/down loops.
                # Only search upwards when the word fits.
                if i >= 3:
                    if search_lines[i][j] == 'X' \
                            and search_lines[i-1][j] == 'M' \
                            and search_lines[i-2][j] == 'A' \
                            and search_lines[i-3][j] == 'S':
                        xmas_count += 1
                    # Only search up left when the word fits.
                    if j >= 3:
                        if search_lines[i][j] == 'X' \
                                and search_lines[i-1][j-1] == 'M' \
                                and search_lines[i-2][j-2] == 'A' \
                                and search_lines[i-3][j-3] == 'S':
                            xmas_count += 1
                    # Only search up right when the word fits.
                    if j < len(search_lines) - 3:
                        if search_lines[i][j] == 'X' \
                                and search_lines[i-1][j+1] == 'M' \
                                and search_lines[i-2][j+2] == 'A' \
                                and search_lines[i-3][j+3] == 'S':
                            xmas_count += 1

                # Only search downwards when the word fits.
                if i < len(search_lines[i]) - 3:
                    if search_lines[i][j] == 'X' \
                            and search_lines[i+1][j] == 'M' \
                            and search_lines[i+2][j] == 'A' \
                            and search_lines[i+3][j] == 'S':
                        xmas_count += 1
                    # Only search down left when the word fits.
                    if j >= 3:
                        if search_lines[i][j] == 'X' \
                                and search_lines[i+1][j-1] == 'M' \
                                and search_lines[i+2][j-2] == 'A' \
                                and search_lines[i+3][j-3] == 'S':
                            xmas_count += 1
                    # Only search down right when the word fits.
                    if j < len(search_lines[i]) - 3:
                        if search_lines[i][j] == 'X' \
                                and search_lines[i+1][j+1] == 'M' \
                                and search_lines[i+2][j+2] == 'A' \
                                and search_lines[i+3][j+3] == 'S':
                            xmas_count += 1

        print(f'There are a total of {xmas_count} occurrences of the word "XMAS"')
