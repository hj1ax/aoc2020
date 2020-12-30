def get_data(file_path):
    with open(file_path, "r") as f:
        return [tuple(x.split(" ")) for x in f.read().splitlines()]

def execute_instruction(line, instructions_copy, instructions_already_swapped, called_times, acc, already_swapped):
    if called_times[line[0]] != 0:
        return False
    
    if instructions_copy[line[0]]["instruction"] == "nop":
        if already_swapped[0] == False and instructions_already_swapped[line[0]] == False:
            already_swapped[0] = True
            instructions_already_swapped[line[0]] = True
            if int(instructions_copy[line[0]]["value"]) == 0:
                return False
            called_times[line[0]] += 1
            line[0] += int(instructions_copy[line[0]]["value"])
        else:
            called_times[line[0]] += 1
            line[0] += 1
    elif instructions_copy[line[0]]["instruction"] == "jmp":
        if already_swapped[0] == False and instructions_already_swapped[line[0]] == False:
            already_swapped[0] = True
            instructions_already_swapped[line[0]] = True
            called_times[line[0]] += 1
            line[0] += 1
        else:
            called_times[line[0]] += 1
            line[0] += int(instructions_copy[line[0]]["value"])
    elif instructions_copy[line[0]]["instruction"] == "acc":
        acc[0] += int(instructions_copy[line[0]]["value"])
        called_times[line[0]] += 1
        line[0] += 1
    
    return True


def execute(instructions, instructions_already_swapped):
    line = [0]
    instructions_copy = instructions.copy()
    print(instructions_copy)
    acc = [0]
    already_swapped = [False]
    called_times = [0 for i in range(len(instructions))]
    while line[0] < len(instructions.keys()):
        if called_times[line[0]] != 0:
            return execute(instructions, instructions_already_swapped)
        if not execute_instruction(line, instructions_copy, instructions_already_swapped, called_times, acc, already_swapped):
            return execute(instructions, instructions_already_swapped)
    
    return acc[0]


def solution(data):
    instructions = {}
    instructions_already_swapped = []
    for i, v in enumerate(data):
        instructions[i] = {"instruction": v[0], "value": v[1]}
        instructions_already_swapped.append(False)
    
    
    acc = execute(instructions, instructions_already_swapped)
    print(acc)

solution(get_data("test.txt"))