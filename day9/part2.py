from part1 import resolve as p1

part1_solution = p1()


def get_data(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().splitlines()]


def resolve(index=0):
    data = get_data("input.txt")
    numbers = data[index : index + 25]
    for i, m in enumerate(numbers):
        for j, n in enumerate(numbers[i:]):
            if sum(numbers[i:j]) == part1_solution:
                return min(numbers[i:j]) + max(numbers[i:j])

    return resolve(index + 1)


if __name__ == "__main__":
    print(resolve())