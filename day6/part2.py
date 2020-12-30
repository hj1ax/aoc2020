def get_data(file_path):
    with open(file_path) as f:
        return [x.split("\n") for x in f.read().strip().split("\n\n")]

def count_answers(data):
    count = set()
    answers_count = {}

    for i in data:
        people_count = len(data)

        for j in i:
            try:
                answers_count[j] += 1
            except KeyError:
                answers_count[j] = 1
        
        for j in answers_count.keys():
            if answers_count[j] == people_count:
                count.add(j)
    
    return len(count)

def sum_counts(data):
    sum = 0
    
    for i in data:
        sum += count_answers(i)
    
    return sum

print(sum_counts(get_data("input.txt")))