inputFileName = 'input'

accumulator = 0
with open(f'./{inputFileName}','r') as fh:
    instructions = fh.readlines()
    instructions = [ i.strip().split(' ') for i in instructions]

    pathTaken = set()
    offset = 0
    while True:
        if offset in pathTaken:
            break
        pathTaken.add(offset)

        op, arg = instructions[offset]
        arg = int(arg)
        if op == 'acc':
            accumulator += arg 
            offset += 1
        elif op == 'jmp':
            offset += arg
        elif op == 'nop':
            offset += 1

    print(f'accumulator: {accumulator} offset: {offset}')
