import re


def parse_file(file_path):
    with open(file_path) as f:
        raw_data = f.read()

    data = [x.split() for x in raw_data.split("\n\n")]

    return data


def check_fields(data, required_fields):
    found_keys = {}
    for i in data:
        key, val = i.split(":")
        found_keys[key] = val

    for i in required_fields:
        if i not in found_keys.keys():
            return False
        if check_field(i, found_keys.get(i)) == False:
            return False

    return True


def check_field(key, value):

    if key == "byr":
        return (
            True
            if len(value) == 4 and int(value) >= 1920 and int(value) <= 2002
            else False
        )
    elif key == "iyr":
        return (
            True
            if len(value) == 4 and int(value) >= 2010 and int(value) <= 2020
            else False
        )
    elif key == "eyr":
        return (
            True
            if len(value) == 4 and int(value) >= 2020 and int(value) <= 2030
            else False
        )
    elif key == "hgt":
        return validate_height(value)
    elif key == "hcl":
        return validate_hair_color(value)
    elif key == "ecl":
        return validate_eye_color(value)
    elif key == "pid":
        return True if re.match(r"^[0-9]{9}$", value) != None else False


def validate_height(value):
    mu = value[-2:]

    if mu == "cm":
        return int(value[:-2]) >= 150 and int(value[:-2]) <= 193
    elif mu == "in":
        return int(value[:-2]) >= 59 and int(value[:-2]) <= 76

    return False


def validate_hair_color(color):
    res = re.match(r"^#[a-fA-F-0-9]{6}$", color)

    return res != None


def validate_eye_color(color):
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    return color in eye_colors


def count_valid_passports(data, required_fields):
    valid_passports = 0

    for i in data:
        if check_fields(i, required_fields):
            valid_passports += 1

    return valid_passports


required_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
data = parse_file("input.txt")

res = count_valid_passports(data, required_fields)

print(res)
