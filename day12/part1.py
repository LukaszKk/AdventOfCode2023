import os

input_file = "input.txt"


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


def generate_combinations(elements, max_length, record, current_index=0, current_combination=[]):
    if len(current_combination) == max_length:
        yield current_combination
        return

    for element in elements:
        if element == record[current_index] or record[current_index] == "?":
            yield from generate_combinations(elements, max_length,
                                             record, current_index + 1,
                                             current_combination + [element])


def calculate(lines: list[str]) -> int:
    res = 0
    i = 1
    elements = [".", "#"]

    for line in lines:
        data = line.strip().split(" ")

        record = tuple(data[0])
        condition = [int(el) for el in data[1].split(",")]
        record_len = len(record)

        solutions = list(generate_combinations(elements, record_len, record))
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
