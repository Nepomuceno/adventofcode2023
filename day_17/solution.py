import time
from colorama import Fore, Back, Style
import itertools
from heapq import heappush, heappop

def is_viable_path(map, path, paths):
    destination = path['position']
    
    if len(path['path']) < 4:
        return True
    if path['position'] in path['visited']:
        return False
    if path['path'][-1]['position'][0] < path['path'][-2]['position'][0]:
        if path['path'][-2]['position'][0] < path['path'][-3]['position'][0]:
            if path['path'][-3]['position'][0] < path['path'][-4]['position'][0]:
                return False
    if path['path'][-1]['position'][0] > path['path'][-2]['position'][0]:
        if path['path'][-2]['position'][0] > path['path'][-3]['position'][0]:
            if path['path'][-3]['position'][0] > path['path'][-4]['position'][0]:
                return False
    if path['path'][-1]['position'][1] < path['path'][-2]['position'][1]:
        if path['path'][-2]['position'][1] < path['path'][-3]['position'][1]:
            if path['path'][-3]['position'][1] < path['path'][-4]['position'][1]:
                return False
    if path['path'][-1]['position'][1] > path['path'][-2]['position'][1]:
        if path['path'][-2]['position'][1] > path['path'][-3]['position'][1]:
            if path['path'][-3]['position'][1] > path['path'][-4]['position'][1]:
                return False
    # check if there is a path in all the paths that cot to this destination with a lower score
    return True
    
        

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    
    grid = [[int(char) for char in line] for line in input.split('\n')]

    total = 0
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]
    while pq:
        heat_loss, row, col, dt_row, dt_col, n = heappop(pq)
        
        if (row, col, dt_row, dt_col, n) in seen:
            continue
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1:
            total = heat_loss
            break
        
        seen.add((row, col, dt_row, dt_col, n))
        
        if n < 3 and (dt_row, dt_col) != (0, 0):
            new_row = row + dt_row
            new_col = col + dt_col
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]): 
                heappush(pq, (heat_loss + grid[new_row][new_col], new_row, new_col, dt_row, dt_col, n + 1))

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            if direction[0] == dt_row and direction[1] == dt_col:
                continue
            if direction[0] == -dt_row and direction[1] == -dt_col:
                continue
            heappush(pq, (heat_loss + grid[new_row][new_col], new_row, new_col, direction[0], direction[1], 1))

    return total


def solve_second(input: str):
    grid = [[int(char) for char in line] for line in input.split('\n')]

    total = 0
    seen = set()
    pq = [(0, 0, 0, 0, 0, 0)]
    while pq:
        heat_loss, row, col, dt_row, dt_col, n = heappop(pq)
        
        if (row, col, dt_row, dt_col, n) in seen:
            continue
        
        if row == len(grid) - 1 and col == len(grid[0]) - 1 and n >= 4:
            total = heat_loss
            break
        
        seen.add((row, col, dt_row, dt_col, n))
        
        if n < 10 and (dt_row, dt_col) != (0, 0):
            new_row = row + dt_row
            new_col = col + dt_col
            if new_row >= 0 and new_row < len(grid) and new_col >= 0 and new_col < len(grid[0]): 
                heappush(pq, (heat_loss + grid[new_row][new_col], new_row, new_col, dt_row, dt_col, n + 1))
        directions = []
        if n >= 4 or (dt_row, dt_col) == (0, 0):
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        for direction in directions:
            new_row = row + direction[0]
            new_col = col + direction[1]
            if new_row < 0 or new_row >= len(grid) or new_col < 0 or new_col >= len(grid[0]):
                continue
            if direction[0] == dt_row and direction[1] == dt_col:
                continue
            if direction[0] == -dt_row and direction[1] == -dt_col:
                continue
            heappush(pq, (heat_loss + grid[new_row][new_col], new_row, new_col, direction[0], direction[1], 1))

    return total

