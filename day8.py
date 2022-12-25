from aocd import lines
import numpy as np


def parser():

    forest = np.empty([len(lines), len(lines[0])])
    for i, line in enumerate(lines):
        for j, tree in enumerate(line):
            forest[i][j] = int(tree)
    return forest


def part1(forest) -> int:
    ans1 = np.zeros(forest.shape, dtype=bool)
    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            ans1[i, j] = (
                np.all(forest[i, :j] < forest[i, j])
                or np.all(forest[i, j + 1 :] < forest[i, j])
                or np.all(forest[:i, j] < forest[i, j])
                or np.all(forest[i + 1 :, j] < forest[i, j])
            )
    return np.count_nonzero(ans1)


def part2(forest) -> int:
    ans2 = np.zeros(forest.shape, dtype=int)
    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            ans2[i][j] = get_scenic_score(forest=forest, x=i, y=j)
    return np.amax(ans2)


def get_scenic_score(forest, x, y):
    original_element = forest[x][y]
    scenic_score = 1
    count = 0

    if x == 0 or y == 0 or x == len(forest) - 1 or y == len(forest[0]) - 1:
        scenic_score = 0

    # Loop through top direction
    for i in range(x - 1, -1, -1):
        if forest[i][y] < original_element:
            count += 1
        else:
            count = count if count == 0 else count + 1
            break
    count = count if count > 0 else 1
    scenic_score *= count
    count = 0

    # Loop through bottom direction
    for i in range(x + 1, len(forest)):
        if forest[i][y] < original_element:
            count += 1
        else:
            count = count if count == 0 else count + 1
            break
    count = count if count > 0 else 1
    scenic_score *= count
    count = 0

    # Loop through left direction
    for i in range(y - 1, -1, -1):
        if forest[x][i] < original_element:
            count += 1
        else:
            count = count if count == 0 else count + 1
            break
    count = count if count > 0 else 1
    scenic_score *= count
    count = 0

    # Loop through right direction
    for i in range(y + 1, len(forest[0])):
        if forest[x][i] < original_element:
            count += 1
        else:
            count = count if count == 0 else count + 1
            break
    count = count if count > 0 else 1
    scenic_score *= count
    return scenic_score


def main():
    forest = parser()
    ans1 = part1(forest)
    ans2 = part2(forest)
    print(f"part 1: {ans1} - part 2: {ans2}")


if __name__ == "__main__":
    main()
