def get_data(file_path):
    with open(file_path) as f:
        return [x.split("\n") for x in f.read().strip().split("\n\n")]

def count_answers(data):
    answers = set()
    for i in data:
        for j in i:
            answers.add(j)
    
    return len(answers)

def sum_counts(data):
    sum = 0
    
    for i in data:
        sum += count_answers(i)
    
    return sum

print(sum_counts(get_data("input.txt")))