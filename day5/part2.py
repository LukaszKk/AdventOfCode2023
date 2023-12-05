import os

input_file = "input.txt"

# Res: 52210644


def calculate(lines: list[str]) -> int:
    seeds = [int(el) for el in lines[0].split(":")[1].split()]
    print(seeds)
    global_min_location = 10 ** 20

    alls = []

    for j in range(0, len(seeds), 2):
        seed_map = [[seeds[j], seeds[j] + seeds[j + 1] - 1]]

        data_map = map_reader(lines, "seed-to-soil map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "soil-to-fertilizer map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "fertilizer-to-water map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "water-to-light map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "light-to-temperature map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "temperature-to-humidity map:")
        seed_map = map_process(seed_map, data_map)

        data_map = map_reader(lines, "humidity-to-location map:")
        seed_map = map_process(seed_map, data_map)

        # print(seed_map)

        alls.extend([x[0] for x in seed_map])

        min_location = min([x[0] for x in seed_map])
        global_min_location = min_location if min_location < global_min_location else global_min_location

    print()
    print(alls)
    print([el for el in alls if el < 52210644])

    return global_min_location


def map_process(seed_map: list[list], data_map: list[str]) -> list[list]:
    copy_map = seed_map.copy()
    new_maps = []
    for data in data_map:
        data_details = data.split(" ")
        length = int(data_details[2])
        destination_start = int(data_details[0])
        source_start = int(data_details[1])
        source_end = source_start + length - 1

        # print(f"map: {copy_map} source: {source_start} - {source_end} dest: {destination_start}")

        for i in range(len(seed_map)):
            seed_start = seed_map[i][0]
            seed_end = seed_map[i][1]

            if seed_start < source_start:
                if seed_end < source_start:
                    pass
                elif seed_end <= source_end:
                    copy_map[i][1] = source_start - 1
                    new_maps.append([destination_start, destination_start + (seed_end - source_start)])
                elif seed_end > source_end:
                    copy_map[i][1] = source_start - 1
                    new_maps.append([destination_start, destination_start + (source_end - source_start)])
                    new_maps.append([source_end + 1, seed_end])

            elif seed_start >= source_start:
                if seed_start <= source_end:
                    copy_map[i][0] = destination_start + (seed_start - source_start)

                    if seed_end <= source_end:
                        copy_map[i][1] = destination_start + (seed_end - source_start)
                    elif seed_end > source_end:
                        copy_map[i][1] = destination_start + (source_end - source_start)
                        new_maps.append([source_end + 1, seed_end])

                elif seed_start > source_end:
                    pass

    return copy_map + new_maps


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
