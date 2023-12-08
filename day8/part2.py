import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    instructions, network = process_input(lines)
    print(instructions)
    print(network)
    curr_node = network["AAA"]
    instr_index = 0
    move_count = 0
    while move_count < 10**10:
        curr_node_id = curr_node[0] if instructions[instr_index] == "L" else curr_node[1]
        if curr_node_id == "ZZZ":
            return move_count + 1

        curr_node = network[curr_node_id]
        print(f"{curr_node_id} : {curr_node}")

        move_count += 1
        if instr_index == len(instructions) - 1:
            instr_index = 0
        else:
            instr_index += 1
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
