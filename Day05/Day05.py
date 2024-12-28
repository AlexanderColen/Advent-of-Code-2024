import os
import sys


current = os.path.dirname(os.path.realpath(__file__))
parent = os.path.dirname(current)
sys.path.append(parent)

from BaseDay import BaseDay


class Day05(BaseDay):
    def parse_input(self, input_data: list) -> (list, list):
        order_rules = []
        updates = []
        parsed_rules = False

        for line in input_data:
            if not line:
                parsed_rules = True
            elif parsed_rules:
                updates.append(line)
            else:
                order_rules.append(line)

        return order_rules, updates

    def extract_correct_updates(self, rules: list, updates: list) -> list:
        correct_updates = []

        for update in updates:
            correct = True
            page_nos = update.split(',')

            for i in range(0, len(page_nos) - 1):
                # Try to find a rule that contain both page nos.
                for rule in rules:
                    if page_nos[i] in rule and page_nos[i+1] in rule:
                        correct = rule.index(page_nos[i]) < rule.index(page_nos[i + 1])
                        break
                    else:
                        pass
                if not correct:
                    break

            if correct:
                correct_updates.append(update)

        return correct_updates

    def count_middle_pages(self, updates: list) -> int:
        return sum(int(update.split(',')[len(update.split(',')) // 2]) for update in updates)

    def puzzle_1(self):
        input_data = self.get_input_lines()
        rules, updates = self.parse_input(input_data)
        correct_updates = self.extract_correct_updates(rules, updates)

        print(f'The sum of the middle pages of correctly ordered updates is {self.count_middle_pages(correct_updates)}.')
