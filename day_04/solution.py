import re

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    
    total = 0
    for line in input.splitlines():
        game = line.split(':')[0].split(' ')[1]
        numbers = line.split(':')[1].split('|')
        bet = numbers[0].split(' ')
        results = numbers[1].split(' ')
        # remove '' from results and bet
        results = [x for x in results if x != '']
        bet = [x for x in bet if x != '']
        # check how many numbers are correct in any p§
        correct = 0
        for i in range(len(bet)):
            for j in range(len(results)):
                if bet[i] == results[j]:
                    correct += 1
                    break
        total += int(2 ** (correct-1))
    return total
        
def solve_second(input: str):
    total = 0
    lines = input.splitlines()
    multipliers = [1] * len(lines)
    for k, line in enumerate(lines):
        game = line.split(':')[0].split(' ')[1]
        numbers = line.split(':')[1].split('|')
        bet = numbers[0].split(' ')
        results = numbers[1].split(' ')
        results = [x for x in results if x != '']
        bet = [x for x in bet if x != '']
        correct = 0
        for i in range(len(bet)):
            for j in range(len(results)):
                if bet[i] == results[j]:
                    correct += 1
                    break
        
        for i in range(correct):
            multipliers[k+i+1] += 1*multipliers[k]
    total = sum(multipliers)
            
    return total