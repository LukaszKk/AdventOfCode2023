import os
from functools import cache

input_file = "input.txt"


def process_input(lines):
    return tuple(tuple(line.strip()) for line in lines)


def print_platform(arr):
    for y in arr:
        for x in y:
            print(x, end="")
        print()
    print()


@cache
def transpose(arr):
    return tuple([tuple(el) for el in zip(*arr)])


@cache
def move(platform):
    arr = [list(t) for t in platform]
    for j, line in enumerate(arr):
        dots_pos = []
        for i, el in enumerate(line):
            if el == "O":
                try:
                    dot_i = dots_pos.pop(0)
                    line[i], line[dot_i] = line[dot_i], line[i]
                    el = line[i]
                except IndexError:
                    continue

            if el == "#":
                dots_pos.clear()
                continue
            if el == ".":
                dots_pos.append(i)
                continue

    return tuple([tuple(t) for t in arr])


@cache
def calc_res(platform):
    arr = [list(t) for t in platform]
    res = 0
    multiplier = len(arr)
    for line in arr:
        o_count = line.count("O")
        res += o_count * multiplier
        multiplier -= 1
    return res


@cache
def left_to_right(platform):
    arr = [list(t) for t in platform]
    for line in arr:
        left = 0
        right = len(line) - 1
        while left < right:
            line[left], line[right] = line[right], line[left]
            left += 1
            right -= 1

    return tuple([tuple(t) for t in arr])


def calculate(lines: list[str]):
    platform = process_input(lines)
    print_platform(platform)

    i = 0
    # cycle_count = 1000000000
    cycle_count = 1000

    while i < cycle_count:
        # north
        platform = transpose(platform)
        platform = move(platform)
        platform = transpose(platform)
        # print("To north")
        # print_platform(platform)

        # west
        platform = move(platform)
        # print("To west")
        # print_platform(platform)

        # south
        platform = transpose(platform)
        platform = left_to_right(platform)
        platform = move(platform)
        platform = left_to_right(platform)
        platform = transpose(platform)
        # print("To south")
        # print_platform(platform)

        # east
        platform = left_to_right(platform)
        platform = move(platform)
        platform = left_to_right(platform)
        # print("To east")
        # print_platform(platform)

        # print_platform(platform)
        print(f"{i + 1}: {calc_res(platform)}")

        i += 1

    return calc_res(platform)


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
