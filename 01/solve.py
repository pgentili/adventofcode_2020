def get_entries(vals, target):
    seen = set()
    for val in vals:
        if target - val in seen:
            return (val, target - val)
        seen.add(val)
    return None

if __name__ == '__main__':
    with open('input') as f:
        lines = f.readlines()
        vals = [int(line.strip()) for line in lines] 

    # Part 1
    entries = get_entries(vals, 2020)
    if entries:
        print(entries[0] * entries[1])
    
    # Part 2
    for i, val in enumerate(vals):
        entries = get_entries(vals[:i] + vals[i+1:], 2020 - val)
        if entries:
            print(val * entries[0] * entries[1])
            break
    
