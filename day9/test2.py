def get_data(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().splitlines()]


def resolve(data, index=0):
    numbers = data[index : index + 25]
    for i, m in enumerate(numbers):
        for j, n in enumerate(numbers[i:]):
            if sum(numbers[i:j]) == 127:
                return print(min(numbers[i:j]) + max(numbers[i:j]))

    return resolve(data, index + 1)


resolve(get_data("test.txt"))