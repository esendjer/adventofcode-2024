in_date = ""

with open("input.txt") as f:
    in_date = f.read()


def map_to_blocks(array):
    blocks = []
    for idx, num in enumerate(array):
        sub_blocks = []
        if not idx % 2:
            # data block
            sub_blocks = [idx // 2 for _ in range(num)]
        else:
            # free block
            sub_blocks = [None for _ in range(num)]
        blocks.extend(sub_blocks)

    return blocks


def compress(array):
    l_idx = 0
    r_idx = len(array) - 1
    go_on = True
    while go_on:
        if l_idx >= r_idx:
            go_on = False
        l = array[l_idx]
        r = array[r_idx]
        if r == None:
            r_idx -= 1
            continue
        if l is not None:
            l_idx += 1
            continue
        array[l_idx], array[r_idx] = array[r_idx], array[l_idx]
    return array


def compute_checksum(array):
    total = 0
    for idx, num in enumerate(array):
        if num:
            total += idx * num
    return total


dick_map = [int(n) for n in in_date.strip()]
disk_blocks = map_to_blocks(dick_map)
compress(disk_blocks)
print(compute_checksum(disk_blocks))
