import os

data_limit = {"red": 12, "green": 13, "blue": 14}


def calculate(lines):
    ret = 0
    for line in lines:
        details = line.split(":")
        game_number = int(details[0].split(" ")[1])
        reaches = details[1].split(";")

        possible_flag = True
        for reach in reaches:
            cubes = reach.split(",")
            for cube in cubes:
                cube_detail = cube.strip().split(" ")
                cube_amount = int(cube_detail[0])
                cube_color = cube_detail[1]
                if cube_amount > data_limit[cube_color]:
                    possible_flag = False

        if possible_flag:
            ret += game_number
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
