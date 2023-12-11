import os
from collections import deque
from itertools import combinations

input_file = "test_input.txt"


def calculate(lines: list[str]) -> int:
    res = 0

    universe = process_input(lines)
    universe = expand_universe(universe)
    universe, id_value, max_galaxy = mark_galaxies(universe)

    print_universe(universe)

    pairs = unique_pairs(range(1, max_galaxy + 1))
    pairs = sorted(pairs, key=lambda x: x[0])
    pairs = [([(value[0], value[1]) for value in id_value if value[2] == pair[0]][0],
              [(value[0], value[1]) for value in id_value if value[2] == pair[1]][0],
              pair[0], pair[1])
             for pair in pairs]
    print(pairs)
    print()

    for start, end, start_char, end_char in pairs:
        path_length = manhattan_distance(start, end)
        res += path_length
        print(f"{start_char}, {end_char}: {path_length} = {res}")

    return res


def unique_pairs(numbers) -> set:
    numbers_set = set(numbers)
    return set(combinations(numbers_set, 2))


def manhattan_distance(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


def is_valid(x, y, rows, cols):
    return 0 <= x < rows and 0 <= y < cols


def bfs(grid, start, end):
    rows, cols = len(grid), len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]  # Right, Left, Down, Up

    queue = deque([(start[0], start[1], 0)])  # (x, y, distance)
    visited = set()
    visited.add((start[0], start[1]))

    while queue:
        y, x, distance = queue.popleft()

        if (y, x) == end:
            return distance  # Shortest path found

        for dx, dy in directions:
            new_y, new_x = y + dy, x + dx
            if is_valid(new_y, new_x, rows, cols) and (new_y, new_x) not in visited:
                queue.append((new_y, new_x, distance + 1))
                visited.add((new_y, new_x))

    return -1  # No path found


def print_universe(universe: list[list[str]]):
    for y in range(len(universe)):
        for x in range(len(universe[y])):
            print(universe[y][x], end="")
        print()
    print()


def process_input(lines: list[str]) -> list[list[str]]:
    return [list(line.strip()) for line in lines]


def expand_universe(universe: list[list[str]]) -> list[list[str]]:
    height = len(universe)
    width = len(universe[0])
    y_ids = []
    x_ids = []

    for y in range(height):
        should_expand = True
        for x in range(width):
            if universe[y][x] == "#":
                should_expand = False
        if should_expand:
            y_ids.append(y)

    for x in range(width):
        should_expand = True
        for y in range(height):
            if universe[y][x] == "#":
                should_expand = False
        if should_expand:
            x_ids.append(x)

    for i, y in enumerate(y_ids):
        universe.insert(y + i, ["."] * width)

    height = len(universe)
    for i, x in enumerate(x_ids):
        for y in range(height):
            universe[y].insert(x + i, ".")

    return universe


def mark_galaxies(universe: list[list[str]]) -> tuple[list, list, int]:
    index = 1
    id_value = []

    for y in range(len(universe)):
        for x in range(len(universe[y])):
            if universe[y][x] == "#":
                universe[y][x] = index
                id_value.append((y, x, index))
                index += 1
    return universe, id_value, index - 1


def read_input() -> list[str]:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/{input_file}", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(f"Result: {output}")


if __name__ == "__main__":
    main()
