import os

input_file = "input.txt"


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


def fix_reflection(pattern, ignore_indexes=[]):
    for i in range(len(pattern)):
        for j in range(i + 1, len(pattern)):
            list1 = pattern[i]
            list2 = pattern[j]
            difference = [idx for idx, (x, y) in enumerate(zip(list1, list2)) if x != y]

            if (len(difference) == 1) and (difference[0] not in ignore_indexes):
                pattern[i][difference[0]] = "#" if pattern[i][difference[0]] == "." else "."

                print(difference)
                print(f"{i}: {list1}")
                print(f"{j}: {list2}")

                return pattern, difference[0]

    return pattern, None


def calculate(lines: list[str]) -> int:
    res = 0
    patterns = process_input(lines)
    i = 1
    for pattern in patterns:
        print(f"\nPattern {i}")
        i += 1

        ignore_indexes_horizontal = []
        ignore_indexes_vertical = []
        j = 0

        while True:
            pattern_copy = pattern.copy()

            print("horizontal")
            pattern_copy, idx = fix_reflection(pattern_copy, ignore_indexes_horizontal)
            ignore_indexes_horizontal.append(idx)
            is_reflected_horizontal, value_horizontal = has_reflection(pattern_copy)

            print("vertical")
            transpose = list([list(el) for el in zip(*pattern)])
            transpose, idx = fix_reflection(transpose, ignore_indexes_vertical)
            ignore_indexes_vertical.append(idx)
            is_reflected_vertical, value_vertical = has_reflection(transpose)

            if is_reflected_horizontal:
                value_horizontal *= 100
                res += value_horizontal

                # print(f"Horizontal: {value}")
                [print("".join(row)) for row in pattern_copy]
                j = 0
                break
            elif is_reflected_vertical:
                res += value_vertical

                # print(f"Vertical: {value}")
                [print("".join(row)) for row in pattern]
                j = 0
                break
            else:
                # print(f"\nPattern {i - 1}")
                # [print("".join(row)) for row in pattern]
                j += 1

            if j == 1000:
                raise Exception("ERORR")

    # wrong: 36293
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
