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


def get_highest_id(data):
    highest_id = get_row(data[0][:-3]) * 8 + get_column(data[0][-3:])
    for i in data[1:]:
        row, col = get_row(i[:-3]), get_column(i[-3:])
        id = row * 8 + col
        if id > highest_id:
            highest_id = id

    return highest_id


print(get_highest_id(get_data("input.txt")))