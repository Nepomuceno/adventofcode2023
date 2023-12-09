import time

def is_all_zeroes(numbers):
    return all([x == 0 for x in numbers])

def solve(input: str, second: bool):
    total = 0
    if second:
        return solve_second(input)
    # split in lines and each line in a sequence of integers
    lines = input.splitlines()
    numbers = []
    for line in lines:
        numbers.append([int(x) for x in line.split(' ')])
    for line in numbers:
        sequences = [line]
        while not is_all_zeroes(sequences[-1]):
            new_sequence = []
            for i in range(0, len(sequences[-1])-1):
                new_sequence.append(sequences[-1][i+1] - sequences[-1][i])
            sequences.append(new_sequence)
        sequences.reverse()
        for i in range(0, len(sequences)-1):
            sequences[i+1].append(sequences[i][-1] + sequences[i+1][-1])
        sequences.reverse()
        total += sequences[0][-1]
        print(sequences[0][-1])
        print('---')

    return total

    
def solve_second(input: str):
    total = 0
    # split in lines and each line in a sequence of integers
    lines = input.splitlines()
    numbers = []
    for line in lines:
        numbers.append([int(x) for x in line.split(' ')])
    for line in numbers:
        sequences = [line]
        while not is_all_zeroes(sequences[-1]):
            new_sequence = []
            for i in range(0, len(sequences[-1])-1):
                new_sequence.append(sequences[-1][i+1] - sequences[-1][i])
            sequences.append(new_sequence)
        sequences.reverse()
        for i in range(0, len(sequences)-1):
            sequences[i+1].insert(0, sequences[i+1][0] - sequences[i][0])
        sequences.reverse()
        total += sequences[0][0]
        print(sequences[0][0])
        print('---')

    return total