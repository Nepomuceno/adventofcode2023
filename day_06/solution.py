import re

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 1
    times = [int(x) for x in re.findall(r'\d+', input.splitlines()[0])]
    distances = [int(x) for x in re.findall(r'\d+', input.splitlines()[1])]
    for i in range(len(times)):
        time = times[i]
        distance = distances[i]
        number_coditions = 0
        for j in range(time):
            travel = j * (time - j)
            if travel > distance:
                number_coditions += 1
        total *= number_coditions
    return total
        
def solve_second(input: str):
    lines = input.splitlines()
    time = int(lines[0].split(': ')[1].replace(' ', ''))
    distance = int(lines[1].split(': ')[1].replace(' ', ''))
    number_coditions = 0
    for j in range(time):
        travel = j * (time - j)
        if travel > distance:
            number_coditions += 1
    return number_coditions


    