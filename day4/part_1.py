import re

def parse_file(file_path):
    with open(file_path) as f:
        raw_data = f.read()
    
    data = [x.split() for x in raw_data.split("\n\n")]

    return data

def check_fields(data, required_fields):
    found_keys = []
    for i in data:
        key, _ = i.split(":")
        found_keys.append(key)
    
    for i in required_fields:
        if i not in found_keys:
            return False

    return True

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
