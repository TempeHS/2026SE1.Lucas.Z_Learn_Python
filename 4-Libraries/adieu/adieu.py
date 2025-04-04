import inflect
p = inflect.engine()
names=[]
while True:
    try:
        s=input("")
        names.append(s)
    except EOFError:
        print("Adieu, adieu, to ", p.join(names))
        break