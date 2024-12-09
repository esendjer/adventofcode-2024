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


def find_files(array):
    files = {}
    start = 0
    for i, item in enumerate(array):
        if item is None:
            continue
        if item not in files:
            start = i
        files[item] = ((i + 1 - start), (start, i + 1))
    return files


def find_free_spaces(array, l_needed, rightest_pos):
    # sub_arr = array[:rightest_pos]
    for i in range(rightest_pos):
        start = i
        end = i
        if array[i] is not None:
            continue
        for j in range(i, rightest_pos):
            end = j
            if array[j] is not None:
                break
        if end - start >= l_needed:
            return start, end
    return (-1, -1)


def compress_by_files(array):
    all_files = find_files(array)
    for key in list(all_files.keys())[-1::-1]:
        f_len, pos = all_files[key]
        free = find_free_spaces(array, f_len, pos[1])
        if free == (-1, -1):
            continue
        array[pos[0] : pos[1]], array[free[0] : free[0] + f_len] = (
            array[free[0] : free[0] + f_len],
            array[pos[0] : pos[1]],
        )
    return array


def compute_checksum(array):
    total = 0
    for idx, num in enumerate(array):
        if num:
            total += idx * num
    return total


dick_map = [int(n) for n in in_date.strip()]
disk_blocks = map_to_blocks(dick_map)
compress_by_files(disk_blocks)
print(compute_checksum(disk_blocks))
