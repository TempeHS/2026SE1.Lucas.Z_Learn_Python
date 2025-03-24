dic = {}
while True:
    try:
        item = input()
        if item in dic:
            dic[item] += 1
        else:
            dic[item] = 1
    except EOFError:
        for item in sorted(dic):
            print(f"{dic[item]} {item.upper()}")
        break