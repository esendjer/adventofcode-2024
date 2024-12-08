from itertools import product, combinations_with_replacement, combinations

in_date = ""

with open("input.txt") as f:
    in_date = f.read()


raw_map = in_date.strip().split("\n")
matrixed = [list(row.strip()) for row in raw_map]


def walk_map(matrix):
    all_antennas = {}
    for i, row in enumerate(matrix):
        for j, col in enumerate(row):
            if col != ".":
                if not col in all_antennas:
                    all_antennas[col] = set()
                all_antennas[col].add((i, j))

    return all_antennas


def calculate_diff(a_spot, b_spot):
    x = a_spot[0] - b_spot[0]
    y = a_spot[1] - b_spot[1]
    return (x, y), (x * -1, y * -1)


def compute_antinodes(spots):
    listed_spots = list(spots)
    anti_nodes = []
    for idx, first_sport in enumerate(listed_spots):
        for jdx in range(idx + 1, len(listed_spots)):
            second_spot = listed_spots[jdx]
            abs_anti_node = calculate_diff(first_sport, second_spot)
            first_antinode = first_sport[0] + abs_anti_node[0][0], first_sport[1] + abs_anti_node[0][1]
            second_antinode = second_spot[0] + abs_anti_node[1][0], second_spot[1] + abs_anti_node[1][1]
            anti_nodes.append(first_antinode)
            anti_nodes.append(second_antinode)

    return anti_nodes


def on_map(m, spot):
    return 0 <= spot[0] < len(m) and 0 <= spot[1] < len(m[0])


def set_antinode(m, spot):
    if on_map(m, spot):
        m[spot[0]][spot[1]] = "#"
    return m


def to_str(m):
    return "\n".join(["".join(row) for row in m])


all_antennas = walk_map(matrixed)

for antenna, spots in all_antennas.items():
    anti_nodes_v1 = compute_antinodes(spots)
    for anti_node in anti_nodes_v1:
        matrixed = set_antinode(matrixed, anti_node)

res = to_str(matrixed)

print(res.count("#"))
