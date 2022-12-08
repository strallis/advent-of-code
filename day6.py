from aocd import data


def part1(data):
    index = 4
    marker = list(data[:index])
    for i in data[index:]:
        if i not in marker and len(marker) == len(set(marker)):
            return index
        else:
            marker.pop(0)
            marker.append(i)
            index += 1


def part2(data):
    index = 14
    marker = list(data[:index])
    for i in data[index:]:
        if len(marker) == len(set(marker)):
            return index
        else:
            marker.pop(0)
            marker.append(i)
            index += 1


def main():
    ans1 = part1(data)
    ans2 = part2(data)
    print(f"part 1: {ans1} - part 2: {ans2}")


if __name__ == "__main__":
    main()
