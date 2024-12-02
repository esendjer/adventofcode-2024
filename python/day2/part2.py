import asyncio
from enum import IntEnum

in_data: str = ""

with open("input.txt") as f:
    in_data = f.read()

str_reports = in_data.strip().split("\n")

reports = [l.strip().split() for l in str_reports]


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


def main():
    safe_reports = 0
    last_resorts = []
    for r in reports:
        int_r = [int(i) for i in r]
        if check_rep(int_r):
            safe_reports += 1
        else:
            last_resorts.append(int_r)

    l_safe_reports = 0
    for last_resort_repo in last_resorts:
        for i in range(len(last_resort_repo)):
            sub_arr = last_resort_repo[:i] + last_resort_repo[i + 1 :]
            if check_rep(sub_arr):
                l_safe_reports += 1
                break

    print(f"Safe at the first place: {safe_reports}")
    print(f"Safe after removing a single report: {l_safe_reports}")
    print(f"Total: {l_safe_reports+safe_reports}")


if __name__ == "__main__":
    main()
