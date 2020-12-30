def get_row(input):
    low, high = 0, 127

    for i in input:
        if i.lower() == "f":
            high -= (high - low + 1) / 2
        else:
            low += (high - low + 1) / 2

    if input[-1:].lower() == "f":
        return int(low)

    return int(high)


def get_column(input):
    low, high = 0, 7

    for i in input:
        if i.lower() == "l":
            high -= (high - low + 1) / 2
        else:
            low += (high - low + 1) / 2

    if input[-1:].lower() == "l":
        return int(low)

    return int(high)


def get_id(row, column):
    return row * column


def get_data(file_path):
    with open(file_path, "r") as f:
        return f.read().split("\n")


def find_seat_id(data):
    ids = [get_row(x[:-3]) * 8 + get_column(x[-3:]) for x in data]
    ids.sort()
    for i in range(0, len(ids)):
        if ids[i] + 1 != ids[i + 1]:
            return ids[i] + 1


print(find_seat_id(get_data("input.txt")))