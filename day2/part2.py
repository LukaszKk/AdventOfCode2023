import os


def calculate(lines):
    ret = 0
    for line in lines:
        data_limit = {"red": 0, "green": 0, "blue": 0}

        details = line.split(":")
        reaches = details[1].split(";")

        for reach in reaches:
            cubes = reach.split(",")

            for cube in cubes:
                cube_detail = cube.strip().split(" ")
                cube_amount = int(cube_detail[0])
                cube_color = cube_detail[1]
                if cube_amount > data_limit[cube_color]:
                    data_limit[cube_color] = cube_amount

        power = data_limit["red"] * data_limit["green"] * data_limit["blue"]
        ret += power

    return ret


def read_input() -> list[str]:
    current_dir = os.path.dirname(os.path.realpath(__file__))
    with open(current_dir + "/input.txt", "r") as f:
        return f.readlines()


def main():
    lines = read_input()
    output = calculate(lines)
    print(output)


if __name__ == "__main__":
    main()
