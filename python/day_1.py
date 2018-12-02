input_path = '../input/day_1.txt'

def run():
    part_1()
    part_2()

def part_1():
    with open(input_path, 'r') as input_file:
        frequency = 0
        for line in input_file:
            frequency += int(line)
        print(f"Result frequency: {frequency}")

def part_2():
    frequencies = set()
    frequency = 0
    frequencies.add(frequency)
    while True:
        with open(input_path, 'r') as input_file:
            for line in input_file:
                frequency += int(line)
                if frequency in frequencies:
                    print(f"Duplicate frequency: {frequency}")
                    return
                else:
                    frequencies.add(frequency)

if __name__ == "__main__":
    run()