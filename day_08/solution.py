import time
from math import lcm

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    instructions = input.splitlines()[0]
    lines = input.splitlines()[2:]
    paths = [(x.split(' = ')[0], x.split(' = ')[1].split(', ')[0].replace('(', ''), x.split(' = ')[1].split(', ')[1].replace(')', '')) for x in lines]
    current_node = 'AAA'
    i = 0
    while not current_node == 'ZZZ':
        instruction = instructions[i%len(instructions)]
        # path where 0 is current node
        path = [x for x in paths if x[0] == current_node][0]
        if instruction == 'L':
            current_node = path[1]
        elif instruction == 'R':
            current_node = path[2]
        i += 1
    return i

def all_nodes_end_with_Z(current_nodes):
    for node in current_nodes:
        if not node.endswith('Z'):
            return False
    return True
    
        
def solve_second(input: str):
    start_time = time.time()
    instructions = input.splitlines()[0]
    lines = input.splitlines()[2:]
    paths = [(x.split(' = ')[0], x.split(' = ')[1].split(', ')[0].replace('(', ''), x.split(' = ')[1].split(', ')[1].replace(')', '')) for x in lines]
    # currrent nodes are all nodes that end with A
    current_nodes = [x[0] for x in paths if x[0].endswith('A')]
    node_cycles = []
    for j, current_node in enumerate(current_nodes):
        cycles = []
        initial_solution = ''
        for i in range(0, 100000):
            instruction = instructions[i%len(instructions)]
            # path where 0 is current node
            path = [x for x in paths if x[0] == current_node][0]
            if instruction == 'L':
                current_node = path[1]
            elif instruction == 'R':
                current_node = path[2]
            if current_node.endswith('Z'):
                cycles.append(i+1)
                if initial_solution == '':
                    initial_solution = current_node
                elif initial_solution == current_node:
                    initial_solution = ''
                    break
        node_cycles.append(cycles)
    
    # get the first of each cycle
    node_cycles = [x[0] for x in node_cycles]
    # the the lcm of all of those cycles
    lcm_result = lcm(*node_cycles)
    print(lcm_result)

    
def solve_second_brute(input: str):
    start_time = time.time()
    instructions = input.splitlines()[0]
    lines = input.splitlines()[2:]
    paths = [(x.split(' = ')[0], x.split(' = ')[1].split(', ')[0].replace('(', ''), x.split(' = ')[1].split(', ')[1].replace(')', '')) for x in lines]
    # currrent nodes are all nodes that end with A
    current_nodes = [x[0] for x in paths if x[0].endswith('A')]
    i = 0
    
    
    while not all_nodes_end_with_Z(current_nodes):
        for j, current_node in enumerate(current_nodes):
            instruction = instructions[i%len(instructions)]
            # path where 0 is current node
            path = [x for x in paths if x[0] == current_node][0]
            if instruction == 'L':
                current_nodes[j] = path[1]
            elif instruction == 'R':
                current_nodes[j] = path[2]
        if i % 10000 == 0:
            print(i, current_nodes, time.time() - start_time)
        i += 1
    return i