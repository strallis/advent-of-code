with open("2023/day1.txt", "r") as input:
    input_raw = input.read()
    input_list = input_raw.split("\n")[0:-1]

# input_list = ['two1nine', '8wothree', 'abcone2threexyz', 'xtwone3four', '4nineeightseven2', 'zoneight234', '7pqrstsixteen']

sum = 0
for e in input_list:
    s = "".join(x for x in e if x.isdigit())
    num = s[0] + s[-1]
    sum += int(num)

print(f"Part1: {sum}")


def replace_with_dict(e: str) -> str:
    transformation = {
        "one": "one1one",
        "two": "two2two",
        "three": "three3three",
        "four": "four4four",
        "five": "five5five",
        "six": "six6six",
        "seven": "seven7seven",
        "eight": "eight8eight",
        "nine": "nine9nine",
    }
    for k, v in transformation.items():
        e = e.replace(k, v)
    return e


sum = 0
for e in input_list:
    e = replace_with_dict(e)
    s = "".join(x for x in e if x.isdigit())
    print(f"first:{s[0]}, last:{s[-1]}")
    num = s[0] + s[-1]
    sum += int(num)

print(f"Part2: {sum}")
