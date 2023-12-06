import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    res = 1
    times, record_distances = process_input(lines)
    for time, record_distance in zip(times, record_distances):
        sol_count = 0
        for current_speed in range(1, time):
            distance = current_speed * (time - current_speed)
            if distance > record_distance:
                sol_count += 1
        res *= sol_count

    return res


def process_input(lines: list[str]) -> tuple[list[int], list[int]]:
    times = [int(el) for el in lines[0].split(":")[1].strip().split()]
    distances = [int(el) for el in lines[1].split(":")[1].strip().split()]
    return times, distances


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
