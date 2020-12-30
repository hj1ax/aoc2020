def part1():
    with open("input.txt", "r") as f:
        valid_passwords = 0
        for i in f.read().split("\n"):
            line = i.split(":", 1)
            info = line[0].split(" ")
            min, max = [int(x) for x in info[0].split("-")]
            ch = info[1]
            password = line[1].strip()

            valid_characters = 0

            for ch in password:
                if ch == ch:
                    valid_characters += 1
            
            if valid_characters >= min and valid_characters<= max:
                valid_passwords += 1

        print(valid_passwords)
        
        f.close()

def part2():
    with open("input.txt", "r") as f:
        valid_passwords = 0
        for i in f.read().split("\n"):
            line = i.split(":", 1)
            info = line[0].split(" ")
            indexes = [int(x) for x in info[0].split("-")]
            print(indexes)
            ch = info[1]
            password = line[1].strip()
            valid_characters = 0
            for i in indexes:
                if password[i - 1] == ch:
                    valid_characters += 1
            
            if valid_characters == 1:
                valid_passwords += 1

        print(valid_passwords)
        
        f.close()

part2()