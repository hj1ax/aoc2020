def get_data(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().splitlines()]


def resolve(data, index=0):
    numbers = data[index : index + 5]
    for i, m in enumerate(numbers):
        for n in numbers[i:]:
            if m + n == data[5 + index]:
                return resolve(data, index + 1)

    print(data[5 + index])


resolve(get_data("test.txt"))