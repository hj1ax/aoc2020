def get_data(file_path):
    with open(file_path, "r") as f:
        return [int(x) for x in f.read().splitlines()]


def resolve(index=0):
    data = get_data("input.txt")
    numbers = data[index : index + 25]
    for i, m in enumerate(numbers):
        for n in numbers[i:]:
            if m + n == data[25 + index]:
                return resolve(index + 1)

    return data[25 + index]


if __name__ == "__main__":
    print(resolve())