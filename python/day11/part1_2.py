from functools import lru_cache


def is_even(num):
    count = 0
    a = num
    while a:
        a //= 10
        count += 1
    return count % 2 == 0


@lru_cache(maxsize=1000_000)
def check_stone(stone):
    if stone == 0:
        return (1, -1)
    if is_even(stone):
        s = str(stone)
        l = s[: len(s) // 2]
        r = s[len(s) // 2 :]
        return (int(l), int(r))
    return (stone * 2024, -1)


in_date = ""

with open("input.txt") as f:
    in_date = f.read()

init_stones = [int(i) for i in in_date.strip().split()]

total_nums = {}
for i in init_stones:
    res = total_nums.get(i, 0) + 1
    total_nums[i] = res


for iter in range(75):
    new_total_nums = {}
    for n, c in total_nums.items():
        l, r = check_stone(n)
        if r != -1:
            r_count = new_total_nums.get(r, 0)
            new_total_nums[r] = r_count + (1 * c)
        l_count = new_total_nums.get(l, 0)
        new_total_nums[l] = l_count + (1 * c)
    total_nums = new_total_nums

total = sum(total_nums.values())
print(total)
