import os
from itertools import product

input_file = "input.txt"


def generate_solution(record_len):
    elements = [".", "#"]
    return list(product(elements, repeat=record_len))


def find_all_possible_solutions(solutions, record):
    possible_solutions = []
    for combo in solutions:
        is_ok = True
        for r, c in zip(record, combo):
            if ((r == ".") and (r != c)) or ((r == "#") and (r != c)):
                is_ok = False
                break
        if is_ok:
            possible_solutions.append(combo)
    return possible_solutions


def verify_solution(solutions, condition):
    ok_solutions = []
    for combo in solutions:
        hashes = []
        hash_count = 0
        for c in combo:
            if c == "#":
                hash_count += 1
            elif c == "." and hash_count > 0:
                hashes.append(hash_count)
                hash_count = 0
        if hash_count > 0:
            hashes.append(hash_count)

        is_ok = True
        for h, c in zip(hashes, condition):
            if h != c:
                is_ok = False
                break

        if (len(hashes) == len(condition)) and is_ok:
            ok_solutions.append(combo)

    return len(ok_solutions)


def calculate(lines: list[str]) -> int:
    res = 0
    i = 1
    for line in lines:
        data = line.strip().split(" ")
        record = tuple(data[0])
        condition = [int(el) for el in data[1].split(",")]
        record_len = len(record)

        solutions = generate_solution(record_len)
        solutions = find_all_possible_solutions(solutions, record)

        arrangements = verify_solution(solutions, condition)

        print(f"{i}. {''.join(record)} : {','.join(map(str, condition))} : {arrangements}")

        res += arrangements
        i += 1

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
