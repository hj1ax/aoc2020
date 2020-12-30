def get_data(file_path):
    with open(file_path, "r") as f:
        return [tuple(x.split(" ")) for x in f.read().splitlines()]


def execute_instruction(line, instructions, acc):
    if instructions[line[0]]["called_times"] != 0:
        return False

    if instructions[line[0]]["instruction"] == "nop":
        instructions[line[0]]["called_times"] += 1
        line[0] += 1
    elif instructions[line[0]]["instruction"] == "jmp":
        instructions[line[0]]["called_times"] += 1
        line[0] += int(instructions[line[0]]["value"])
    elif instructions[line[0]]["instruction"] == "acc":
        acc[0] += int(instructions[line[0]]["value"])
        instructions[line[0]]["called_times"] += 1
        line[0] += 1

    return True


def execute(instructions, acc):
    line = [0]

    while True:
        if line[0] >= len(instructions.keys()):
            break
        if instructions[line[0]]["called_times"] != 0:
            break
        if not execute_instruction(line, instructions, acc):
            break


def solution(data):
    instructions = {}

    for i, v in enumerate(data):
        instructions[i] = {"instruction": v[0], "value": v[1], "called_times": 0}

    acc = [0]
    execute(instructions, acc)
    print(acc[0])


solution(get_data("input.txt"))