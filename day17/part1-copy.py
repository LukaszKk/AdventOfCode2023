import os
import heapq

input_file = "input.txt"


def process_input(lines):
    return [list(map(int, list(line.strip()))) for line in lines]


def print_grid(grid):
    for y in range(len(grid)):
        for x in range(len(grid[0])):
            print(grid[y][x], end="")
        print()
    print()


def dijkstra(graph, start, end):
    max_rows, max_cols = len(graph), len(graph[0])
    directions = [{"direction": "right", "coord": (0, 1)},
                  {"direction": "left", "coord": (0, -1)},
                  {"direction": "down", "coord": (1, 0)},
                  {"direction": "up", "coord": (-1, 0)}]
    heap = [(graph[start[0]][start[1]], start, {"direction": directions[0]["direction"], "length": 0}, [])]
    distances = {start: 0}
    visited = set()

    while heap:
        distance, current, current_direction, path = heapq.heappop(heap)
        if current == end:
            for y in range(len(graph)):
                for x in range(len(graph[0])):
                    if (y, x) in path:
                        print("#", end="")
                    else:
                        print(graph[y][x], end="")
                print()
            print()
            return distances[end]

        for direction in directions:
            dy, dx = direction["coord"][0], direction["coord"][1]
            y, x = current[0] + dy, current[1] + dx

            new_length = 0
            new_direction = direction["direction"]
            if new_direction == current_direction["direction"]:
                new_length = current_direction["length"] + 1

            if (0 <= y < max_rows) and (0 <= x < max_cols) and (new_length < 4):
                new_distance = distance + graph[y][x]

                if ((y, x) not in distances) or (new_distance < distances[(y, x)]):

                    if (y, x) in visited:
                        continue
                    visited.add((y, x))

                    distances[(y, x)] = new_distance
                    heapq.heappush(
                        heap,
                        (
                            new_distance,
                            (y, x),
                            {"direction": new_direction, "length": new_length},
                            path + [(y, x)]
                        )
                    )

    return float('inf')


def calculate(lines: list[str]) -> int:
    grid = process_input(lines)
    print_grid(grid)

    start = (0, 0)
    end = (len(grid) - 1, len(grid[0]) - 1)
    return dijkstra(grid, start, end)


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
