import time
from colorama import Fore, Back, Style
import itertools

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp
    return arr


def permute(i: int, s: str) -> list[str]:
    # Base case
    if i == (len(s) - 1):
        # print(s)
        return [s]

    prev = "*"
    result = []
    # Loop from j = 1 to length of String
    for j in range(i, len(s)):
        temp = list(s)
        if j > i and temp[i] == temp[j]:
            continue
        if prev != "*" and prev == s[j]:
            continue

        # Swap the elements
        temp = swap(temp, i, j)
        prev = s[j]

        # Recursion call
        result.extend(permute(i + 1, "".join(temp)))
    return result


def sortString(inputString):
    # Convert input string to char array
    tempArray = list(inputString)
    # Sort tempArray
    tempArray.sort()
    # Return new sorted string
    return "".join(tempArray)


def is_valid_solution(item: tuple[str, list[int]]):
    contigous_sharps = []
    contigous = 0
    for i in range(len(item[0])):
        if item[0][i] == "#":
            contigous += 1
        else:
            if contigous > 0:
                contigous_sharps.append(contigous)
            contigous = 0
    if contigous > 0:
        contigous_sharps.append(contigous)
    expected = item[1]
    if len(expected) != len(contigous_sharps):
        return False
    for i in range(len(expected)):
        if expected[i] != contigous_sharps[i]:
            return False
    return True


def fill_all_required(problems: list[tuple[str, list[int]]]) -> list[list[str]]:
    total_valid_permutations = []
    for problem in problems:
        input = problem[0]
        # number of # in the input string
        number_of_sharp = input.count("#")
        # number of . in the input string
        number_of_dot = input.count(".")
        total_of_sharp = sum(problem[1])
        total_of_dot = len(problem[0]) - total_of_sharp
        missing_sharp = total_of_sharp - number_of_sharp
        missing_dot = total_of_dot - number_of_dot
        # string with missing sharp and dot
        missing_string = "#" * missing_sharp + "." * missing_dot
        permutations = permute(0, sortString(missing_string))

        # for each permutation replace all the ? in the input with the permutation in the same order
        # for exemple the input ???.#. with the permutation ##. will result in ##..#.
        total_valid = []
        for permutation in permutations:
            temp_input = input
            for i in range(len(permutation)):
                temp_input = temp_input.replace("?", permutation[i], 1)
            if is_valid_solution((temp_input, problem[1])):
                if len(total_valid) == 0:
                    print(
                        f"Input: {input} - Expected: {problem[1]} - First valid: {temp_input}"
                    )
                total_valid.append(temp_input)

        total_valid_permutations.append(total_valid)
    return total_valid_permutations


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    problems = [
        (line.split(" ")[0], [int(x) for x in line.split(" ")[1].split(",")])
        for line in input.splitlines()
    ]
    results = fill_all_required(problems)
    print(results)
    return sum([len(x) for x in results])


def solve_second(input: str):
    problems = [
        (line.split(" ")[0]*5, [int(x) for x in line.split(" ")[1].split(",")]*5)
        for line in input.splitlines()
    ]
    results = fill_all_required(problems)
    print(results)
    # expanded = [x[1] * 5 for x in problems]
    # valids = []
    # for i, result in enumerate(results):
    #     valid_results = 0
    #     new_results = itertools.combinations_with_replacement(result, 5)
    #     for comb in new_results:
    #         new_input = "".join(comb)
    #         if is_valid_solution((new_input, expanded[i])):
    #             if (valid_results == 0):
    #                 print(
    #                     f"Input: {problems[i][0]} - Expected: {expanded[i]} - First valid: {new_input}"
    #                 )
    #             valid_results += 1
    #     valids.append(valid_results)
    # print(valids)
    return 0


