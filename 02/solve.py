def check_line_part_1(line):
    tokens = line.split(' ')

    lower, upper = tokens[0].split('-')
    lower, upper = int(lower), int(upper)

    letter = tokens[1][0]

    password = tokens[2]

    return lower <= password.count(letter) <= upper

def check_line_part_2(line):
    tokens = line.split(' ')

    first, second = tokens[0].split('-')
    first, second = int(first) - 1, int(second) - 1

    letter = tokens[1][0]

    password = tokens[2]

    return (password[first] == letter) ^ (password[second] == letter)

if __name__ == '__main__':
    for checker in [check_line_part_1, check_line_part_2]:
        valid = 0
        with open('input.txt') as f:
            for line in f:
                valid += checker(line.rstrip('\n'))
        print(valid)
