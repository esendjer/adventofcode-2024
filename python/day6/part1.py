from enum import IntEnum, auto
from dataclasses import dataclass

in_date = ""

with open("input.txt") as f:
    in_date = f.read()


class Direction(IntEnum):
    Up = auto()
    Right = auto()
    Down = auto()
    Left = auto()


@dataclass
class Position:
    x: int
    y: int


@dataclass
class Guardian:
    Pos: Position
    Dir: Direction

    def turn_right(self):
        if self.Dir == Direction.Up:
            self.Dir = Direction.Right
        elif self.Dir == Direction.Right:
            self.Dir = Direction.Down
        elif self.Dir == Direction.Down:
            self.Dir = Direction.Left
        elif self.Dir == Direction.Left:
            self.Dir = Direction.Up

    def take_step(self):
        if self.Dir == Direction.Up:
            self.Pos.x -= 1
        elif self.Dir == Direction.Right:
            self.Pos.y += 1
        elif self.Dir == Direction.Down:
            self.Pos.x += 1
        elif self.Dir == Direction.Left:
            self.Pos.y -= 1
        return self.Pos

    def next_pos(self):
        posable_pos = Position(self.Pos.x, self.Pos.y)
        if self.Dir == Direction.Up:
            posable_pos.x -= 1
        elif self.Dir == Direction.Right:
            posable_pos.y += 1
        elif self.Dir == Direction.Down:
            posable_pos.x += 1
        elif self.Dir == Direction.Left:
            posable_pos.y -= 1
        return posable_pos


class Action(IntEnum):
    Turn = auto()
    Step = auto()
    Out = auto()


class Map:
    def __init__(self, matrix: str):
        self.map = matrix
        self.guardian = self.find_guardian()

    def find_guardian(self):
        for i, row in enumerate(self.map):
            for j, col in enumerate(row):
                if col == "^":
                    self.map[i][j] = "X"
                    return Guardian(Position(i, j), Direction.Up)

    def is_open(self, pos: Position):
        if not self.on_map(pos):
            return False, Action.Out
        if self.map[pos.x][pos.y] in {".", "X"}:
            return True, Action.Step
        else:
            return False, Action.Turn

    def on_map(self, pos: Position):
        return 0 <= pos.x < len(self.map) and 0 <= pos.y < len(self.map[0])

    def mark_visited(self, pos: Position):
        self.map[pos.x][pos.y] = "X"

    def count_visited(self):
        return sum([1 for row in self.map for col in row if col == "X" or col == "^"])

    def __str__(self):
        return "\n".join(["".join(row) for row in self.map])


raw_map = in_date.strip().split("\n")
matrixed = [list(row.strip()) for row in raw_map]
m = Map(matrixed)

go_on = True
while go_on:
    current_pos = m.guardian.Pos
    is_open, action = m.is_open(m.guardian.next_pos())
    if is_open:
        m.guardian.take_step()
        m.mark_visited(current_pos)
    elif action == Action.Turn:
        m.guardian.turn_right()
    elif action == Action.Out:
        go_on = False

print(m.count_visited())