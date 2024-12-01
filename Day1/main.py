file = "data.txt"

first_list = []
second_list = []
distance = 0
score = 0


with open(file, "r") as input:
    for line in input:
        first, second = map(int, line.strip().split())
        first_list.append(first)
        second_list.append(second)

first_list.sort()
second_list.sort()

for first, second in zip(first_list, second_list):
    distance += abs(first - second)

for number in first_list:
    amount = second_list.count(number)
    score_to_add = number * amount
    score += score_to_add



print(f"Total distance: {distance}")
print(f"Simalitarty score: {score}")