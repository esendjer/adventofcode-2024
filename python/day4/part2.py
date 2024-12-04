from dataclasses import dataclass, replace, field
from enum import IntEnum, auto

in_date = ""

with open("input.txt") as f:
    in_date = f.read()


@dataclass
class XShape:
    StartingPoint: tuple[int] = field(default_factory=lambda: tuple())
    Success: bool = False


def get_points_to_check(hw_len: tuple[int], shape: XShape) -> list[list[int] | None]:
    # 1 - 2
    # - - -
    # 3 - 4
    #
    # -1,-1   -1,+1
    #      x,y
    # +1,-1   +1,+1
    #
    next_steps = [
        [shape.StartingPoint[0] - 1, shape.StartingPoint[1] - 1],
        [shape.StartingPoint[0] - 1, shape.StartingPoint[1] + 1],
        [shape.StartingPoint[0] + 1, shape.StartingPoint[1] - 1],
        [shape.StartingPoint[0] + 1, shape.StartingPoint[1] + 1],
    ]
    for p in next_steps:
        if not (p[0] in range(0, hw_len[0])) or not (p[1] in range(0, hw_len[1])):
            return list()
    return next_steps


VALID_SHAPES = {
    """
M.S
.A.
M.S
""",
    """
S.M
.A.
S.M
""",
    """
M.M
.A.
S.S
""",
    """
S.S
.A.
M.M
""",
}


def validate_x(hw_len, search: XShape) -> bool:
    global VALID_SHAPES
    points = get_points_to_check(hw_len, search)
    l = []
    if points:
        d = f"""
{matrix[points[0][0]][points[0][1]]}.{matrix[points[1][0]][points[1][1]]}
.{matrix[search.StartingPoint[0]][search.StartingPoint[1]]}.
{matrix[points[2][0]][points[2][1]]}.{matrix[points[3][0]][points[3][1]]}
"""
        if d in VALID_SHAPES:
            return True
    return False


lines = in_date.strip().split("\n")
matrix = [list(line.strip()) for line in lines]

hw_len = (len(matrix), len(matrix[-1]))

passed_searches = []

for h_idx, _ in enumerate(matrix):
    for w_idx, _ in enumerate(matrix[h_idx]):
        if matrix[h_idx][w_idx] == "A":
            current_search = XShape((h_idx, w_idx))
            current_search.Success = validate_x(hw_len, current_search)
            passed_searches.append(current_search)


count = 0
for s in passed_searches:
    s: XShape = s
    current = False
    if s.Success:
        count += 1

print(f"Found: {count} X-shaped MAS words")
print(len(passed_searches))
