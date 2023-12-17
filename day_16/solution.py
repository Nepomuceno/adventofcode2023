import time
from colorama import Fore, Back, Style
import itertools


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    map = [[char for char in line] for line in input.split('\n')]
    beans = [{'position': (-1,0), 'direction': 'r'}]
    total = find_energized(map, beans)
    return total

def find_energized(map, beans):
    previsous_done = set()
    energized_tiles = set()
    i = 0
    while len(beans) > 0:
        i += 1
        # print(f'Iteration {i}, beans: {len(beans)}, energized tiles: {len(energized_tiles)}')
        for bean in beans:
            if (bean['position'][0],bean['position'][1],bean['direction']) in previsous_done:
                beans.remove(bean)
                continue
            previsous_done.add((bean['position'][0],bean['position'][1],bean['direction']))
            if bean['direction'] == 'r':
                target = (bean['position'][0] + 1, bean['position'][1])
                # if the target is outside the map, remove the bean
                if target[0] >= len(map[0]):
                    beans.remove(bean)
                    continue
                bean['position'] = target
                energized_tiles.add(target)
                if map[target[1]][target[0]] == '/':
                    bean['direction'] = 'u'
                elif map[target[1]][target[0]] == '\\':
                    bean['direction'] = 'd'
                elif map[target[1]][target[0]] == '|':
                    bean['direction'] = 'u'
                    beans.append({'position': target, 'direction': 'd'})
                continue
            if bean['direction'] == 'l':
                target = (bean['position'][0] - 1, bean['position'][1])
                # if the target is outside the map, remove the bean
                if target[0] < 0:
                    beans.remove(bean)
                    continue
                bean['position'] = target
                energized_tiles.add(target)
                if map[target[1]][target[0]] == '/':
                    bean['direction'] = 'd'
                elif map[target[1]][target[0]] == '\\':
                    bean['direction'] = 'u'
                elif map[target[1]][target[0]] == '|':
                    bean['direction'] = 'd'
                    beans.append({'position': target, 'direction': 'u'})
                continue
            if bean['direction'] == 'u':
                target = (bean['position'][0], bean['position'][1] - 1)
                # if the target is outside the map, remove the bean
                if target[1] < 0:
                    beans.remove(bean)
                    continue
                bean['position'] = target
                energized_tiles.add(target)
                if map[target[1]][target[0]] == '/':
                    bean['direction'] = 'r'
                elif map[target[1]][target[0]] == '\\':
                    bean['direction'] = 'l'
                elif map[target[1]][target[0]] == '-':
                    bean['direction'] = 'l'
                    beans.append({'position': target, 'direction': 'r'})
                continue
            if bean['direction'] == 'd':
                target = (bean['position'][0], bean['position'][1] + 1)
                # if the target is outside the map, remove the bean
                if target[1] >= len(map):
                    beans.remove(bean)
                    continue
                bean['position'] = target
                energized_tiles.add(target)
                if map[target[1]][target[0]] == '/':
                    bean['direction'] = 'l'
                elif map[target[1]][target[0]] == '\\':
                    bean['direction'] = 'r'
                elif map[target[1]][target[0]] == '-':
                    bean['direction'] = 'r'
                    beans.append({'position': target, 'direction': 'l'})
                continue
    return len(energized_tiles)

def solve_second(input: str):
    # genretate the array of 256 boxes
    max = 0
    map = [[char for char in line] for line in input.split('\n')]
    
    for i in range(len(map)):
        beans = [{'position': (-1,i), 'direction': 'r'}]
        total = find_energized(map, beans)
        print(f'(-1,{i}) -> {total}')
        if total > max:
            max = total
        beans = [{'position': (len(map[0]),i), 'direction': 'l'}]
        total = find_energized(map, beans)
        print(f'({len(map[0])},{i}) -> {total}')
        if total > max:
            max = total
    for i in range(len(map[0])):
        beans = [{'position': (i,-1), 'direction': 'd'}]
        total = find_energized(map, beans)
        print(f'({i},-1) -> {total}')
        if total > max:
            max = total
        beans = [{'position': (i,len(map)), 'direction': 'u'}]
        total = find_energized(map, beans)
        print(f'({i},{len(map)}) -> {total}')
        if total > max:
            max = total
    return max

