import os

input_file = "input.txt"

cards_figure = ["A", "K", "Q", "T", "9", "8", "7", "6", "5", "4", "3", "2", "J"]


def calculate(lines: list[str]) -> int:
    rank = process_input(lines)
    # [print(el["cards"]) for el in rank]
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
        joker_count = cards.count("J")

        duplicates_joker = duplicates_count_plus_joker(counts, joker_count)
        if duplicates_joker == 5:
            five.append({"cards": cards, "bid": int(data[1])})
        elif duplicates_joker == 4:
            four.append({"cards": cards, "bid": int(data[1])})
        elif duplicates_joker == 6:
            full.append({"cards": cards, "bid": int(data[1])})
        elif duplicates_joker == 3:
            three.append({"cards": cards, "bid": int(data[1])})
        elif duplicates_joker == 2:
            two.append({"cards": cards, "bid": int(data[1])})
        elif duplicates_joker == 1:
            one.append({"cards": cards, "bid": int(data[1])})
        else:
            none.append({"cards": cards, "bid": int(data[1])})

        # print(f"{cards}: {counts} : {joker_count} -> {duplicates_joker}")

    sort_cards(none)
    sort_cards(one)
    sort_cards(two)
    sort_cards(three)
    sort_cards(full)
    sort_cards(four)
    sort_cards(five)

    return none + one + two + three + full + four + five


def duplicates_count_plus_joker(counts: list[int], joker_count):
    if counts.count(5) == 5:
        return 5

    if counts.count(4) == 4 and counts.count(1) == 1:
        if joker_count == 1:
            return 5
        return 4

    if counts.count(3) == 3 and counts.count(2) == 2:
        return 6

    if counts.count(3) == 3 and counts.count(1) == 2:
        if joker_count == 2:
            return 5
        if joker_count == 1:
            return 4
        return 3

    if counts.count(2) == 4 and counts.count(1) == 1:
        if joker_count == 1:
            return 6
        return 2

    if counts.count(2) == 2 and counts.count(1) == 3:
        if joker_count == 3:
            return 5
        if joker_count == 2:
            return 4
        if joker_count == 1:
            return 3
        return 1

    if counts.count(1) == 5:
        if joker_count == 5:
            return 5
        if joker_count == 4:
            return 5
        if joker_count == 3:
            return 4
        if joker_count == 2:
            return 3
        if joker_count == 1:
            return 1
        return 0

    return 0


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
    return 1 if char == "J" else text.count(char)


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
