import os

day = os.path.basename(__file__).strip(".py")

with open(f"2023/{day}.txt", "r") as input:
    input_raw = input.read()
    input_list = input_raw.split("\n")  # [0:-1]

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14

sum_of_ids = 0
for i in input_list:
    cur_max_red = 0
    cur_max_green = 0
    cur_max_blue = 0

    game_id = int(i.split(":")[0].replace("Game ", ""))
    cubes = i.split(":")[1][1:]
    for cube in cubes.replace(";", ",").strip().split(","):

        cube_num = int(cube.strip().split(" ")[0])
        cube_color = cube.strip().split(" ")[1]

        if cube_color == "red" and cur_max_red < cube_num:
            cur_max_red = cube_num
        if cube_color == "green" and cur_max_green < cube_num:
            cur_max_green = cube_num
        if cube_color == "blue" and cur_max_blue < cube_num:
            cur_max_blue = cube_num

    if (
        cur_max_red <= MAX_RED
        and cur_max_green <= MAX_GREEN
        and cur_max_blue <= MAX_BLUE
    ):
        sum_of_ids += game_id

print(f"Day 2 Part 1: {sum_of_ids}")

min_cubes_needed = 0
for i in input_list:
    cur_max_red = 0
    cur_max_green = 0
    cur_max_blue = 0

    game_id = int(i.split(":")[0].replace("Game ", ""))
    cubes = i.split(":")[1][1:]
    for cube in cubes.replace(";", ",").strip().split(","):

        cube_num = int(cube.strip().split(" ")[0])
        cube_color = cube.strip().split(" ")[1]

        if cube_color == "red" and cur_max_red < cube_num:
            cur_max_red = cube_num
        if cube_color == "green" and cur_max_green < cube_num:
            cur_max_green = cube_num
        if cube_color == "blue" and cur_max_blue < cube_num:
            cur_max_blue = cube_num

    min_cubes_needed += cur_max_red * cur_max_green * cur_max_blue

print(f"Day 2 Part 2: {min_cubes_needed}")
