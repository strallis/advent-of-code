from aocd import data
import re

def parser():
    stack, instructions = data.split('\n\n')

    instructions = instructions.split('\n')
    stacks = {}

    stack = stack.split('\n')
    stack.reverse()


    for index, ele in enumerate(stack[0]):
        if ele.isdigit():
            _tmp = []
            for i in stack[0:]:
                if i[index].isalpha():
                    _tmp.append(i[index])
            stacks[ele] = _tmp
        else:
            pass
    return stacks, instructions

def part1(stacks, instructions):
    for instruction in instructions:
        amount, from_int, to_int = re.findall(r'\b\d+\b',instruction)
        amount = int(amount)
        while amount > 0:
            ele = stacks[from_int].pop()
            stacks[to_int].append(ele)
            amount -= 1
    return stacks

def part2(stacks, instructions):
    for instruction in instructions:
        amount, from_int, to_int = re.findall(r'\b\d+\b',instruction)
        amount = int(amount)
        while amount > 0:
            ele = stacks[from_int].pop(-amount)
            stacks[to_int].append(ele)
            amount -= 1
    return stacks

def answer(stacks):
    answer = ''
    for stack in stacks.values():
        answer += stack[-1]
    print(answer)

def main():
    stacks, instructions = parser()
    #stacks = part1(stacks, instructions)
    stacks = part2(stacks, instructions)
    answer(stacks)

if __name__ == '__main__':
    main()