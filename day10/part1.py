import os

input_file = "test_input.txt"

next_options = {
    "south": (1, 0),
    "east": (0, 1),
    "north": (-1, 0),
    "west": (0, -1),
}

pipe = {
    "|": {"north": "north", "south": "south"},
    "-": {"west": "west", "east": "east"},
    "L": {"south": "east", "west": "north"},
    "J": {"south": "west", "east": "north"},
    "F": {"north": "east", "west": "south"},
    "7": {"north": "west", "east": "south"},
}

next_pipe_options = {
    ("south", "|"): ("|", "L", "J"),
    ("north", "|"): ("|", "F", "7"),
    ("east", "-"): ("-", "J", "7"),
    ("west", "-"): ("-", "L", "F"),
    ("south", "L"): ("-", "7", "J"),
    ("west", "L"): ("|", "F", "7"),
    ("east", "J"): ("-", "F", "L"),
    ("south", "J"): ("|", "F", "7"),
    ("north", "F"): ("-", "J", "7"),
    ("west", "F"): ("|", "L", "J"),
    ("north", "7"): ("-", "F", "L"),
    ("east", "7"): ("|", "L", "J"),
}


def calculate(lines: list[str]) -> int:
    pipe_map = process_input(lines)
    for y in range(len(pipe_map)):
        for x in range(len(pipe_map[y])):
            print(pipe_map[y][x], end="")
        print()
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
    already_visited = []
    current = s
    i = 1
    found_s = False

    while i < 8:
        print()
        found_next = False
        for next_option_direction, next_option_id_values in next_options.items():

            if not (0 <= current[0] + next_option_id_values[0] < len(pipe_map)) \
                    or not (0 <= current[1] + next_option_id_values[1] < len(pipe_map[0])):
                continue

            next_id = (current[0] + next_option_id_values[0], current[1] + next_option_id_values[1])
            next_char = pipe_map[next_id[0]][next_id[1]]

            if next_id in already_visited:
                continue

            if next_char == "S":
                found_s = True
                break

            if next_char == ".":
                continue

            print(next_char)

            try:
                next_next_pipe_options = next_pipe_options[(next_option_direction, next_char)]
            except KeyError:
                continue

            for next_next_option in next_next_pipe_options:
                try:
                    next_next_option_direction = pipe[next_char][next_option_direction]

                    next_next_id = (next_id[0] + next_options[next_next_option_direction][0],
                                    next_id[1] + next_options[next_next_option_direction][1])

                    next_next_char = pipe_map[next_next_id[0]][next_next_id[1]]
                    if next_next_char != next_next_option:
                        continue


                    already_visited.append(next_id)
                    current = next_id

                    print(next_next_char)
                    print(current)
                    print(pipe_map[current[0]][current[1]])

                    distances.append(i)
                    found_next = True
                    break
                except KeyError:
                    continue
                except IndexError:
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
