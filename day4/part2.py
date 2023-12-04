import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    max_len = len(lines)
    instances = [1] * max_len

    for line in lines:
        data = line.split(":")
        card_num = int(data[0].replace("Card", "").strip())

        num_data = data[1].split("|")
        wining_data = " ".join((num_data[0].split())).split()
        actual_data = " ".join((num_data[1].split())).split()
        won_amount = sum(el in wining_data for el in actual_data)

        current_card_index = card_num - 1
        current_card_instances = instances[current_card_index]
        for i in range(1, won_amount + 1):
            if current_card_index + i < max_len:
                instances[current_card_index + i] += current_card_instances

        print(f"{card_num} / {max_len}: {wining_data} || {actual_data}: {won_amount}: {current_card_instances}")
    return sum(el for el in instances)


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
