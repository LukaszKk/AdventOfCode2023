import os
from heapq import heappop, heappush

input_file = "test_input.txt"


def process_input(lines):
    return [list(map(int, list(line.strip()))) for line in lines]


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print()
    print()


def modified_dijkstra(grid):
    max_y, max_x = len(grid) - 1, len(grid[0]) - 1
    start_y, start_x, end_y, end_x = 0, 0, max_y, max_x

    directions = [{"direction": "r", "coord": (0, 1)},
                  {"direction": "l", "coord": (0, -1)},
                  {"direction": "d", "coord": (1, 0)},
                  {"direction": "u", "coord": (-1, 0)}]

    heap = [(0, start_y, start_x, "r", 0, [])]
    visited = set()

    while heap:
        curr_distance, curr_y, curr_x, curr_direction, curr_direction_length, curr_path = heappop(heap)

        if (curr_y == end_y) and (curr_x == end_x):
            return curr_distance

        for direct in directions:
            dy = direct["coord"][0]
            dx = direct["coord"][1]
            new_y, new_x = curr_y + dy, curr_x + dx

            if not ((0 <= new_y <= max_y) and (0 <= new_x <= max_x)):
                continue

            if (new_y == curr_y) and (new_x == curr_x):
                continue

            if curr_direction_length >= 3:
                continue

            if (new_y, new_x) in visited:
                continue

            visited.add((new_y, new_x))

            new_direction_length = 0
            if curr_direction == direct["direction"]:
                new_direction_length = curr_direction_length + 1

            new_distance = curr_distance + grid[new_y][new_x]
            new_direction = direct["direction"]

            heappush(heap, (
                new_distance,
                new_y,
                new_x,
                new_direction,
                new_direction_length,
                curr_path + [(new_y, new_x)]
            ))

    return float('inf')


def calculate(lines: list[str]) -> int:
    grid = process_input(lines)
    print_grid(grid)
    return modified_dijkstra(grid)


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
