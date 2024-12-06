from enum import IntEnum, auto
from dataclasses import dataclass, field

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
    Walks: set = field(default_factory=lambda: set())
    CurrentWalk: list = field(default_factory=lambda: list())
    RepeatedWalks: int = 0
    LastSteps: list = field(default_factory=lambda: list())

    def turn_right(self):
        if self.Dir == Direction.Up:
            self.Dir = Direction.Right
        elif self.Dir == Direction.Right:
            self.Dir = Direction.Down
        elif self.Dir == Direction.Down:
            self.Dir = Direction.Left
        elif self.Dir == Direction.Left:
            self.Dir = Direction.Up
        walk = tuple(self.CurrentWalk)
        self.CurrentWalk = []
        if walk in self.Walks:
            self.RepeatedWalks += 1
        if walk:
            # to not add empty walks
            self.Walks.add(walk)

    def take_step(self):
        if self.Dir == Direction.Up:
            self.Pos.x -= 1
        elif self.Dir == Direction.Right:
            self.Pos.y += 1
        elif self.Dir == Direction.Down:
            self.Pos.x += 1
        elif self.Dir == Direction.Left:
            self.Pos.y -= 1
        self.CurrentWalk.append((self.Pos.x, self.Pos.y))
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

    def add_step(self, step: str):
        if len(self.LastSteps) > 99:
            self.LastSteps = self.LastSteps[1:]
        self.LastSteps.append(step)


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
        return sum([1 for row in self.map for col in row if col == "X"])

    def get_spot(self, pos: Position):
        return self.map[pos.x][pos.y]

    def __str__(self):
        return "\n".join(["".join(row) for row in self.map])


def check_loop(m: Map, iter: int, total: int):
    go_on = True
    last_action = []
    loop_detected = False
    reason = ""
    while go_on:
        curr_pos = m.guardian.Pos
        next_pos = m.guardian.next_pos()
        is_open, action = m.is_open(next_pos)
        if is_open:
            m.guardian.take_step()
            m.mark_visited(curr_pos)
        elif action == Action.Turn:
            m.guardian.turn_right()
        elif action == Action.Out:
            go_on = False
        if last_action.count(action) > 2:
            last_action = last_action[1:]
        last_action.append(action)
        # does guardian stuck in an infinite loop?
        if m.guardian.RepeatedWalks >= 2:
            go_on = False
            loop_detected = True
            reason = "2 repeated walks"
        if last_action == [Action.Turn, Action.Turn, Action.Turn]:
            go_on = False
            loop_detected = True
            reason = "3 turns in a row"
    print(f"Iteration {iter}/{total}")
    return loop_detected


raw_map = in_date.strip().split("\n")
matrixed = [list(row.strip()) for row in raw_map]

possible_obstacles = []

for i in range(len(matrixed)):
    for j in range(len(matrixed[i])):
        if matrixed[i][j] == ".":
            possible_obstacles.append((i, j))

cont = 0
for i, obs in enumerate(possible_obstacles):
    matrixed = [list(row.strip()) for row in raw_map]
    matrixed[obs[0]][obs[1]] = "#"
    m = Map(matrixed)
    if m.guardian is None:
        continue
    if check_loop(m, i + 1, len(possible_obstacles)):
        cont += 1

print(cont)
