import sys
_,extension=sys.argv[1].split(".")
if len(sys.argv)<2 :
    print("Too few command-line arguments")
elif len(sys.argv)>2:
    print("Too many command-line arguments")
elif extension != "py":
    print("Not a Python file")
else:
    try:
        with open (sys.argv[1]) as file:
            lines=file.readlines()
            c=0
            for line in lines:
                if line.startswith("#")or line.strip()=="":
                    continue
                else:
                    c+=1
            print(c)
    except FileNotFoundError:
        print("File does not exist")