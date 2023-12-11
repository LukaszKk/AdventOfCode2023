import os

# All directions are considered: I went ...

input_file = "input.txt"

next_options = {
    "north": (-1, 0),
    "west": (0, -1),
    "south": (1, 0),
    "east": (0, 1),
}

next_next_direction_converter = {
    "|": {"north": "north", "south": "south"},
    "-": {"west": "west", "east": "east"},
    "L": {"south": "east", "west": "north"},
    "J": {"south": "west", "east": "north"},
    "F": {"north": "east", "west": "south"},
    "7": {"north": "west", "east": "south"},
}

next_direction_pipe_options = {
    ("south", "|"): ("|", "L", "J"),
    ("north", "|"): ("|", "F", "7"),
    ("east", "-"): ("-", "J", "7"),
    ("west", "-"): ("-", "L", "F"),
    ("south", "L"): ("-", "7", "J"),
    ("west", "L"): ("|", "F", "7"),
    ("east", "J"): ("|", "F", "7"),
    ("south", "J"): ("-", "F", "L"),
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
    loop_ids = traverse_path(pipe_map, s)
    print()
    print(loop_ids)
    print()

    new_map = list([])
    for y in range(len(pipe_map)):
        new_map.append([])
        for x in range(len(pipe_map[y])):
            if ((y, x) in loop_ids) or ((y, x) == s):
                new_map[y].append("*")
            else:
                new_map[y].append(".")

    for y in range(len(new_map)):
        for x in range(len(new_map[y])):
            print(new_map[y][x], end="")
        print()
    print()

    enclosed_sum = 0
    for y in range(len(new_map)):
        for x in range(len(new_map[y])):
            if new_map[y][x] == ".":
                enclosed_left = False
                enclosed_right = False
                enclosed_top = False
                enclosed_bottom = False

                for i in range(x, -1, -1):
                    if new_map[y][i] == "*":
                        enclosed_left = True

                for i in range(x, len(new_map[y]), 1):
                    if new_map[y][i] == "*":
                        enclosed_right = True

                for j in range(y, -1, -1):
                    if new_map[j][x] == "*":
                        enclosed_top = True

                for j in range(y, len(new_map), 1):
                    if new_map[j][x] == "*":
                        enclosed_bottom = True

                if enclosed_left and enclosed_right and enclosed_top and enclosed_bottom:
                    enclosed_sum += 1

    # Not right: 734
    return enclosed_sum


def traverse_path(pipe_map: list[list], s: tuple[int, int]) -> list[int]:
    loop_ids = []
    already_visited = []
    current = s
    i = 1
    next_next_char = ""
    next_next_option_direction = ""

    while True:
        found_next = False  # noqa
        for next_direction, next_id_values in next_options.items():

            if not (0 <= current[0] + next_id_values[0] < len(pipe_map)) \
                    or not (0 <= current[1] + next_id_values[1] < len(pipe_map[0])):
                continue

            next_id = (current[0] + next_id_values[0], current[1] + next_id_values[1])
            next_char = pipe_map[next_id[0]][next_id[1]]

            if next_id in already_visited:
                continue

            # if next_char == "S":
            #     found_s = True
            #     break

            if next_char == ".":
                continue

            if next_next_char and next_char != next_next_char:
                continue

            if next_next_option_direction and next_direction != next_next_option_direction:
                continue

            # print()
            # current_char = pipe_map[current[0]][current[1]]
            # print(current_char)
            # print(next_char)

            try:
                next_next_pipe_options = next_direction_pipe_options[(next_direction, next_char)]
            except KeyError:
                continue

            for next_next_option in next_next_pipe_options:
                try:
                    next_next_option_direction = next_next_direction_converter[next_char][next_direction]

                    next_next_id = (next_id[0] + next_options[next_next_option_direction][0],
                                    next_id[1] + next_options[next_next_option_direction][1])

                    next_next_char = pipe_map[next_next_id[0]][next_next_id[1]]
                    if next_next_char != next_next_option:
                        continue

                    already_visited.append(next_id)
                    current = next_id

                    # print(next_next_char)

                    loop_ids.append(current)
                    found_next = True
                    break
                except KeyError:
                    continue
                except IndexError:
                    continue
            else:
                # for s_direction, s_id_val in next_options.items():
                #     s_id = (next_id[0] + next_id_values[0], current[1] + next_id_values[1])
                #     s_char = pipe_map[next_id[0]][next_id[1]]
                # found_s = True
                loop_ids.append(next_id)
                return loop_ids
                # raise Exception("Not found")

            if found_next:
                break

        # if found_s:
        #     distances.append(1)
        #     break

        i += 1

    return loop_ids


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
