N=50
IA=int(input("insert amount: "))
if IA ==25 or IA==5 or IA == 10:
    D=N-IA
else:
    D=N
print("remaining amount: ",D)
while D>=0:
    IA=int(input("insert amount: "))
    D=D-IA
    if D>=0:
        print("remaining amount: ",D)
if D<0:
    print("change owed: ",D*-1)
