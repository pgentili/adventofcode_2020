def parse_instructions(inst_lines):
    insts = []
    for line in inst_lines:
        op, arg = line.split(' ')
        insts.append((op, int(arg)))
    return insts

def run_until_loop_or_terminate(insts):
    accumulator = 0
    inst_num = 0
    ran = [False] * len(insts)

    while inst_num < len(insts):
        if ran[inst_num]:
            return False, accumulator
        ran[inst_num] = True

        op, arg = insts[inst_num]
        if op == 'nop':
            inst_num += 1
        elif op == 'acc':
            accumulator += arg
            inst_num += 1
        elif op == 'jmp':
            inst_num += arg
        else:
            raise Exception(f'Invalid operation found in instruction {inst_num}')
    
    return inst_num == len(insts), accumulator

def fix_instructions(insts):
    for i, (op, arg) in enumerate(insts):
        if op == 'acc':
            continue
        elif op == 'jmp':
            try_op = 'nop'
        elif op == 'nop':
            try_op = 'jmp'
        else:
            raise Exception(f'Invalid operation found while trying to fix instructions: {op}')

        try_insts = insts[:i] + [(try_op, arg)] + insts[i+1:]
        success, accumulator = run_until_loop_or_terminate(try_insts)
        if success:
            return accumulator

    raise Exception('Could not fix instructions')


if __name__ == '__main__':
    with open('input.txt') as f:
        inst_lines= f.read().splitlines()
    broken_insts = parse_instructions(inst_lines)
    print(run_until_loop_or_terminate(broken_insts)[1])
    print(fix_instructions(broken_insts))