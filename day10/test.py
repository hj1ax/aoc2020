def resolve():
    with open("test.txt") as f:
        data = list(map(lambda x: int(x), f.read().splitlines()))
    
    jolt1, jolt3 = 0, 0

    for i, m in enumerate(data):
        for n in data[i + 1:]:
            print(f"{m}-{n}")
            if abs(m - n) == 3:
                jolt3 += 1
            
            if abs(m - n) == 1:
                jolt1 += 1
    
    print(jolt1, jolt3)

resolve()