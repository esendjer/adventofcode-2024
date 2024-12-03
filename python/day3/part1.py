import re

in_date = ""

with open("input.txt") as f:
    in_date = f.read()

pattern = r"(mul\((\d{1,3},\d{1,3})\))"

def mul(xy) -> int:
    x, y = (int(d) for d in catch[2].split(","))
    return x * y


total = 0
for catch in re.finditer(pattern, in_date):
    total += mul(catch[2])

print(total)
