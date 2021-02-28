PREAMBLE_LENGTH = 25

def find_invalid(numbers):
    def is_valid(preamble, number):
        for candidate in set(preamble):
            if number - candidate in preamble and number != 2 * candidate:
                return True
        return False

    for i, number in enumerate(numbers[PREAMBLE_LENGTH:]):
        if not is_valid(numbers[i:i+PREAMBLE_LENGTH], number):
            return number

def find_contiguous_range(numbers, goal_number):
    running_sum = 0

    # map of sum(numbers[0:i]) -> i for all i 
    sub_sums = {running_sum: -1}

    for i, number in enumerate(numbers):
        running_sum += number
        diff = running_sum - goal_number
        if diff in sub_sums:
            start = sub_sums[diff] + 1
            end = i + 1
            return numbers[start:end]
        sub_sums[running_sum] = i
    
    return None


if __name__ == '__main__':
    with open('input.txt') as f:
        numbers = [int(line) for line in f]
    
    invalid_number = find_invalid(numbers)
    print(invalid_number)

    contig_range = find_contiguous_range(numbers, invalid_number)
    if contig_range:
        print(min(contig_range) + max(contig_range))
    
