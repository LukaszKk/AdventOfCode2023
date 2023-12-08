import os
import math

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    instructions, network = process_input(lines)
    print(instructions)
    print(network, end="\n\n")

    curr_node_list = [(el, 0) for el in network if el[2] == "A"]
    z_node_indexes = []
    length = len(curr_node_list)
    move_count = 0
    instruction_index = 0

    while move_count < 100000:
        if len(z_node_indexes) == length:
            break
        for i, curr_node in enumerate(curr_node_list):
            if i in z_node_indexes:
                continue
            next_node_id = network[curr_node[0]][0] if instructions[instruction_index] == "L" else network[curr_node[0]][1]
            if next_node_id[2] == "Z":
                z_node_indexes.append(i)
            curr_node_list[i] = (next_node_id, move_count + 1)

        # for i, node in enumerate(curr_node_list):
        #     if node[0][2] == "Z":
        #         print(f"{"." * 14}|" * i, end="")
        #         print(f"{node}", end="")
        #         print(f"|{"." * 14}" * (6 - i - 1), end="")
        #         print(f" : {move_count + 1}")

        move_count += 1
        instruction_index = 0 if instruction_index == len(instructions) - 1 else instruction_index + 1

    indexes = [el[1] for el in curr_node_list]
    return math.lcm(*indexes)


def process_input(lines) -> tuple[str, dict]:
    instructions = ""
    network = {}
    for i, line in enumerate(lines):
        if i == 0:
            instructions = line.strip()
            continue
        if i == 1:
            continue
        data = line.split("=")
        node = data[0].rstrip()
        lr_data = data[1].replace("(", "").replace(")", "").replace(",", "").strip().split()
        left = lr_data[0]
        right = lr_data[1]
        network.update({node: (left, right)})
    return instructions, network


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
