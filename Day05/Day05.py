from itertools import combinations
import os
import re
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

    def validate_correct_update(self, rules: list, update: str) -> bool:
        correct = True
        page_nos = update.split(',')

        for i in range(0, len(page_nos) - 1):
            # Try to find a rule that contain both page nos.
            for rule in rules:
                if page_nos[i] in rule and page_nos[i+1] in rule:
                    correct = rule.index(page_nos[i]) < rule.index(page_nos[i+1])
                    break
                else:
                    pass
            if not correct:
                break

        return correct

    def extract_correct_updates(self, rules: list, updates: list) -> list:
        correct_updates = []

        for update in updates:
            if self.validate_correct_update(rules, update):
                correct_updates.append(update)

        return correct_updates

    def count_middle_pages(self, updates: list) -> int:
        return sum(int(update.split(',')[len(update.split(',')) // 2]) for update in updates)

    def puzzle_1(self):
        input_data = self.get_input_lines()
        rules, updates = self.parse_input(input_data)
        correct_updates = self.extract_correct_updates(rules, updates)

        print(f'The sum of the middle pages of correctly ordered updates is {self.count_middle_pages(correct_updates)}.')

    def puzzle_2(self):
        input_data = self.get_input_lines()
        rules, updates = self.parse_input(input_data)
        correct_updates = self.extract_correct_updates(rules, updates)
        incorrect_updates = [update for update in updates if update not in correct_updates]

        fixed_updates = []
        for incorrect_update in incorrect_updates:
            # Extract all rules between all the numbers
            page_nos = incorrect_update.split(',')
            possible_page_pairs = combinations(page_nos, 2)
            page_regexes = []
            for pair in possible_page_pairs:
                page_regexes.append(r'\|'.join(pair))
                page_regexes.append(r'\|'.join([pair[-1], pair[0]]))
            relevant_rules = []
            for page_regex in page_regexes:
                for rule in rules:
                    if re.search(page_regex, rule):
                        relevant_rules.append(rule)
                        break

            # Count how many times each number is the start of a pair.
            page_counts = {}
            for page_no in page_nos:
                page_counts[page_no] = 0

            for relevant_rule in relevant_rules:
                page_counts[relevant_rule[:2]] += 1

            # Sort & build correct update based on that count.
            page_counts = sorted(page_counts.items(), key=lambda item: item[1])
            page_counts.reverse()
            fixed_update = ''
            for page_no in page_counts:
                fixed_update += f',{page_no[0]}'

            fixed_updates.append(fixed_update[1:])

        print(f'The sum of the middle pages of fixed incorrectly ordered updates is {self.count_middle_pages(fixed_updates)}.')
