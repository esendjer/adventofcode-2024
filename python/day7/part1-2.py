from itertools import product

in_date = ""

with open("input.txt") as f:
    in_date = f.read()

operators = ["*", "+"]


def calculate(operators, nums):
    t = nums[0]
    for i, o in enumerate(operators):
        if o == "*":
            t *= nums[i + 1]
        elif o == "+":
            t += nums[i + 1]
    return t


def process():
    valid = []
    for idx, line in enumerate(in_date.strip().split("\n")):
        val, rest = line.split(":")
        val = int(val)
        operands = [int(o) for o in rest.strip().split()]
        num_operations = len(operands) - 1
        possible_sets = set(list(product(operators, repeat=num_operations)))
        for op_set in possible_sets:
            if calculate(op_set, operands) == val:
                valid.append(val)
                break

    return valid


total = sum(process())

print(total)
