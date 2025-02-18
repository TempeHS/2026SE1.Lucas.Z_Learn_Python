question=(input("what is the question ").split(" "))
x,y,z= int(question[0]), question[1], int(question[2])
if y == '+':
    print(x + z)
elif y == '-':
    print(x - z)
elif y == '*':
    print(x * z)
else :
    print(x / z)
