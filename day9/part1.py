import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    res = 0
    histories = process_input(lines)
    print(histories)

    for history in histories:
        prev_list = []
        differences = history.copy()

        while not all(element == 0 for element in differences):
            for i in range(0, len(differences) - 1):
                diff_1 = differences[i]
                diff_2 = differences[i + 1]

                if i + 1 == len(differences) - 1:
                    prev_list.insert(0, diff_2)

                differences[i] = diff_2 - diff_1
            differences.pop()

        next_el = 0
        for prev_el in prev_list:
            next_el = next_el + prev_el

        res += next_el

    return res


def process_input(lines: list[str]) -> list[list[int]]:
    histories = []
    for line in lines:
        histories.append([int(el) for el in line.strip().split()])
    return histories


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
