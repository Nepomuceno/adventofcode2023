import re
import functools

def letter_to_number(letter: str) -> int:
    if letter == 'T':
        return 10
    if letter == 'J':
        return 11
    if letter == 'Q':
        return 12
    if letter == 'K':
        return 13
    if letter == 'A':
        return 14
    return int(letter)

def letter_to_number_2(letter: str) -> int:
    if letter == 'T':
        return 10
    if letter == 'J':
        return 1
    if letter == 'Q':
        return 12
    if letter == 'K':
        return 13
    if letter == 'A':
        return 14
    return int(letter)
   
    
    

def get_score(hand: str) -> int:
    
    hand_sortes = sorted(hand, key=lambda x: letter_to_number(x), reverse=True)
    print(hand_sortes)
    # five of a kind
    if len(set(hand_sortes)) == 1:
        return 100_000_000_000_000_000_000_000_000_000_000_000 * letter_to_number(hand_sortes[0])
    # four of a kind
    if len(set(hand_sortes)) == 2 and hand_sortes.count(hand_sortes[0]) == 4:
        return 100_000_000_000_000_000_000_000_000_000_000 * letter_to_number(hand_sortes[0])
    if len(set(hand_sortes)) == 2 and hand_sortes.count(hand_sortes[0]) == 1:
        return 100_000_000_000_000_000_000_000_000_000_000 * letter_to_number(hand_sortes[4])
    # full house
    if len(set(hand_sortes)) == 2:
        return 100_000_000_000_000_000_000_000_000_000 * letter_to_number(hand_sortes[2]) + 100_000_000_000_000_000_000_000_000 * letter_to_number(hand_sortes[0])
    # three of a kind
    if len(set(hand_sortes)) == 3 and hand_sortes.count(hand_sortes[0]) == 3:
        return 100_000_000_000_000 * letter_to_number(hand_sortes[0])
    if len(set(hand_sortes)) == 3 and hand_sortes.count(hand_sortes[0]) == 1:
        return 100_000_000_000_000 * letter_to_number(hand_sortes[4])
    # two pairs
    if len(set(hand_sortes)) == 3:
        return 100_000_000_000 * letter_to_number(hand_sortes[3]) + 100_000_000 * letter_to_number(hand_sortes[1])
    # one pair
    if len(set(hand_sortes)) == 4:
        # which one is the pair?
        if hand_sortes.count(hand_sortes[0]) == 2:
            return 100_000_000 * letter_to_number(hand_sortes[0])
        if hand_sortes.count(hand_sortes[1]) == 2:
            return 100_000_000 * letter_to_number(hand_sortes[1])
        if hand_sortes.count(hand_sortes[2]) == 2:
            return 100_000_000 * letter_to_number(hand_sortes[2])
        if hand_sortes.count(hand_sortes[3]) == 2:
            return 100_000_000 * letter_to_number(hand_sortes[3])
        if hand_sortes.count(hand_sortes[4]) == 2:
            return 100_000_000 * letter_to_number(hand_sortes[4])
    # high card
    return letter_to_number(hand_sortes[0])

def compare_equalhands(hand1: str, hand2: str) -> int:
    for i in range(5):
        if letter_to_number(hand1[i]) > letter_to_number(hand2[i]):
            return 1
        if letter_to_number(hand1[i]) < letter_to_number(hand2[i]):
            return -1
    return 0

def compare_equalhands_2(hand1: str, hand2: str) -> int:
    for i in range(5):
        if letter_to_number_2(hand1[i]) > letter_to_number_2(hand2[i]):
            return 1
        if letter_to_number_2(hand1[i]) < letter_to_number_2(hand2[i]):
            return -1
    return 0

