import argparse
import datetime
from importlib import import_module

def get_day():
    return int(datetime.datetime.now().strftime('%d'))

def get_input(day):
    return open('day_{:02d}/input.txt'.format(day)).read()

def get_sample(day):
    return open('day_{:02d}/sample.txt'.format(day)).read()

def solve_day(day, input, second):
    module_name = f'day_{day:02d}.solution'
    module = import_module(module_name)
    return module.solve(input, second)

def main():
    parser = argparse.ArgumentParser(description='Run the advent of code 2020 challenge')
    parser.add_argument('--day', type=int, help='the day of the challenge')
    parser.add_argument('--solve', action='store_true', help='solve the challenge')
    parser.add_argument('--second', action='store_true', help='solve the second part of the challenge')
    args = parser.parse_args()
    day = args.day
    solve = args.solve
    second = args.second
    if day is None:
        day = get_day()
    if solve:
        input = get_input(day)
    else:
        input = get_sample(day)
    solution = solve_day(day, input, second)
    print(solution)

if __name__ == '__main__':
    main()
