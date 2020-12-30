def part1():
    with open("input.txt", "r") as f:
        numbers = [int(x) for x in f.read().split("\n")]

        for i in numbers:
            for j in numbers:
                if i + j == 2020:
                    print(i * j)
                    return

def part2():
    with open("input.txt", "r") as f:
        numbers = [int(x) for x in f.read().split("\n")]

        for i in numbers:
            for j in numbers:
                for k in numbers:
                    if i + j + k == 2020:
                        print(i * j * k)
                        return

# part1()
part2()
