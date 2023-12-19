import time
from colorama import Fore, Back, Style
import itertools
from heapq import heappush, heappop
import json


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    workflows = dict()
    for line in input.split('\n'):
        if line == '':
            break
        label = line.split('{')[0]
        rules = line.split('{')[1].split('}')[0].split(',')
        
        for rule in rules:
            rule = rule.strip()
            if len(rule.split(':')) == 2:
                condition_part = rule.split(':')[0][0]
                condition_op = rule.split(':')[0][1]
                condition_value = int(rule.split(':')[0][2:])
                result_part = rule.split(':')[1]
                if label not in workflows:
                    workflows[label] = []
                workflows[label].append((condition_part, condition_op, condition_value, result_part))
            else:
                result_part = rule.split(':')[0]
                if label not in workflows:
                    workflows[label] = []
                workflows[label].append((None, None, None, result_part))
    for key, value in workflows.items():
        print(key, value)
    
    processing = False
    parts = []
    for line in input.split('\n'):
        if line == '':
            processing = True
            continue
        if not processing:
            continue
        # read line as json
        line = line[1:-1]
        attributes = line.split(',')
        part = dict()
        for attribute in attributes:
            attribute = attribute.strip()
            content = attribute.split('=')
            part[content[0]] = int(content[1])
        parts.append(part)
        
    for part in parts:
        accepted = walk_workflow(workflows['in'], workflows, part, ['in'])
        if accepted:
            for key, value in part.items():
                total += value
    return total

def walk_workflow(workflow, workflows, part, visited_workflows) -> bool:
    result = None
    for i in workflow:
        if i[0] is None:
            result = i[3]
            break
        if i[1] == '<':
            if part[i[0]] < i[2]:
                result = i[3]
                break
            continue
        elif i[1] == '>':
            if part[i[0]] > i[2]:
                result = i[3]
                break
            continue
    if result is None:
        return False
    if result == 'A':
        print('Accepted: ', part, visited_workflows)
        return True
    if result == 'R':
        print('Rejected: ', part, visited_workflows)
        return False
    if result in visited_workflows:
        return False
    return walk_workflow(workflows[result], workflows, part, visited_workflows + [result])
    

def solve_second(input: str):
    total = 0
    workflows = dict()
    for line in input.split('\n'):
        if line == '':
            break
        label = line.split('{')[0]
        rules = line.split('{')[1].split('}')[0].split(',')
        
        for rule in rules:
            rule = rule.strip()
            if len(rule.split(':')) == 2:
                condition_part = rule.split(':')[0][0]
                condition_op = rule.split(':')[0][1]
                condition_value = int(rule.split(':')[0][2:])
                result_part = rule.split(':')[1]
                if label not in workflows:
                    workflows[label] = []
                workflows[label].append((condition_part, condition_op, condition_value, result_part))
            else:
                result_part = rule.split(':')[0]
                if label not in workflows:
                    workflows[label] = []
                workflows[label].append((None, None, None, result_part))
    for key, value in workflows.items():
        print(key, value)
        
    # find the boundaries for each part that endup in one workflow with A
    boundaries = []
    workflows_to_check = [
        {
            'key': 'in',
            'x': (1, 4000),
            'm': (1, 4000),
            'a': (1, 4000),
            's': (1, 4000),
            'path': ['in']
        }
    ]
    valid_boundaries = []
    workflows_visited = set()
    workflows_visited.add('in')
    while len(workflows_to_check) > 0:
        boundary = workflows_to_check.pop()
        if boundary['key'] == 'A':
            valid_boundaries.append(boundary)
            continue
        if boundary['key'] in 'R':
            continue
        rules = workflows[boundary['key']]
        for rule in rules:
            if rule[0] is None and rule[3] == 'A':
                print('Found A', boundary)
                valid_boundaries.append(boundary)
                continue
            if rule[0] is None and rule[3] == 'R':
                print('Found R', boundary)
                continue
            if rule[0] is None:
                boundary['key'] = rule[3]
                workflows_to_check.append(boundary)
                continue
            if rule[0] in boundary:
                if rule[1] == '<':
                    if boundary[rule[0]][0] < rule[2]:
                        new_check = boundary.copy()
                        new_check[rule[0]] = (boundary[rule[0]][0], rule[2]-1)
                        new_check['key'] = rule[3]
                        workflows_to_check.append(new_check)
                        workflows_visited.add(rule[3])
                    boundary[rule[0]] = (rule[2], boundary[rule[0]][1])
                    continue
                elif rule[1] == '>':
                    if boundary[rule[0]][1] > rule[2]:
                        new_check = boundary.copy()
                        new_check[rule[0]] = (rule[2]+1, boundary[rule[0]][1])
                        new_check['key'] = rule[3]
                        workflows_to_check.append(new_check)
                        workflows_visited.add(rule[3])
                    boundary[rule[0]] = (boundary[rule[0]][0], rule[2])
                    continue
    for boundary in valid_boundaries:
        x = boundary['x'][1] - boundary['x'][0] + 1
        m = boundary['m'][1] - boundary['m'][0] + 1
        a = boundary['a'][1] - boundary['a'][0] + 1
        s = boundary['s'][1] - boundary['s'][0] + 1
        print(f"x: {boundary['x']} m: {boundary['m']} a: {boundary['a']} s: {boundary['s']} = {x * m * a * s}")
        total += x * m * a * s
    
    return total
