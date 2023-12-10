import time
from colorama import Fore, Back, Style

def is_all_zeroes(numbers):
    return all([x == 0 for x in numbers])

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    loop = []
    # get a matrix of chars from the input
    matrix = [[x for x in line] for line in input.splitlines()]
    # find the starting point marked by S
    starting = [(i, j) for i, row in enumerate(matrix) for j, x in enumerate(row) if x == 'S'][0]
    print(starting)
    find_loop(loop, matrix, starting)
    return len(loop) / 2

def find_loop(loop, matrix, starting):
    loop.append(starting)
    # get first step
    if(starting[0] > 0):
        if(matrix[starting[0]-1][starting[1]] in ['F','|','J']):
            loop.append((starting[0]-1, starting[1]))
    if((starting[0] < len(matrix)-1)  and loop[-1] == starting):
        if(matrix[starting[0]+1][starting[1]] in ['L','|','J']):
            loop.append((starting[0]+1, starting[1]))
    if(starting[1] > 0 and loop[-1] == starting):
        if(matrix[starting[0]][starting[1]-1] in ['F','-','L']):
            loop.append((starting[0], starting[1]-1))
    if((starting[1] < len(matrix[0])-1) and loop[-1] == starting):
        if(matrix[starting[0]][starting[1]+1] in ['7','-','J']):
            loop.append((starting[0], starting[1]+1))
    
    while loop[-1] != starting:
        if(matrix[loop[-1][0]][loop[-1][1]] == 'S'):
            break
        if(matrix[loop[-1][0]][loop[-1][1]] == 'F'):
            if(loop[-2][0] > loop[-1][0]):
                loop.append((loop[-1][0], loop[-1][1]+1))
            else:
                loop.append((loop[-1][0]+1, loop[-1][1]))
            continue
        if(matrix[loop[-1][0]][loop[-1][1]] == 'L'):
            if(loop[-1][0] > loop[-2][0]):
                loop.append((loop[-1][0], loop[-1][1]+1))
            else:
                loop.append((loop[-1][0]-1, loop[-1][1]))
            continue
        if(matrix[loop[-1][0]][loop[-1][1]] == '7'):
            if(loop[-2][0] > loop[-1][0]):
                loop.append((loop[-1][0], loop[-1][1]-1))
            else:
                loop.append((loop[-1][0]+1, loop[-1][1]))
            continue
        if(matrix[loop[-1][0]][loop[-1][1]] == 'J'):
            if(loop[-1][0] > loop[-2][0]):
                loop.append((loop[-1][0], loop[-1][1]-1))
            else:
                loop.append((loop[-1][0]-1, loop[-1][1]))
            continue
        if(matrix[loop[-1][0]][loop[-1][1]] == '|'):
            if(loop[-2][0] > loop[-1][0]):
                loop.append((loop[-1][0]-1, loop[-1][1]))
            else:
                loop.append((loop[-1][0]+1, loop[-1][1]))
            continue
        if(matrix[loop[-1][0]][loop[-1][1]] == '-'):
            if(loop[-1][1] > loop[-2][1]):
                loop.append((loop[-1][0], loop[-1][1]+1))
            else:
                loop.append((loop[-1][0], loop[-1][1]-1))
            continue


def print_digit(i,j,matrix,loop):
    if((i,j) in loop):
        print(Fore.GREEN + Style.DIM + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    if(matrix[i][j] == ','):
        print(Fore.LIGHTBLACK_EX + Style.DIM + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
    else:
        print(matrix[i][j], end='')

def matrix_counts(matrix, loop):
    in_the_loop = 0
    out_of_the_loop = 0
    undecided = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if((i,j) in loop):
                in_the_loop += 1
            elif(matrix[i][j] == ','):
                out_of_the_loop += 1
            else:
                undecided += 1
    return in_the_loop, out_of_the_loop, undecided

def solve_second(input: str):
    total = 0
    loop = []
    # get a matrix of chars from the input
    matrix = [[x for x in line] for line in input.splitlines()]
    # find the starting point marked by S
    starting = [(i, j) for i, row in enumerate(matrix) for j, x in enumerate(row) if x == 'S'][0]
    print(starting)
    find_loop(loop, matrix, starting)
    starting_time = time.time()
    # tranform any point in the matrix that is not in the loop to '#'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if((i,j) in loop):
                continue
            matrix[i][j] = '#'
    current_undecided = 0
    k = 0
    counts = matrix_counts(matrix, loop)
    while current_undecided != counts[2]:
        current_undecided = counts[2]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if((i,j) in loop):
                    continue
                if(matrix[i][j] == ','):
                    continue
                escaped = False
                for ii in range(i-1,i+2):
                    if escaped:
                        break
                    for jj in range(j-1,j+2):
                        # if ii,jj is out of bounds of the matrix
                        if(ii < 0 or jj < 0 or ii >= len(matrix) or jj >= len(matrix[0])):
                            escaped = True
                            break
                        if(matrix[ii][jj] == ','):
                            escaped = True
                            break
                if escaped:
                    matrix[i][j] = ','
                    continue
        counts = matrix_counts(matrix, loop)
        time_elapsed = time.time() - starting_time
        k += 1
        print(f'{k}: {counts[0]} {counts[1]} {counts[2]} {time_elapsed:.2f}')
        starting_time = time.time()
        
                    
    # print the matrix
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            print_digit(i,j,matrix,loop)
        print()
    return total