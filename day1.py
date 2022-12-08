from aocd import data

elves_rations = data.split("\n\n")
calories_sums = []

for ration in elves_rations:
    food_items = ration.split("\n")
    food_items = [int(i) for i in food_items]
    calories = sum(food_items)
    calories_sums.append(calories)

calories_sums.sort()
print(calories_sums[-1])
print(sum(calories_sums[-3:]))
