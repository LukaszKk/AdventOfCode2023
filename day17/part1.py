import os
from queue import PriorityQueue

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
    def __init__(self, y, x, weight, previous=None, heuristic=float('inf')):
        self.y = y
        self.x = x
        self.weight = weight
        self.heuristic = heuristic
        self.previous = previous

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

    def __lt__(self, other):
        return self.weight < other.weight


def manhattan_distance(a: Node, b: Node) -> float:
    return abs(a.y - b.y) + abs(a.x - b.x)


def a_star_search(grid, start: Node, end: Node):
    queue = PriorityQueue()
    queue.put((start.heuristic, start))

    distances = {(start.y, start.x): 0}

    while not queue.empty():
        current_distance, current = queue.get()

        if current == end:
            return current

        neighbours = [
            (current.y, current.x + 1),
            (current.y, current.x - 1),
            (current.y + 1, current.x),
            (current.y - 1, current.x),
        ]

        for y, x in neighbours:
            if (0 <= y < len(grid)) and (0 <= x < len(grid[y])):
                new_distance = current_distance + grid[y][x]

                if ((y, x) not in distances) or (new_distance < distances[(y, x)]):
                    distances[(y, x)] = new_distance

                    next_node = Node(y, x, new_distance, current)
                    next_node.heuristic = new_distance + manhattan_distance(next_node, end)
                    queue.put((next_node.heuristic, next_node))

    return None


def calculate(lines: list[str]) -> int:
    grid = process_input(lines)
    print_grid(grid)

    start = Node(0, 0, grid[0][0])
    end = Node(len(grid) - 1, len(grid[0]) - 1, grid[len(grid) - 1][len(grid[0]) - 1])
    node = a_star_search(grid, start, end)
    print((node.y, node.x))
    path = []
    while node.previous:
        path.append((node.y, node.x))
        node = node.previous
    print(path)
    print_grid(grid, path)
    # return distance


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
