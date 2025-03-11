P=[1,2,3]
for x in P:
    for y in P:
        for z in P:
            if x!=y and y!=z and x!=z:
                print(x,y,z)