import re

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    
    total = 0
    lines = input.splitlines()
    seeds = [int(x) for x in lines[0].split(': ')[1].split(' ')]
    lines = lines[2:]
    transformers = []
    transformer = {
        "from": "",
        "to": "",
        "cordinates": []
    }
    for line in lines:
        if line == '':
            transformers.append(transformer)
            transformer = {
                "from": "",
                "to": "",
                "cordinates": []
            }
            continue
        if line.endswith("map:"):
            text = line.split(' ')[0]
            transformer['from'] = text.split('-to-')[0]
            transformer['to'] = text.split('-to-')[1]
        else:
            transformer['cordinates'].append([int(x) for x in line.split(' ')])
    transformers.append(transformer)
    print(transformers)
    locations = []
    for seed in seeds:
        current = seed
        for transformer in transformers:
            for cordinate in transformer['cordinates']:
                if current >= cordinate[1] and current < cordinate[1] + cordinate[2]:
                    current = cordinate[0] + (current - cordinate[1])
                    break
            print(transformer['from'], transformer['to'], current)
        print("------")
        locations.append(current)
        
    return min(locations)
        
def solve_second(input: str):
    lines = input.splitlines()
    seed_ranges = [int(x) for x in lines[0].split(': ')[1].split(' ')]
    # grop every 2 seeds
    seed_range = []
    for i in range(0, len(seed_ranges), 2):
        seed_range.append([seed_ranges[i], seed_ranges[i+1]])

    lines = lines[2:]
    transformers = []
    transformer = {
        "from": "",
        "to": "",
        "cordinates": []
    }
    for line in lines:
        if line == '':
            transformers.append(transformer)
            transformer = {
                "from": "",
                "to": "",
                "cordinates": []
            }
            continue
        if line.endswith("map:"):
            text = line.split(' ')[0]
            transformer['from'] = text.split('-to-')[0]
            transformer['to'] = text.split('-to-')[1]
        else:
            transformer['cordinates'].append([int(x) for x in line.split(' ')])
    transformers.append(transformer)
    # sort coordinates by index 1
    for transformer in transformers:
        transformer['cordinates'] = sorted(transformer['cordinates'], key=lambda x: x[1])
    
    print(transformers)
    min_locations = []

    for seed_r in seed_range:
        current = [seed_r]
        for transformer in transformers:
            current = process_range(current, transformer)
        min_seed = min(current, key=lambda x: x[0])[0]
        print(min_seed)
        min_locations.append(min_seed)
    
    return min(min_locations)


def process_range(source_ranges, transformer):
    ranges = []
    for source_range in source_ranges:
        i = source_range[0]
        while i < source_range[0]+source_range[1]:
            for cordinate in transformer['cordinates']:
                if i >= cordinate[1] and i < cordinate[1] + cordinate[2]:
                    length_range = (i-cordinate[1])
                    max_number = min(cordinate[2] - length_range, source_range[0]+source_range[1]-i)
                    ranges.append([cordinate[0]+length_range, max_number])
                    i = i + max_number
            if(i < source_range[0]+source_range[1]):
                length = max(source_range[0]+source_range[1]-i, 1)
                ranges.append([i, length])
                i = i + length
    return ranges
    