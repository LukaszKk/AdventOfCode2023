import os
import numpy as np

input_file = "/input.txt"
adjacent_ids = [(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (-1, 1), (1, -1), (1, 1)]


def calculate(arr: np.ndarray):
    ret = 0
    shape = arr.shape
    adjacent_store = []
    for y in range(shape[0]):
        numbers = []
        for x in range(shape[1]):
            char: str = arr[y, x]
            if char.isdigit():
                numbers.append({"num": int(char), "pos": (y, x)})

            if (x == shape[1] - 1) or (char == "." or not char.isdigit()):
                num = 0

                if numbers:
                    is_adjacent = False
                    adjacent_temp_stored = []

                    for data in numbers:
                        num = num * 10 + data["num"]

                        for adjacent_idx in adjacent_ids:
                            adjacent_y = data["pos"][0] + adjacent_idx[0]
                            adjacent_x = data["pos"][1] + adjacent_idx[1]

                            if adjacent_y < 0 or adjacent_y >= shape[0] or adjacent_x < 0 or adjacent_x >= shape[1]:
                                continue

                            adjacent_char: str = arr[adjacent_y, adjacent_x]
                            if adjacent_char == "*":
                                is_adjacent = True
                                adj_pos = {"adj_pos": (adjacent_y, adjacent_x)}
                                if adj_pos not in adjacent_temp_stored:
                                    adjacent_temp_stored.append(adj_pos)
                                # print(adjacent_char)

                    if is_adjacent:
                        adjacent_store.append(*[{"num": num, **adj} for adj in adjacent_temp_stored])
                        # print(adjacent_store)

                numbers = []

    for i, element in enumerate(adjacent_store):
        for j in range(i + 1, len(adjacent_store)):
            search_element = adjacent_store[j]
            if element["adj_pos"] == search_element["adj_pos"]:
                ret += element["num"] * search_element["num"]

    return ret


def read_input() -> np.ndarray:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + input_file, "r") as f:
        return np.array([list(line.strip().replace("\n", "")) for line in f.readlines()])


def main():
    lines = read_input()
    output = calculate(lines)
    print(F"Result: {output}")


if __name__ == "__main__":
    main()
