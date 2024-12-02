in_data: str = ""

with open("input.txt") as f:
    in_data = f.read()

l0, l1 = [], []

for idx, item in enumerate(in_data.strip().split()):
    if idx % 2:
        l1.append(int(item))
    else:
        l0.append(int(item))

l0.sort()
l1.sort()

diff = []

f = 0
l = len(l0) - 1

while f <= l:
    fi0, fi1 = l0[f], l1[f]
    diff.append(abs(fi0 - fi1))
    f += 1

# print(diff)
print(sum(diff))
