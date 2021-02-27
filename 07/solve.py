import re

def parse_rules(rules):
    regex = re.compile(r'^([a-z ]*[a-z]) bags? contain (.* bags?).\n$')

    bag_rules = {}
    for rule in rules:
        result = regex.fullmatch(rule)
        parent_bag, child_block = result.groups()

        assert(parent_bag not in bag_rules)

        if child_block == 'no other bags':
            bag_rules[parent_bag] = {}
        else:
            child_bag_descs = child_block.split(', ')

            child_bags = {}
            for child_bag_desc in child_bag_descs:
                tokens = child_bag_desc.split(' ')
                bag_count = int(tokens[0])
                bag_name = ' '.join(tokens[1:3])
                child_bags[bag_name] = bag_count

            bag_rules[parent_bag] = child_bags

    return bag_rules

def is_suitable_bag(bag_rules, start_bag, goal_bag):
    unexplored = set([start_bag])
    explored = set()

    while unexplored:
        new_unexplored = set()
        for unexplored_bag in unexplored:
            children = bag_rules[unexplored_bag].keys()
            for child in children:
                if child not in unexplored and child not in explored:
                    new_unexplored.add(child)
            explored.add(unexplored_bag)
        unexplored = new_unexplored

        if goal_bag in unexplored:
            return True

    return False

def num_bags_inside(bag_rules, bag):
    total_count = 0
    if bag_rules[bag]:
        print(bag, bag_rules[bag])

    for child_bag, child_count in bag_rules[bag].items():
        print(child_bag, child_count, num_bags_inside(bag_rules, child_bag))
        total_count += child_count * (1 + num_bags_inside(bag_rules, child_bag))
    
    return total_count


if __name__ == '__main__':
    with open('input.txt') as f:
        rules = f.readlines()

    rules = parse_rules(rules)
    print(sum(is_suitable_bag(rules, start_bag, 'shiny gold') for start_bag in rules))
    print(num_bags_inside(rules, 'shiny gold'))