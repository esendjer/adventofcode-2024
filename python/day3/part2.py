import re

in_date = ""

with open("input.txt") as f:
    in_date = f.read()

pattern = r"(don\'t\(\))|(do\(\))|(mul\((\d{1,3},\d{1,3})\))"

def mul(xy) -> int:
    x, y = (int(d) for d in xy.split(","))
    return x * y


carry_on = True
total = 0
for catch in re.finditer(pattern, in_date):
    if carry_on and catch.group(3):
        total += mul(catch[4])
    elif catch.group(2):
        carry_on = True
    elif catch.group(1):
        carry_on = False

print(total)
