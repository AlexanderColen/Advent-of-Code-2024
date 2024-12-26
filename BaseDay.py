from os import path
import requests


class BaseDay:
    def who_dis(self) -> str:
        return type(self).__name__

    def puzzle_1(self):
        raise NotImplementedError('Developer is slacking...')

    def puzzle_2(self):
        # Exclude Day 25 as it has no puzzle 2.
        if self.who_dis() != 'Day25':
            raise NotImplementedError('Developer is slacking...')

    def get_input_lines(self) -> list:
        input_path = f'{self.who_dis()}/input.txt'
        # Download input data if not present yet.
        if not path.exists(input_path):
            # Determine day no to fetch data for.
            day_no = self.who_dis()[3:]
            if day_no.startswith('0'):
                day_no = day_no[1:]
            # Get cookie from file or user input.
            cookie_path = './cookie.txt'
            cookie = ''
            if path.exists(cookie_path):
                with open(cookie_path, 'r') as file:
                    for line in file:
                        cookie += line
            if not cookie:
                cookie = input(f'Please provide your cookie to fetch {day_no}''s Advent of Code input?\n>>>')
            # Get the actual input data from the AoC website.
            input_data = requests.get(f'https://adventofcode.com/2024/day/{day_no}/input', cookies={'session': cookie}).text
            with open(input_path, 'w') as file:
                file.write(input_data)

        with open(input_path, 'r') as file:
            lines = [line.rstrip() for line in file]
        return lines
