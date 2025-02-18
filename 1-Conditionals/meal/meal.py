time=input("meal time?").split(":")
hr,min=int(time[0]),int(time[1])*(1/60)
real=hr+min
if real>=7 and real<=8:
    print("breakfast time!")
elif real>=12 and real<=13:
    print("lunch time!")
elif real>=18 and real<=19:
    print("dinner time!")