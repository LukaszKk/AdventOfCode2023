import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    instructions, network = process_input(lines)
    print(instructions)
    print(network, end="\n\n")

    curr_node_list = [el for el in network if el[2] == "A"]
    length = len(curr_node_list)
    print(f"{curr_node_list} : 0")
    move_count = 0
    instruction_index = 0

    while move_count < 1000000:
        z_nodes_count = 0
        for i, curr_node in enumerate(curr_node_list):
            next_node_id = network[curr_node][0] if instructions[instruction_index] == "L" else network[curr_node][1]
            if next_node_id[2] == "Z":
                z_nodes_count += 1
            curr_node_list[i] = next_node_id

        if sum([1 if el[2] == "Z" else 0 for el in curr_node_list]) == 2:
            print(f"{curr_node_list} : {move_count + 1}")

        if z_nodes_count == length:
            return move_count + 1

        move_count += 1
        instruction_index = 0 if instruction_index == len(instructions) - 1 else instruction_index + 1
    return -1


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
