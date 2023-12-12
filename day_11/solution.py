import time
from colorama import Fore, Back, Style

debug_print=False

def is_all_zeroes(numbers):
    return all([x == 0 for x in numbers])

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    # get a matrix of chars from the input
    matrix = [[x for x in line] for line in input.splitlines()]
    # find every line that does not have # in it
    lines = [i for i, line in enumerate(matrix) if '#' not in line]
    # find every column that does not have # in it
    columns = [i for i, column in enumerate(zip(*matrix)) if '#' not in column]
    # insert a new line of only . after every line that does not have #
    inserted = 0
    print_matrix(matrix)
    for i in lines:
        matrix.insert(i+inserted, ['.'] * len(matrix[i]))
        inserted += 1
    # insert a new column of only . after every column that does not have #
    inserted = 0
    for i in columns:
        for j in range(len(matrix)):
            matrix[j].insert(i + inserted, '.')
        inserted += 1
    print_matrix(matrix)
    # find every galaxy in the matrix
    galaxies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                galaxies.append((i,j))
    for i, starting in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            destination = galaxies[j]
            distance = get_distance(starting, destination)
            print_matrix(matrix, [starting, destination])
            if debug_print:
                print(f"Distance from {starting} to {destination} is {distance}")
            total += distance
    return total

def get_distance(starting, destination):
    starting_x, starting_y = starting
    destination_x, destination_y = destination
    return abs(starting_x - destination_x) + abs(starting_y - destination_y)

def print_matrix(matrix, interesting = []):
    if not debug_print:
        return
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            print_digit(i,j,matrix, interesting)
        print()

def print_digit(i,j,matrix, interesting = []):
    
    if (i,j) in interesting:
        print(Fore.RED + Style.BRIGHT + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    if(matrix[i][j] == '#'):
        print(Fore.YELLOW + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    if(matrix[i][j] == '.'):
        print(Fore.LIGHTBLACK_EX + Style.DIM + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    print(matrix[i][j], end='')


def solve_second(input: str):
    total = 0
    expasion_rate = 1000000
    # get a matrix of chars from the input
    matrix = [[x for x in line] for line in input.splitlines()]
    # find every line that does not have # in it
    lines = [i for i, line in enumerate(matrix) if '#' not in line]
    # find every column that does not have # in it
    columns = [i for i, column in enumerate(zip(*matrix)) if '#' not in column]  
    # find every galaxy in the matrix
    galaxies = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == '#':
                galaxies.append((i,j))
    for i , galaxy in enumerate(galaxies):
        galaxy_x, galaxy_y = galaxy
        # count the number of lines that are smaller than the current galaxy x
        lines_smaller = len([line for line in lines if line < galaxy_x])
        galaxy_x = ((expasion_rate-1) * lines_smaller) + galaxy_x
        # count the number of columns that are smaller than the current galaxy y
        columns_smaller = len([column for column in columns if column < galaxy_y])
        galaxy_y = ((expasion_rate-1) * columns_smaller) + galaxy_y
        galaxies[i] = (galaxy_x, galaxy_y)
    
    print_matrix(matrix)
    for i, starting in enumerate(galaxies):
        for j in range(i+1, len(galaxies)):
            destination = galaxies[j]
            distance = get_distance(starting, destination)
            print_matrix(matrix, [starting, destination])
            if debug_print:
                print(f"Distance from {starting} to {destination} is {distance}")
            total += distance
    return total

# the rsponse it is lower than 450 (the correct one)