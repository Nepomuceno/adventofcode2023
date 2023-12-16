import time
from colorama import Fore, Back, Style
import itertools


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    codes = input.split(',')
    for code in codes:
        result = 0
        for i in range(0, len(code)):
            value = ord(code[i]) + result
            value = value * 17
            value = value % 256
            result = value
        print(f'{code} -> {result}')
        total += result
    return total

def solve_second(input: str):
    # genretate the array of 256 boxes
    total = 0
    boxes = []
    for i in range(0, 256):
        boxes.append([])
    codes = input.split(',')
    for code in codes:
        result = 0
        if code.find('=') != -1:
            result = int(code.split('=')[1])
            label = code.split('=')[0]
            hash = get_hash(label)
            found_box = False
            for box in boxes[hash]:
                if box['label'] == label:
                    found_box = True
                    box['focal'] = result
                    break
            if not found_box:
                boxes[hash].append({
                    'label': label,
                    'focal': int(code.split('=')[1])
                })
            
        else:
            label = code.split('-')[0]
            hash = get_hash(label)
            # remove the registry from the box
            for box in boxes[hash]:
                if box['label'] == label:
                    boxes[hash].remove(box)
                    break
                
            
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            value = (1 + i) * (1 + j) * lens['focal']
            print(f'{i} {j} {lens} {value}')
            total += value
            
    return total

def get_hash(code):
    result = 0
    for i in range(0, len(code)):
        value = ord(code[i]) + result
        value = value * 17
        value = value % 256
        result = value
    return result
    

# > 95985