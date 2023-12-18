import os

input_file = "test_input.txt"


class Move:
    def __init__(self, max_y, max_x):
        self.max_y = max_y
        self.max_x = max_x

    direction = {
        "right": [0, 1],
        "left": [0, -1],
        "up": [-1, 0],
        "down": [1, 0]
    }

    special_chars = ["|", "-", "/", "\\"]

    interaction = {
        ("right", "|"): [{"position": direction["down"], "new_direction": "down"},
                         {"position": direction["up"], "new_direction": "up"}],
        ("left", "|"): [{"position": direction["down"], "new_direction": "down"},
                        {"position": direction["up"], "new_direction": "up"}],
        ("down", "|"): {"position": direction["down"], "new_direction": "down"},
        ("up", "|"): {"position": direction["up"], "new_direction": "up"},

        ("down", "-"): [{"position": direction["left"], "new_direction": "left"},
                        {"position": direction["right"], "new_direction": "right"}],
        ("up", "-"): [{"position": direction["left"], "new_direction": "left"},
                      {"position": direction["right"], "new_direction": "right"}],
        ("right", "-"): {"position": direction["right"], "new_direction": "right"},
        ("left", "-"): {"position": direction["left"], "new_direction": "left"},

        ("right", "/"): {"position": direction["up"], "new_direction": "up"},
        ("left", "/"): {"position": direction["down"], "new_direction": "down"},
        ("down", "/"): {"position": direction["left"], "new_direction": "left"},
        ("up", "/"): {"position": direction["right"], "new_direction": "right"},

        ("left", "\\"): {"position": direction["up"], "new_direction": "up"},
        ("right", "\\"): {"position": direction["down"], "new_direction": "down"},
        ("up", "\\"): {"position": direction["left"], "new_direction": "left"},
        ("down", "\\"): {"position": direction["right"], "new_direction": "right"},
    }


class Beam:
    def __init__(self, position=[0,0], direction="right"):
        self.position = position
        self.direction = direction
        self.energized_amount = 0
        self.energized_count = 0


def calculate(lines: list[str]) -> int:
    layout = process_input(lines)
    energized = [['.' for _ in range(len(layout[y]))] for y in range(len(layout))]

    print_layout(layout)
    print_layout(energized)

    move = Move(len(layout), len(layout[0]))
    beams = [Beam()]

    i = 0
    j = 1
    while i < 100:
        i += 1
        if i == j * 50:
            print(i)
            j += 1

        for idx, beam in enumerate(beams):
            if ((beam.position[0] >= move.max_y) or (beam.position[0] < 0) or
                    (beam.position[1] >= move.max_x) or (beam.position[1] < 0)):
                beams.pop(idx)
                continue

            y = beam.position[0]
            x = beam.position[1]

            if energized[y][x] != "#":
                beam.energized_amount += 1
                beam.energized_count = 0
            else:
                beam.energized_count += 1
            energized[y][x] = "#"

            if beam.energized_count == 150:
                beams.pop(idx)
                continue

            current_char = layout[y][x]
            if current_char in move.special_chars:
                interaction = move.interaction[(beam.direction, current_char)]
                if type(interaction) is list:
                    new_interaction = interaction[1]
                    new_position = [y + new_interaction["position"][0], x + new_interaction["position"][1]]
                    new_direction = new_interaction["new_direction"]
                    new_beam = Beam(new_position, new_direction)
                    beams.append(new_beam)
                    interaction = interaction[0]

                new_y = y + interaction["position"][0]
                new_x = x + interaction["position"][1]
                beam.position = [new_y, new_x]
                beam.direction = interaction["new_direction"]
            else:
                new_y = y + move.direction[beam.direction][0]
                new_x = x + move.direction[beam.direction][1]
                beam.position = [new_y, new_x]

    print_layout(energized)

    return sum(row.count('#') for row in energized)


def print_layout(arr):
    for y in range(len(arr)):
        for x in range(len(arr[0])):
            print(arr[y][x], end="")
        print()
    print()


def process_input(lines):
    arr = []
    for line in lines:
        arr.append(list(line.strip()))
    return arr


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
