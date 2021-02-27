import re
from functools import reduce

def get_num_answers(group_block):
    return len(set(re.sub(r'[ \n]', '', group_block)))

def get_num_common_answers(group_block):
    all_answers = [set(single_response) for single_response in group_block.splitlines()]
    return len(reduce(set.intersection, all_answers))

if __name__ == '__main__':
    with open('input.txt') as f:
        groups = f.read().rstrip('\n').split('\n\n')
    
    print(sum(get_num_answers(group) for group in groups))
    print(sum(get_num_common_answers(group) for group in groups))