from importlib import import_module
from datetime import datetime

allowed_days = [f'{i}' for i in range(1, 26)]
day_no = None
while day_no not in allowed_days:
    day_no = input(f'Which day do you want to run the puzzle(s) for? ({" / ".join(allowed_days)})\n>>>')

allowed_puzzles = ['1', '2', 'both']
puzzle_no = None
while puzzle_no not in allowed_puzzles:
    puzzle_no = input(f'Would you like to run just puzzle 1, 2 or both? ({" / ".join(allowed_puzzles)})\n>>>')

if len(day_no) == 1:
    day_no = f'0{day_no}'
module_str: str = f'Day{day_no}'
class_str: str = f'Day{day_no}.Day{day_no}'
try:
    module = import_module(class_str)
    class_instance = getattr(module, module_str)
    day_class = class_instance()
    puzzle_1 = getattr(day_class, 'puzzle_1')
    puzzle_2 = getattr(day_class, 'puzzle_2')

    if puzzle_no in ['1', 'both']:
        start = datetime.now()
        puzzle_1()
        end = datetime.now()
        print(f'Puzzle 1 finished in {end - start}')

    if puzzle_no in ['2', 'both']:
        start = datetime.now()
        puzzle_2()
        end = datetime.now()
        print(f'Puzzle 2 finished in {end - start}')
except ModuleNotFoundError:
    raise ModuleNotFoundError(f'Module "{class_str}" does not exist (yet).')
