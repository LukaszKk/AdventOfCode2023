import os

input_file = "input.txt"

cards_figure = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]


def calculate(lines: list[str]) -> int:
    rank = process_input(lines)
    [print(el["cards"]) for el in rank]
    res = 0
    for i in range(1, len(rank) + 1):
        res += rank[i - 1]["bid"] * i
    return res


def process_input(lines: list[str]) -> list[dict]:
    five = []
    four = []
    full = []
    three = []
    two = []
    one = []
    none = []
    for line in lines:
        data = line.split()
        cards = data[0]
        counts = [duplicate_count(cards, cards[0]), duplicate_count(cards, cards[1]), duplicate_count(cards, cards[2]),
                  duplicate_count(cards, cards[3]), duplicate_count(cards, cards[4])]

        # print(f"{cards}: {counts}")

        if 5 in counts:
            five.append({"cards": cards, "bid": int(data[1])})
        elif 4 in counts:
            four.append({"cards": cards, "bid": int(data[1])})
        elif 3 in counts and 2 in counts:
            full.append({"cards": cards, "bid": int(data[1])})
        elif 3 in counts:
            three.append({"cards": cards, "bid": int(data[1])})
        elif counts.count(2) == 4:
            two.append({"cards": cards, "bid": int(data[1])})
        elif counts.count(2) == 2:
            one.append({"cards": cards, "bid": int(data[1])})
        else:
            none.append({"cards": cards, "bid": int(data[1])})

    # print(one)
    # print(two)
    # print(three)
    # print(full)
    # print(four)
    # print(five)
    # print()
    #
    # print(none + one + two + three + full + four + five)

    sort_cards(none)
    sort_cards(one)
    sort_cards(two)
    sort_cards(three)
    sort_cards(full)
    sort_cards(four)
    sort_cards(five)

    return none + one + two + three + full + four + five


def sort_cards(cards_rank: list[dict]):
    length = len(cards_rank)
    for i in range(length - 1):
        for j in range(0, length - i - 1):
            cards_j = cards_rank[j]["cards"]
            cards_j_o = cards_rank[j + 1]["cards"]

            for k in range(0, len(cards_j)):
                if cards_compare(cards_j[k], cards_j_o[k]) == 1:
                    cards_rank[j], cards_rank[j + 1] = cards_rank[j + 1], cards_rank[j]
                    break
                elif cards_compare(cards_j[k], cards_j_o[k]) == -1:
                    break


def cards_compare(card_1: str, card_2: str):
    index_1 = cards_figure.index(card_1)
    index_2 = cards_figure.index(card_2)
    if index_1 < index_2:
        return 1
    elif index_1 > index_2:
        return -1
    return 0


def duplicate_count(text: str, char: str) -> int:
    return text.count(char)


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
