from dataclasses import dataclass, field

in_date = ""

with open("input.txt") as f:
    in_date = f.read()

lines = in_date.strip().split("\n")

grid = []

for line in lines:
    row = []
    for i in list(line):
        if i != ".":
            row.append(int(i))
        else:
            row.append(None)
    grid.append(row)


@dataclass
class Map:
    grid: list[list[int | None]]
    visited: set[tuple[int, int]] = field(default_factory=set)

    def on_map(self, point: tuple[int, int]):
        if point:
            return 0 <= point[0] < len(self.grid) and 0 <= point[1] < len(self.grid[0])
        return False

    def count(self, value: int):
        return sum([1 for rv in self.grid for cv in rv if cv == value])

    def valid_neighbor(self, current_value, neighbor: tuple[int, tuple[int, int]], visited: set[tuple[int, int]]):
        if current_value is None:
            return False
        if neighbor in visited:
            return False
        if not self.on_map(neighbor[1]):
            return False
        if self.grid[neighbor[1][0]][neighbor[1][1]] is None:
            return False
        return self.grid[neighbor[1][0]][neighbor[1][1]] - current_value == 1

    def find_paths(self, start: tuple[int, int]):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        stack = [(0, start, -1)]
        visited = set()
        visited.add(start)

        all_paths = []

        while stack:
            cur_id, cur_pos, previous = stack.pop()
            current_value = self.grid[cur_pos[0]][cur_pos[1]]

            if current_value == 9 and previous == 8:
                all_paths.append((cur_id, cur_pos))

            for add_idx, direction in enumerate(directions, cur_id + 1):
                neighbor = (cur_pos[0] + direction[0], cur_pos[1] + direction[1])
                flow_step = (cur_id + add_idx, neighbor, current_value)
                if self.valid_neighbor(current_value, flow_step, visited):
                    stack.append(flow_step)
                    visited.add(flow_step)
        return len(all_paths)


m = Map(grid)

total = 0
for i, rv in enumerate(m.grid):
    for j, cv in enumerate(rv):
        if cv == 0:
            start = (i, j)
            total += m.find_paths(start)

print(total)
