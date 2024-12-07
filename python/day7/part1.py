from itertools import product
import asyncio


in_date = ""

with open("input.txt") as f:
    in_date = f.read()

all_operators = ["*", "+"]


def get_all_options(operators):
    all_possibles = []
    for idx, line in enumerate(in_date.strip().split("\n")):
        val, rest = line.split(":")
        val = int(val)
        operands = [int(o) for o in rest.strip().split()]
        num_operations = len(operands) - 1
        possible_sets = set(list(product(operators, repeat=num_operations)))
        for op_set in possible_sets:
            cp_operands = operands[::]
            result = f"{cp_operands.pop(0)}"
            for op in op_set:
                sec_operand = cp_operands.pop(0)
                result = f"({result} {op} {sec_operand})"
            all_possibles.append((result, val, idx))

    return all_possibles


passed = set()


async def check(expression, val, idx):
    if idx in passed:
        return
    if eval(expression) == val:
        passed.add(idx)
        return idx, val


async def amint(opt):
    futures = [check(*t) for t in get_all_options(opt)]
    raw_results = await asyncio.gather(*futures)
    return set([res for res in raw_results if res])


valid = asyncio.run(amint(all_operators))

total = sum(map(lambda x: x[-1], valid))

print(total)
