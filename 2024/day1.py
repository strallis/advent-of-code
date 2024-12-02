list1 = []
list2 = []

with open("2024/day1.txt", "r") as input_file:
    for line in input_file:
        values = line.split()
        if len(values) == 2:
            list1.append(int(values[0]))
            list2.append(int(values[1]))

# Question 1
# Sort lists
sorted_list1, sorted_list2 = sorted(list1), sorted(list2)

ans1 = 0
for i in range(len(list1)):
    ans1 += abs(sorted_list1[i] - sorted_list2[i])

print(ans1)

# Questions 2
ans2 = 0
for v in list1:
    ans2 += v * list2.count(v)

print(ans2)