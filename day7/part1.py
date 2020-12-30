import re

def parse_data(file_path):
    with open(file_path, "r") as f:
        raw_data = f.read()

    data = raw_data.splitlines()

    return data


def count_bags(bags, key):
    total_bags = 1
    for bag, value in bags[key].items():
        total_bags += int(value) * count_bags(bags, bag)
    
    return total_bags


def contains_bag(bags, key, valid_bags=set()):
    for k, v in bags.items():
        if key in v and k not in valid_bags:
            valid_bags.add(k)
            contains_bag(bags, k, valid_bags=valid_bags)
    
    return len(valid_bags)



def solution(data):
    bags = {}

    for i in data:
        key, values = re.match(r'(.+?)s? contain (.+)', i).groups()
        values = re.findall(r'(\d) ([ a-z]+bag)?', values)

        if key not in bags:
            bags[key] = {}
        
        for size, value in values:
            bags[key][value] = size

    print(bags)
    print(contains_bag(bags, "shiny gold bag"))
    print(count_bags(bags, "shiny gold bag") - 1)

solution(parse_data("input.txt"))