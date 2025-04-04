#1
name=["darius","veigo","kassadin","ziggs","thresh"]
lane=["top","jungle","mid","bot","support"]
#2
print("| Col1 | Col2 |")
print("|----- |------|")
for i in range(len(name)):
    print(f"|{name[i]} | {lane[i]}|")
    print("|----- |------|")
#3
c=input("name? ")
if c in name:
    num=name.index(c)
    print(f"{name[num]}, {lane [num]}")
#4
newitem=input("item ").split(" ")
name.append(newitem[0])
lane.append(newitem[1])
name.sort()
lane.sort()
print("| Col1 | Col2 |")
print("|----- |------|")
for i in range(len(name)):
    print(f"|{name[i]} | {lane[i]}|")
    print("|----- |------|")
#5
with open("text1.txt") as file