import os

input_file = "test_input.txt"


def calculate(lines: list[str]) -> int:
    seeds = [int(el) for el in lines[0].split(":")[1].split()]
    seed_map = [seeds[i] for i in range(len(seeds))]

    data_map = map_reader(lines, "seed-to-soil map:")
    seed_map = map_process(seed_map, data_map)

    data_map = map_reader(lines, "soil-to-fertilizer map:")
    seed_map = map_process(seed_map, data_map)

    data_map = map_reader(lines, "fertilizer-to-water map:")
    seed_map = map_process(seed_map, data_map)

    seed_to_soil = map_reader(lines, "water-to-light map:")
    seed_map = map_process(seed_map, seed_to_soil)

    seed_to_soil = map_reader(lines, "light-to-temperature map:")
    seed_map = map_process(seed_map, seed_to_soil)

    seed_to_soil = map_reader(lines, "temperature-to-humidity map:")
    seed_map = map_process(seed_map, seed_to_soil)

    seed_to_soil = map_reader(lines, "humidity-to-location map:")
    seed_map = map_process(seed_map, seed_to_soil)

    print(seed_map)

    return min(seed_map)


def map_process(seed_map: list[int], data_map: list[str]) -> list[int]:
    copy_map = seed_map.copy()
    for i in range(len(seed_map)):
        for data in data_map:
            data_details = data.split(" ")
            length = int(data_details[2])
            destination_start = int(data_details[0])
            source_start = int(data_details[1])
            source_end = source_start + length

            if source_start <= seed_map[i] < source_end:
                copy_map[i] = destination_start + (seed_map[i] - source_start)

    return copy_map


def map_reader(lines: list[str], line_to_search: str) -> list[str]:
    should_read = False
    data_map = []
    for line in lines:
        line = line.strip()
        if not line and should_read:
            break
        if line == line_to_search:
            should_read = True
            continue
        if should_read:
            data_map.append(line)
    return data_map


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
