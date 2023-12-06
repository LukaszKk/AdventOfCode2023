import os

input_file = "input.txt"


def calculate(lines: list[str]) -> int:
    time, record_distance = process_input(lines)
    sol_count = 0
    for current_speed in range(1, time):
        distance = current_speed * (time - current_speed)
        if distance > record_distance:
            sol_count += 1

    return sol_count


def process_input(lines: list[str]) -> tuple[int, int]:
    return int("".join(lines[0].split(":")[1].split())), int("".join(lines[1].split(":")[1].split()))


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
