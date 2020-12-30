import math

def part1():
    with open("input.txt", "r") as f:
        terrain = f.read().split("\n")

    trees = 0

    x = 0
    for i in range(1, len(terrain)):
        x = (x + 3) % len(terrain[i])

        if terrain[i][x] == "#":
            trees += 1

    print(trees)


def part2():
    with open("input.txt", "r") as f:
        terrain = f.read().split("\n")

    slopes = [
        (1, 1),
        (3, 1),
        (5, 1),
        (7, 1),
        (1, 2)
    ]

    trees = []
    for i in slopes:
        x, trees_count = 0, 0
        
        for j in range(i[1], len(terrain), i[1]):
            x = (x + i[0]) % len(terrain[j])

            if terrain[j][x] == "#":
                trees_count += 1
            
        trees.append(trees_count)

    result = math.prod(trees)
    print(result)

# part1()
part2()