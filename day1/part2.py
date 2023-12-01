import os
import regex

digits_dict = {"one": 1,
               "two": 2,
               "three": 3,
               "four": 4,
               "five": 5,
               "six": 6,
               "seven": 7,
               "eight": 8,
               "nine": 9}


def calculate(lines):
    ret = 0
    digits_re_string = "|".join(digits_dict.keys())
    print(digits_re_string)
    li = 1
    for line in lines:
        digits = regex.findall(rf"\d|{digits_re_string}", line, overlapped=True)
        first = digits[0]
        last = digits[-1]

        try:
            first_num = digits_dict[first]
        except KeyError:
            first_num = int(first)
        try:
            last_num = digits_dict[last]
        except KeyError:
            last_num = int(last)

        number = first_num * 10 + last_num
        print(str(li) + ": " + str(number))
        ret += number
        li += 1
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
