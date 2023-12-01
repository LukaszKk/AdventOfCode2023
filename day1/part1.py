import os
import re


def calculate(lines):
    ret = 0
    li = 1
    for line in lines:
        reversed_line = line[::-1]
        first = re.search(r"\d", line)
        last = re.search(r"\d", reversed_line)
        number = line[first.start()] + reversed_line[last.start()]
        print(str(li) + ": " + number)
        li += 1
        ret += int(number)
    return ret


def read_input() -> list[str]:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(output)


if __name__ == "__main__":
    main()
