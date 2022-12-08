from aocd import lines  # type: ignore


def part1():
    sum_priority = 0
    for line in lines:
        i = int(len(line) / 2)
        l1 = line[:i]
        l2 = line[i:]
        dup = "".join(set([x for x in l1 if x in l2]))
        sum_priority += get_priority(dup)
    print(sum_priority)


def part2():
    sum_priority = 0
    for group in range(0, len(lines), 3):
        dup1 = "".join(set([x for x in lines[group] if x in lines[group + 1]]))
        dup2 = "".join(set([x for x in dup1 if x in lines[group + 2]]))
        sum_priority += get_priority(dup2)
    print(sum_priority)


def get_priority(c):
    return ord(c) - ord("a") + 1 if c.islower() else ord(c) - ord("A") + 27


def main():
    part1()
    part2()


if __name__ == "__main__":
    main()
