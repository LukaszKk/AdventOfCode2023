import os

input_file = "input.txt"


def hash_value(string):
    res = 0
    for letter in string:
        value = ord(letter)
        res += value
        res *= 17
        res %= 256
    return res


def calculate(lines: list[str]) -> int:
    steps = lines[0].strip().split(",")
    boxes = [[]] * 256

    for step in steps:
        operation = "=" if "=" in step else "-"
        data = step.split(operation)
        label = data[0]
        box = hash_value(label)

        if operation == "-":
            boxes[box] = [el for i, el in enumerate(boxes[box]) if el.split(" ")[0] != label]
        else:
            focal_length = data[1]
            new_step = f"{label} {focal_length}"
            boxes[box] = [new_step if el.split(" ")[0] == label else el for i, el in enumerate(boxes[box])]
            if new_step not in boxes[box]:
                boxes[box].append(new_step)

    print(boxes)

    focusing_power = 0
    for i, box in enumerate(boxes):
        for j, lens in enumerate(box):
            focal_length = int(lens.split(" ")[1])
            focusing_power += (i + 1) * (j + 1) * focal_length

    return focusing_power


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
