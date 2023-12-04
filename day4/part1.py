import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    res = 0
    for line in lines:
        data = line.split(":")[1].split("|")
        wining_data = " ".join((data[0].split())).split()
        actual_data = " ".join((data[1].split())).split()
        won_amount = sum(el in wining_data for el in actual_data)

        curr_points = 0
        if won_amount >= 1:
            curr_points = 1
            won_amount -= 1
        curr_points = curr_points << won_amount

        res += curr_points

        print(f"{wining_data} / {actual_data}: {won_amount} - {curr_points}")
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
