import os

input_file = "input.txt"


def has_reflection(pattern):
    indexes = []
    for y in range(len(pattern) - 1):
        indexes.append(y)

    is_reflected = False
    reflection_index = 0
    for index in indexes:
        differences = 0
        for left_index in range(index, -1, -1):
            right_index = index + (index - left_index) + 1

            if right_index > len(pattern) - 1:
                continue

            for left, right in zip(pattern[left_index], pattern[right_index]):
                if left != right:
                    differences += 1

        # print(f"{differences} : {index}")
        if differences == 1:
            reflection_index = index
            is_reflected = True
            break

    return is_reflected, reflection_index + 1


def calculate(lines: list[str]) -> int:
    res = 0
    patterns = process_input(lines)
    i = 1
    for pattern in patterns:
        print(f"\nPattern {i}")
        i += 1

        pattern_copy = pattern.copy()

        is_reflected_horizontal, value_horizontal = has_reflection(pattern_copy)

        transpose = list([list(el) for el in zip(*pattern)])
        is_reflected_vertical, value_vertical = has_reflection(transpose)

        if is_reflected_horizontal:
            value_horizontal *= 100
            res += value_horizontal

            print(f"Horizontal: {value_horizontal}")
            [print("".join(row)) for row in pattern_copy]
        elif is_reflected_vertical:
            res += value_vertical

            print(f"Vertical: {value_vertical}")
            [print("".join(row)) for row in pattern]

    return res


def process_input(lines):
    pattern = []
    length = len(lines)
    for i, line in enumerate(lines):
        if not line.strip():
            yield pattern
            pattern.clear()
            continue
        elif i == length - 1:
            pattern.append(list(line.strip()))
            yield pattern

        pattern.append(list(line.strip()))


def read_input() -> list[str]:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(f"{current_dir}/{input_file}", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print()
    print(f"Result: {output}")


if __name__ == "__main__":
    main()
