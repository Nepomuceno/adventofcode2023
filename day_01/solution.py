def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    for line in input.splitlines():
        # remove non-digits
        line = ''.join(filter(str.isdigit, line))
        line = ''.join([line[0],line[-1]])
        total += int(line)
    return total
        
def solve_second(input: str):
    total = 0
    for line in input.splitlines():
        line = line.replace('eightwo', '82')
        line = line.replace('oneight', '18')
        line = line.replace('threeight', '38')
        line = line.replace('fiveight', '58')
        line = line.replace('sevenine', '79')
        line = line.replace('twone', '21')
        line = line.replace('one', '1')
        line = line.replace('two', '2')
        line = line.replace('three', '3')
        line = line.replace('four', '4')
        line = line.replace('five', '5')
        line = line.replace('six', '6')
        line = line.replace('seven', '7')
        line = line.replace('eight', '8')
        line = line.replace('nine', '9')
        # remove non-digits
        line = ''.join(filter(str.isdigit, line))
        line = ''.join([line[0],line[-1]])
        total += int(line)
    return total