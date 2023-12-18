import os

input_file = "input.txt"


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
    def __init__(self, position=[0, 0], direction="right"):
        self.position = position
        self.direction = direction


def calculate(lines: list[str]) -> int:
    layout = process_input(lines)
    move = Move(len(layout), len(layout[0]))
    res = 0

    beams_starters = ([Beam([0, x], "down") for x in range(len(layout[0]))] +
                      [Beam([y, 0], "right") for y in range(len(layout))] +
                      [Beam([len(layout) - 1, x], "up") for x in range(len(layout[0]))] +
                      [Beam([y, len(layout[0]) - 1], "left") for y in range(len(layout))])

    for beam_starter_idx, beam_start in enumerate(beams_starters):
        beams = [beam_start]
        energized = set()
        beam_tracking = set()

        print(f"Beam: {beam_starter_idx + 1}")

        while beams:
            beams_copy = beams.copy()
            new_beams = []
            to_delete_beams = []

            for idx, beam in enumerate(beams_copy):
                if ((beam.position[0] >= move.max_y) or (beam.position[0] < 0) or
                        (beam.position[1] >= move.max_x) or (beam.position[1] < 0)):
                    to_delete_beams.append(idx)
                    continue

                y = beam.position[0]
                x = beam.position[1]

                energized.add((y, x))

                current_char = layout[y][x]
                if current_char in move.special_chars:
                    interaction = move.interaction[(beam.direction, current_char)]
                    if type(interaction) is list:
                        new_interaction = interaction[1]
                        new_position = [y + new_interaction["position"][0], x + new_interaction["position"][1]]
                        new_direction = new_interaction["new_direction"]
                        new_beam = Beam(new_position, new_direction)

                        if (tuple(new_beam.position), new_beam.direction) not in beam_tracking:
                            beam_tracking.add((tuple(new_beam.position), new_beam.direction))
                            new_beams.append(new_beam)

                        interaction = interaction[0]

                    new_y = y + interaction["position"][0]
                    new_x = x + interaction["position"][1]
                    beam.position = [new_y, new_x]
                    beam.direction = interaction["new_direction"]
                else:
                    new_y = y + move.direction[beam.direction][0]
                    new_x = x + move.direction[beam.direction][1]
                    beam.position = [new_y, new_x]

                if (tuple(beam.position), beam.direction) in beam_tracking:
                    to_delete_beams.append(idx)
                else:
                    beam_tracking.add((tuple(beam.position), beam.direction))

            if to_delete_beams:
                for idx in to_delete_beams[::-1]:
                    beams.pop(idx)
            beams += new_beams

        energized_sum = len(energized)
        if res < energized_sum:
            res = energized_sum

    return res


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
