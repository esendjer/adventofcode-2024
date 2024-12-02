import asyncio
from enum import IntEnum

in_data: str = ""

with open("input.txt") as f:
    in_data = f.read()

str_reports = in_data.strip().split("\n")

reports = [l.strip().split() for l in str_reports]

safe_reports = 0


class Direction(IntEnum):
    UP = 1
    DOWN = 2
    UNDIRECTED = 3
    UNKNOWN = 9

def set_dir(a, b):
    if a < b:
        return Direction.UP
    elif a > b:
        return Direction.DOWN
    else:
        return Direction.UNDIRECTED

def check_rep(rep):
    last_direct = Direction.UNKNOWN
    a = rep[0]
    for idx in range(1, len(rep)):
        b = rep[idx]
        if last_direct == Direction.UNKNOWN:
            last_direct = set_dir(a, b)
        current_direct = set_dir(a, b)
        good_ord = last_direct == current_direct
        good_diff = 1 <= abs(a - b) <= 3
        if not (good_ord and good_diff):
            return False
        a = b
    return True

async def main():
    tasks = []
    for r in reports:
        int_r = [int(i) for i in r]
        tasks.append(int_r)

    futures = [check_rep(t) for t in tasks]

    results = await asyncio.gather(*futures, return_exceptions=True)
    errors = [res for res in results if isinstance(res, BaseException)]
    res = sum(filter(lambda x: x, results))
    print(f"Errors: {len(errors)}")

    print(res)


asyncio.run(main())
