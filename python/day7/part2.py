from itertools import product
import asyncio


in_date = ""

with open("input.txt") as f:
    in_date = f.read()


class NonInt(int):
    # allow to implement `@` operator behavior
    # that will act as `||` from the task
    def __matmul__(self, other):
        return int(f"{self}{other}")


operators_p1 = ["*", "+"]
operators_p2 = ["*", "+", "@"]


def get_all_options(operators, exclude=None):
    all_possibles = []

    valid = set()
    for idx, line in enumerate(in_date.strip().split("\n")):
        if exclude and idx in exclude:
            continue
        val, rest = line.split(":")
        val = int(val)
        operands = [int(o) for o in rest.strip().split()]
        num_operations = len(operands) - 1
        possible_sets = set(list(product(operators, repeat=num_operations)))
        for op_set in possible_sets:
            cp_operands = operands[::]
            result = f"NonInt({cp_operands.pop(0)})"
            for op in op_set:
                sec_operand = cp_operands.pop(0)
                result = f"(NonInt({result}) {op} NonInt({sec_operand}))"
            all_possibles.append((result, val, idx))

    return all_possibles


passed = set()


async def check(expression, val, idx):
    if idx in passed:
        return
    if eval(expression) == val:
        passed.add(idx)
        return idx, val


async def amint(opt, covered=None):
    futures = [check(*t) for t in get_all_options(opt, covered)]
    raw_results = await asyncio.gather(*futures)
    return set([res for res in raw_results if res])


valid_p1 = asyncio.run(amint(operators_p1))
valid_p2 = asyncio.run(amint(operators_p2, passed))

total = sum(map(lambda x: x[-1], valid_p1))
total += sum(map(lambda x: x[-1], valid_p2))

print(total)
