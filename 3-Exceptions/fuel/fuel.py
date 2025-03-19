while True:
    try:
        fuel=input('fuel left?').split("/")
        x=int(fuel[0])
        y=int(fuel[1])
        z=int(x/y)
        if z <= 0.01 :
            print("E")
            break
        elif z>=0.99:
            print("f")
            break
        elif 0.01<z<0.99:
            print(z*100,"%")
            break
    except (ZeroDivisionError, ValueError):
        pass