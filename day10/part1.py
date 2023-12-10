import os

input_file = "test_input.txt"

next_options = {
    "south": (1, 0),
    "east": (0, -1),
    "north": (-1, 0),
    "west": (0, 1),
}

pipe = {
    "|": {"north": next_options["north"], "south": next_options["south"]},
    "-": {"east": next_options["east"], "west": next_options["west"]},
    "L": {"north": next_options["north"], "east": next_options["east"]},
    "J": {"north": next_options["north"], "west": next_options["west"]},
    "F": {"south": next_options["south"], "east": next_options["east"]},
    "7": {"south": next_options["south"], "west": next_options["west"]},
}

next_pipe_options = {
    ("south", "|"): ("|", "L", "J"),
    ("north", "|"): ("|", "F", "7"),
    ("east", "-"): ("-", "J", "7"),
    ("west", "-"): ("-", "L", "F"),
    ("north", "L"): ("|", "F", "7"),
    ("east", "L"): ("-", "7", "J"),
    ("north", "J"): ("|", "F", "7"),
    ("west", "J"): ("-", "F", "L"),
    ("south", "F"): ("|", "L", "J"),
    ("east", "F"): ("-", "J", "7"),
    ("south", "7"): ("|", "L", "J"),
    ("west", "7"): ("-", "F", "L"),
}


def calculate(lines: list[str]) -> int:
    pipe_map = process_input(lines)
    for y in range(len(pipe_map)):
        for x in range(len(pipe_map[y])):
            print(pipe_map[y][x], end="")
        print()

    s = find_char_position(pipe_map, "S")
    distances = traverse_path(pipe_map, s)
    print()
    print(distances)
    # print(distances[len(distances) // 2])
    print()

    return 0 if not distances else distances[len(distances) // 2]


def traverse_path(pipe_map: list[list], s: tuple[int, int]) -> list[int]:
    distances = []
    current = s
    i = 1
    found_s = False
    while i < 3:
        found_next = False
        for next_option_direction, next_option_id_values in next_options.items():
            if (0 <= current[0] + next_option_id_values[0] <= len(pipe_map)) \
                    and (0 <= current[1] + next_option_id_values[1] <= len(pipe_map[0])):
                next_id = (current[0] + next_option_id_values[0], current[1] + next_option_id_values[1])
                next_char = pipe_map[next_id[0]][next_id[1]]
                print(next_char)

                if next_char == "S":
                    found_s = True
                    break

                if next_char == ".":
                    continue

                try:
                    next_next_pipe_options = next_pipe_options[(next_option_direction, next_char)]
                    print(next_next_pipe_options)
                except KeyError:
                    continue

                for next_next_option in next_next_pipe_options:
                    try:
                        next_next_id = (next_id[0] + pipe[next_next_option][next_option_direction][0],
                                        next_id[1] + pipe[next_next_option][next_option_direction][1])

                        # if (0 <= next_next_id[0] <= len(pipe_map)) \
                        #         and (0 <= next_next_id[1] <= len(pipe_map[0])):

                        next_next_char = pipe_map[next_next_id[0]][next_next_id[1]]
                        print(next_next_char)

                        current = next_id

                        distances.append(i)
                        found_next = True
                        break
                    except KeyError:
                        continue

                if found_next:
                    break

        if found_s:
            distances.append(1)
            break

        i += 1

    return distances


def find_char_position(arr, char):
    for y in range(len(arr)):
        for x in range(len(arr[y])):
            if arr[y][x] == char:
                return y, x
    return None


def process_input(lines: list[str]) -> list[list]:
    pipe_map = list([])
    for line in lines:
        pipe_map.append(list(line.strip()))
    return pipe_map


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
