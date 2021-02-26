import numpy as np

def encounter_trees(map, slope=(1, 3)):
    trees = 0
    curr_loc = (0, 0)
    map_shape = (len(map), len(map[0]))

    while curr_loc[0] + slope[0] < map_shape[0]:
        curr_loc = (curr_loc[0] + slope[0], (curr_loc[1] + slope[1]) % map_shape[1])
        if map[curr_loc[0]][curr_loc[1]]  == '#':
            trees += 1

    return trees

    

if __name__ == '__main__':
    with open('input.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    print(encounter_trees(lines))

    trees_found = []
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        trees_found.append(encounter_trees(lines, slope))
    total_trees = 1
    for trees in trees_found:
        total_trees *= trees
    print(total_trees)