in_data: str = ""

with open("input.txt") as f:
    in_data = f.read()

l0, l1 = [], []

for idx, item in enumerate(in_data.strip().split()):
    if idx % 2:
        l1.append(int(item))
    else:
        l0.append(int(item))


count_right = {}

for item in l1:
    count = count_right.setdefault(item, 0)
    count_right[item] = count + 1

count_diff = []

for item in l0:
    count = count_right.setdefault(item, 0)
    count_diff.append(item * count)

print(sum(count_diff))
