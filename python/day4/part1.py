from dataclasses import dataclass, field
from enum import IntEnum, auto

in_date = ""

with open("input.txt") as f:
    in_date = f.read()


class Direction(IntEnum):
    # horizontal, vertical, diagonal
    Up = auto()  # |
    UpRight = auto()  # /
    Right = auto()  # -
    DownRight = auto()  # \
    Down = auto()  # |
    DownLeft = auto()  # /
    Left = auto()  # -
    UpLeft = auto()  # \


@dataclass
class Search:
    Direction: Direction
    CurrentPoint: tuple[int] = field(default_factory=lambda: tuple())
    StartingPoint: tuple[int] = field(default_factory=lambda: tuple())
    Letters: list[str] = field(default_factory=lambda: list(["S", "A", "M"]))  # last X absent, due to has already been found at first
    Finished: bool = False
    Success: bool = False


def get_new_searches(cur_point: tuple[int]):
    searches = []
    all_dirs = [
        Direction.Up,
        Direction.UpRight,
        Direction.Right,
        Direction.DownRight,
        Direction.Down,
        Direction.DownLeft,
        Direction.Left,
        Direction.UpLeft,
    ]
    for d in all_dirs:
        searches.append(Search(Direction=d, CurrentPoint=cur_point, StartingPoint=cur_point))
    return searches


def get_next_point(hw_len: tuple[int], search: Search) -> tuple[int | None]:
    next_step = list(search.CurrentPoint)
    d = search.Direction
    if d == Direction.Up:
        next_step[0] -= 1
    elif d == Direction.UpRight:
        next_step[0] -= 1
        next_step[1] += 1
    elif d == Direction.Right:
        next_step[1] += 1
    elif d == Direction.DownRight:
        next_step[0] += 1
        next_step[1] += 1
    elif d == Direction.Down:
        next_step[0] += 1
    elif d == Direction.DownLeft:
        next_step[0] += 1
        next_step[1] -= 1
    elif d == Direction.Left:
        next_step[1] -= 1
    elif d == Direction.UpLeft:
        next_step[0] -= 1
        next_step[1] -= 1

    if not (next_step[0] in range(0, hw_len[0])) or not (next_step[1] in range(0, hw_len[1])):
        return tuple()
    return tuple(next_step)


lines = in_date.strip().split("\n")
matrix = [list(line.strip()) for line in lines]

search_stack = []
current_stack = []

hw_len = (len(matrix), len(matrix[-1]))

passed_searches = []

for h_idx, _ in enumerate(matrix):
    for w_idx, _ in enumerate(matrix[h_idx]):
        if matrix[h_idx][w_idx] == "X":
            search_stack.extend(get_new_searches((h_idx, w_idx)))
        while search_stack:
            current_search: Search = search_stack.pop()
            xy_to_check = get_next_point(hw_len, current_search)
            if xy_to_check:
                x = xy_to_check[0]
                y = xy_to_check[1]
                letter_to_find = current_search.Letters[-1]
                if matrix[x][y] == letter_to_find:
                    current_search.Letters.pop()
                    current_search.CurrentPoint = (x, y)
                else:
                    current_search.Finished = True
                    current_search.Success = False
                if not current_search.Letters:
                    current_search.Finished = True
                    current_search.Success = True
            else:
                current_search.Finished = True
                current_search.Success = False
            if current_search.Finished:
                passed_searches.append(current_search)
            else:
                search_stack.append(current_search)


count = 0
for s in passed_searches:
    if s.Success:
        count += 1

print(f"Found: {count} XMAS words")
