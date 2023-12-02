import re

def parse_input(input: str):
    content = input.split(':')
    game = int(content[0].split(' ')[1])
    regex = re.compile('((\d+) (green|red|blue))')
    result = {
        'game': game,
        'games': [],
    }
    games = content[1].split(';')
    for game in games:
        game_result = {
            'green': 0,
            'red': 0,
            'blue': 0,
        }
        for match in regex.finditer(game):
            x = match.group(2)
            if match.group(3) == 'green':
                game_result['green'] += int(x)
            elif match.group(3) == 'red':
                game_result['red'] += int(x)
            elif match.group(3) == 'blue':
                game_result['blue'] += int(x)
        result['games'].append(game_result)
    return result

def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    for line in input.splitlines():
        games = parse_input(line)
        # if any of the games is not a valid game, skil the whole line
        valid = True
        for game in games['games']:
            if game['red'] > 12 or game['green'] > 13 or game['blue'] > 14:
                valid = False
                break
        if valid:
            total += games['game']
    return total
        
def solve_second(input: str):
    total = 0
    for line in input.splitlines():
        games = parse_input(line)
        min_green = 0
        min_red = 0
        min_blue = 0
        for game in games['games']:
            if game['red'] > min_red:
                min_red = game['red']
            if game['green'] > min_green:
                min_green = game['green']
            if game['blue'] > min_blue:
                min_blue = game['blue']
        score = min_red * min_green * min_blue
        total += score
    return total