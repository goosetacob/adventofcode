inputFileName = 'input'

def checkIfTerminates(instructions):
    accumulator = 0
    pathTaken = set()
    offset = 0
    while True:
        if offset >= len(instructions):
            return True, accumulator
        if offset in pathTaken:
            return False, accumulator
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

with open(f'./{inputFileName}','r') as fh:
    instructions = fh.readlines()
    instructions = [ i.strip().split(' ') for i in instructions]

    for idx in range(0, len(instructions)):
        inst = instructions[idx]
        op, arg = inst
        if op == 'jmp' or op == 'nop':
            # flip op
            inst[0] = 'nop' if inst[0] == 'jmp' else 'jmp'
            instructions[idx] = inst

            terminates, accVal = checkIfTerminates(instructions)
            if terminates:
                print(f'accumulator {accVal} for terminating instructions')

            # flip back
            inst[0] = 'jmp' if inst[0] == 'nop' else 'nop'
            instructions[idx] = inst
