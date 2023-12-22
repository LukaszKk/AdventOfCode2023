import os
from heapq import heappush, heappop

input_file = "test2_input.txt"


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


class Node:
    def __init__(self, y, x, weight, previous=None):
        self.y = y
        self.x = x
        self.weight = weight
        self.heuristic = float('inf')
        self.previous = previous

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __lt__(self, other):
        return self.heuristic < other.heuristic


def heuristic_cost(a: Node, b: Node) -> float:
    return ((a.y - b.y) ** 2 + (a.x - b.x) ** 2) ** 0.5


def a_star_search(grid, start: Node, end: Node):
    movements = [
        {"dir": "r", "coord": (0, 1)},
        {"dir": "l", "coord": (0, -1)},
        {"dir": "d", "coord": (1, 0)},
        {"dir": "u", "coord": (-1, 0)}
    ]

    reverse_dir = {
        "r": "l",
        "l": "r",
        "d": "u",
        "u": "d",
    }

    heap = []
    distances = dict()
    for j in range(len(grid)):
        for i in range(len(grid[j])):
            distances[(j, i)] = float('inf')

    heappush(heap, (0, start))

    while heap:
        current_cost, current_node = heappop(heap)

        if current_node == end:
            return current_node

        for move in movements:
            y = current_node.y + move["coord"][0]
            x = current_node.x + move["coord"][1]

            if y == 0 and x == 5:
                continue

            if (0 <= y < len(grid)) and (0 <= x < len(grid[0])):
                new_weight = current_node.weight + grid[y][x]

                if new_weight < distances[(y, x)]:
                    distances[(y, x)] = new_weight

                    next_node = Node(y, x, new_weight, current_node)

                    new_heuristic = new_weight + heuristic_cost(next_node, end)
                    next_node.heuristic = new_heuristic

                    heappush(heap, (new_heuristic, next_node))

    return None


def calculate(lines: list[str]) -> int:
    grid = process_input(lines)
    print_grid(grid)

    start = Node(0, 0, 0)
    end = Node(len(grid) - 1, len(grid[0]) - 1, grid[len(grid) - 1][len(grid[0]) - 1])
    node = a_star_search(grid, start, end)

    path = []
    distance = 0
    if node:
        distance = node.weight
        while node.previous:
            path.append((node.y, node.x))
            node = node.previous

    print_grid(grid, path)

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
