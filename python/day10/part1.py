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

    def on_map(self, point):
        if point:
            return 0 <= point[0] < len(self.grid) and 0 <= point[1] < len(self.grid[0])
        return False

    def count(self, value):
        total = 0
        points = set()
        for i, rv in enumerate(self.grid):
            for j, cv in enumerate(rv):
                if cv == value:
                    total += 1
                    points.add((i, j))
        return total, points

    def valid_neighbor(self, current_value, neighbor, visited):
        if current_value is None:
            return False
        if neighbor in visited:
            return False
        if not self.on_map(neighbor):
            return False
        if self.grid[neighbor[0]][neighbor[1]] is None:
            return False
        return self.grid[neighbor[0]][neighbor[1]] - current_value == 1

    def is_reachable(self, start, end):
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        queue = [(0, start)]
        visited = set()
        visited.add(start)

        while queue:
            previous, cur_point = queue.pop(0)
            current_value = self.grid[cur_point[0]][cur_point[1]]
            if current_value == 9 and previous == 8 and cur_point == end:
                return True

            for direction in directions:
                neighbor = (cur_point[0] + direction[0], cur_point[1] + direction[1])
                if self.valid_neighbor(current_value, neighbor, visited):
                    queue.append((current_value, neighbor))
                    visited.add(neighbor)
        return False


m = Map(grid)

_, end_points = m.count(9)

total = 0
for i, rv in enumerate(m.grid):
    for j, cv in enumerate(rv):
        if cv == 0:
            start = (i, j)
            for end in end_points:
                if m.is_reachable(start, end):
                    total += 1

print(total)