def compare_hands(hand1: tuple[str,int], hand2: tuple[str,int]) -> int:
    a = hand1[0]
    sa = sorted(a, key=lambda x: letter_to_number(x), reverse=True)
    b = hand2[0]
    sb = sorted(b, key=lambda x: letter_to_number(x), reverse=True)
    # five of a kind
    if len(set(sa)) == 1 and len(set(sb)) == 1:
        return compare_equalhands(a, b)
    if len(set(sa)) == 1:
        return 1
    if len(set(sb)) == 1:
        return -1
    # four of a kind
    if len(set(sa)) == 2 and sa.count(sa[1]) == 4 and len(set(sb)) == 2 and sb.count(sb[1]) == 4:
        return compare_equalhands(a, b)
    if len(set(sa)) == 2 and sa.count(sa[1]) == 4:
        return 1
    if len(set(sb)) == 2 and sb.count(sb[1]) == 4:
        return -1
    # full house
    if len(set(sa)) == 2 and len(set(sb)) == 2:
        return compare_equalhands(a, b)
    if len(set(sa)) == 2:
        return 1
    if len(set(sb)) == 2:
        return -1
    # three of a kind
    if len(set(sa)) == 3 and sa.count(sa[2]) == 3 and len(set(sb)) == 3 and sb.count(sb[2]) == 3:
        return compare_equalhands(a, b)
    if len(set(sa)) == 3 and sa.count(sa[2]) == 3:
        return 1
    if len(set(sb)) == 3 and sb.count(sb[2]) == 3:
        return -1
    # two pairs
    if len(set(sa)) == 3 and len(set(sb)) == 3:
        return compare_equalhands(a, b)
    if len(set(sa)) == 3:
        return 1
    if len(set(sb)) == 3:
        return -1
    # one pair
    if len(set(sa)) == 4 and len(set(sb)) == 4:
        return compare_equalhands(a, b)
    if len(set(sa)) == 4:
        return 1
    if len(set(sb)) == 4:
        return -1
    # high card
    return compare_equalhands(a, b)

def get_pretend_hand(hand: str) -> str:
    # if J is not in the hand, return the hand
    if 'J' not in hand:
        return hand
    result = hand
    letters = ['T', 'Q', 'K', 'A', '9', '8', '7', '6', '5', '4', '3', '2']
    for letter in letters:
        status = compare_hands((result,0), (hand.replace('J', letter),0))
        if status < 0:
            result = hand.replace('J', letter)
    return result

def compare_hands_2(hand1: tuple[str,int], hand2: tuple[str,int]) -> int:
    a = hand1[0]
    pha = get_pretend_hand(a)
    sa = sorted(pha, key=lambda x: letter_to_number(x), reverse=True)
    b = hand2[0]
    phb = get_pretend_hand(b)
    sb = sorted(phb, key=lambda x: letter_to_number(x), reverse=True)
    # five of a kind
    if len(set(sa)) == 1 and len(set(sb)) == 1:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 1:
        return 1
    if len(set(sb)) == 1:
        return -1
    # four of a kind
    if len(set(sa)) == 2 and sa.count(sa[1]) == 4 and len(set(sb)) == 2 and sb.count(sb[1]) == 4:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 2 and sa.count(sa[1]) == 4:
        return 1
    if len(set(sb)) == 2 and sb.count(sb[1]) == 4:
        return -1
    # full house
    if len(set(sa)) == 2 and len(set(sb)) == 2:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 2:
        return 1
    if len(set(sb)) == 2:
        return -1
    # three of a kind
    if len(set(sa)) == 3 and sa.count(sa[2]) == 3 and len(set(sb)) == 3 and sb.count(sb[2]) == 3:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 3 and sa.count(sa[2]) == 3:
        return 1
    if len(set(sb)) == 3 and sb.count(sb[2]) == 3:
        return -1
    # two pairs
    if len(set(sa)) == 3 and len(set(sb)) == 3:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 3:
        return 1
    if len(set(sb)) == 3:
        return -1
    # one pair
    if len(set(sa)) == 4 and len(set(sb)) == 4:
        return compare_equalhands_2(a, b)
    if len(set(sa)) == 4:
        return 1
    if len(set(sb)) == 4:
        return -1
    # high card
    return compare_equalhands_2(a, b)


def solve(input: str, second: bool):
    if second:
        return solve_second(input)
    total = 0
    hands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in input.splitlines()]
    hands = sorted(hands, key=functools.cmp_to_key(compare_hands))
    for i, hand in enumerate(hands):
        total += (i+1)*hand[1]
    return total
        
def solve_second(input: str):
    total = 0
    total = 0
    hands = [(x.split(' ')[0], int(x.split(' ')[1])) for x in input.splitlines()]
    hands = sorted(hands, key=functools.cmp_to_key(compare_hands_2))
    for i, hand in enumerate(hands):
        total += (i+1)*hand[1]
    return total

    