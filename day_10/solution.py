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
    if(matrix[i][j] == '.'):
        print(Fore.YELLOW + Style.BRIGHT + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    if(matrix[i][j] == ','):
        print(Fore.LIGHTBLACK_EX + Style.DIM + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return
    if((i,j) in loop):
        print(Fore.GREEN + Style.DIM + matrix[i][j] + Fore.RESET + Style.RESET_ALL, end='')
        return

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
            elif(matrix[i][j] == '.'):
                in_the_loop += 1
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
    
    # tranform any point in the matrix that is not in the loop to '#'
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if((i,j) in loop):
                continue
            matrix[i][j] = '#'
    find_counts(loop, matrix)
    simplify_loop(loop, matrix)
    find_counts(loop, matrix)
        
    counts = matrix_counts(matrix, loop)
    print(f'{counts[0]} {counts[1]} {counts[2]}')
    # print the matrix
    for i, row in enumerate(matrix):
        for j, x in enumerate(row):
            print_digit(i,j,matrix,loop)
        print()
    return total

def find_counts(loop, matrix):
    starting_time = time.time()
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

def simplify_loop(loop, matrix):
    for i in range(10):
        for point in loop:
            if(matrix[point[0]][point[1]] == 'L'):
                if((point[0]-1, point[1]) in loop) and (point[0], point[1]+1) in loop and (point[0]-1, point[1]+1) in loop:
                    # | |  L J  
                    # L J  . .
                    if matrix[point[0]-1][point[1]] == '|' and matrix[point[0]][point[1]+1] == 'J' and matrix[point[0]-1][point[1]+1] == '|':
                        matrix[point[0]-1][point[1]] = 'L'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]-1][point[1]+1] = 'J'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0], point[1]+1) in loop:
                            loop.remove((point[0], point[1]+1))
                        continue
                    # F -  . F
                    # L -  . L
                    if matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]][point[1]+1] == '-' and matrix[point[0]-1][point[1]+1] == '-':
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]][point[1]+1] = 'L'
                        matrix[point[0]-1][point[1]+1] = 'F'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0]-1, point[1]) in loop:
                            loop.remove((point[0]-1, point[1]))
                        continue
                    if matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]][point[1]+1] == '7' and matrix[point[0]-1][point[1]+1] == 'J':
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]][point[1]+1] = '|'
                        matrix[point[0]-1][point[1]+1] = '|'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0]-1, point[1]) in loop:
                            loop.remove((point[0]-1, point[1]))
                        continue
                    if matrix[point[0]-1][point[1]] == '|' and matrix[point[0]][point[1]+1] == 'J' and matrix[point[0]-1][point[1]+1] == 'F':
                        matrix[point[0]-1][point[1]] = 'L'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]-1][point[1]+1] = '-'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0], point[1]+1) in loop:
                            loop.remove((point[0], point[1]+1))
                        continue
                    # 7 |  - J
                    # L J  . .
                    if matrix[point[0]-1][point[1]] == '7' and matrix[point[0]][point[1]+1] == 'J' and matrix[point[0]-1][point[1]+1] == '|':
                        matrix[point[0]-1][point[1]] = '-'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]-1][point[1]+1] = 'J'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0], point[1]+1) in loop:
                            loop.remove((point[0], point[1]+1))
                        continue
                    # F J  . |
                    # L -  . L
                    if matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]][point[1]+1] == '-' and matrix[point[0]-1][point[1]+1] == 'J':
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]][point[1]+1] = 'L'
                        matrix[point[0]-1][point[1]+1] = '|'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0]-1, point[1]) in loop:
                            loop.remove((point[0]-1, point[1]))
                        continue
                    # 7 F  - -
                    # L J  . .
                    if matrix[point[0]-1][point[1]] == '7' and matrix[point[0]][point[1]+1] == 'J' and matrix[point[0]-1][point[1]+1] == 'F':
                        matrix[point[0]-1][point[1]] = '-'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]-1][point[1]+1] = '-'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0], point[1]+1) in loop:
                            loop.remove((point[0], point[1]+1))
                        continue
                    # F -  - -
                    # L 7  . L
                    if matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]][point[1]+1] == '7' and matrix[point[0]-1][point[1]+1] == '-':
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]][point[1]+1] = '|'
                        matrix[point[0]-1][point[1]+1] = 'F'
                        matrix[point[0]][point[1]] = '.'
                        if (point[0], point[1]) in loop:
                            loop.remove((point[0], point[1]))
                        if (point[0]-1, point[1]) in loop:
                            loop.remove((point[0]-1, point[1]))
                        continue
            if(matrix[point[0]][point[1]] == 'J'):
                if((point[0]-1, point[1]) in loop) and (point[0], point[1]+1) in loop and (point[0]-1, point[1]+1) in loop:
                    if(matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == 'L'):
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '-'
                        matrix[point[0]][point[1]] = '-'
                        loop.remove((point[0]-1, point[1]))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
                    if(matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == '|'):
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '-'
                        matrix[point[0]][point[1]] = '7'
                        loop.remove((point[0]-1, point[1]))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
            if(matrix[point[0]][point[1]] == '|'):
                if((point[0]-1, point[1]) in loop) and (point[0], point[1]+1) in loop and (point[0]-1, point[1]+1) in loop:
                    if(matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == 'L'):
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '-'
                        matrix[point[0]][point[1]] = 'F'
                        loop.remove((point[0]-1, point[1]))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
                    if(matrix[point[0]-1][point[1]] == 'F' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == '|'):
                        matrix[point[0]-1][point[1]] = '.'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '7'
                        matrix[point[0]][point[1]] = 'F'
                        loop.remove((point[0]-1, point[1]))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
            if(matrix[point[0]][point[1]] == 'F'):
                if((point[0]-1, point[1]) in loop) and (point[0], point[1]+1) in loop and (point[0]-1, point[1]+1) in loop:
                    if(matrix[point[0]-1][point[1]] == 'L' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == 'J'):
                        matrix[point[0]-1][point[1]] = '|'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]][point[1]] = '|'
                        loop.remove((point[0], point[1]+1))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
            if(matrix[point[0]][point[1]] == '-'):
                if((point[0]-1, point[1]) in loop) and (point[0], point[1]+1) in loop and (point[0]-1, point[1]+1) in loop:
                    if(matrix[point[0]-1][point[1]] == 'L' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == 'J'):
                        matrix[point[0]-1][point[1]] = '|'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]][point[1]] = 'J'
                        loop.remove((point[0], point[1]+1))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
                    if(matrix[point[0]-1][point[1]] == '-' and matrix[point[0]-1][point[1]+1] == '7' and matrix[point[0]][point[1]+1] == 'J'):
                        matrix[point[0]-1][point[1]] = '7'
                        matrix[point[0]-1][point[1]+1] = '.'
                        matrix[point[0]][point[1]+1] = '.'
                        matrix[point[0]][point[1]] = 'J'
                        loop.remove((point[0], point[1]+1))
                        loop.remove((point[0]-1, point[1]+1))
                        continue;
# the rsponse it is lower than 450 (the correct one)