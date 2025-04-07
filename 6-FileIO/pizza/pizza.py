import sys
import tabulate
import csv
_,extension=sys.argv[1].split(".")
if len(sys.argv)<2 :
    print("Too few command-line arguments")
elif len(sys.argv)>2:
    print("Too many command-line arguments")
elif extension != "csv":
    print("Not a csv file")
else:
    try:
        with open(sys.argv[1]) as file:
            pizza=csv.reader(file)
            List=[]
            for row in pizza:
                List.append(row)
            print(tabulate.tabulate(List,tablefmt="grid"))
    except FileNotFoundError:
        print("File does not exist")