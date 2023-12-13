import os

input_file = "test_input.txt"


def has_reflection(pattern):
    indexes = []
    for y in range(len(pattern) - 1):
        if pattern[y] == pattern[y + 1]:
            indexes.append(y)

    is_reflected = False
    reflection_index = 0
    for index in indexes:
        is_reflected = True

        for left_index in range(index - 1, -1, -1):
            right_index = index + (index - left_index) + 1
            if right_index > len(pattern) - 1:
                break

            if pattern[left_index] != pattern[right_index]:
                is_reflected = False
                break

        if is_reflected:
            reflection_index = index
            break

    return is_reflected, reflection_index + 1


def calculate(lines: list[str]) -> int:
    res = 0
    patterns = process_input(lines)
    i = 1
    for pattern in patterns:
        print(f"\nPattern {i}")
        i += 1

        transpose = list(zip(*pattern))
        is_reflected, value = has_reflection(transpose)
        if is_reflected:
            res += value

            print(f"Vertical: {value}")
            [print("".join(row)) for row in pattern]
            continue

        is_reflected, value = has_reflection(pattern)
        if is_reflected:
            value *= 100
            res += value

            print(f"Horizontal: {value}")
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
