import os

input_file = "test_input.txt"


def hash_value(string):
    res = 0
    for letter in string:
        value = ord(letter)
        res += value
        res *= 17
        res %= 256
    return res


def calculate(lines: list[str]) -> int:
    values = lines[0].strip().split(",")
    res = 0

    for value in values:
        res += hash_value(value)

    return res


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
