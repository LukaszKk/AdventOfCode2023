import os
from queue import PriorityQueue

input_file = "test_2_input.txt"


def process_input(lines):
    return [list(map(int, list(line.strip()))) for line in lines]


def print_grid(grid, hash_points=()):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            if (y, x) in hash_points:
                print("#", end="")
            else:
                print(grid[y][x], end="")
        print()
    print()


def modified_dijkstra(grid):
    max_y, max_x = len(grid) - 1, len(grid[0]) - 1
    start_y, start_x, end_y, end_x = 0, 0, max_y, max_x

    directions = [
        {"direction": "r", "coord": (0, 1)},
        {"direction": "l", "coord": (0, -1)},
        {"direction": "d", "coord": (1, 0)},
        {"direction": "u", "coord": (-1, 0)}
    ]

    reverse_direction = {
        "r": "l",
        "l": "r",
        "u": "d",
        "d": "u"
    }

    q = PriorityQueue()
    q.put((0, (start_y, start_x, "r", 0, [])))
    distances = dict()

    while q:
        curr_distance, (curr_y, curr_x, curr_direction, curr_direction_length, curr_path) = q.get()

        if (curr_y == end_y) and (curr_x == end_x):
            return curr_distance, curr_path

        available_directions = directions.copy()
        if curr_direction_length == 2:
            available_directions = [el for el in available_directions if el["direction"] != curr_direction]

        for direct in available_directions:
            new_y, new_x = curr_y + direct["coord"][0], curr_x + direct["coord"][1]

            if (0 <= new_y <= max_y) and (0 <= new_x <= max_x):
                new_distance = curr_distance + grid[new_y][new_x]

                if ((new_y, new_x) not in distances.keys()) or (new_distance < distances[(new_y, new_x)]):
                    new_direction = direct["direction"]
                    new_direction_length = 0

                    if new_direction == reverse_direction[curr_direction]:
                        continue
                    if new_direction == curr_direction:
                        new_direction_length = curr_direction_length + 1

                    distances[(new_y, new_x)] = new_distance

                    q.put((new_distance, (
                        new_y,
                        new_x,
                        new_direction,
                        new_direction_length,
                        curr_path + [(new_y, new_x)]
                    )))

    return float('inf'), []


def calculate(lines: list[str]) -> int:
    grid = process_input(lines)
    print_grid(grid)
    distance, hash_points = modified_dijkstra(grid)
    print_grid(grid, hash_points)
    return distance


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
