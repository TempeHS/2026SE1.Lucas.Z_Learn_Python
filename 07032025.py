num1=int(input("what is number 1? "))
num2=int(input("what is number 2? "))
operator=input("what is the operator? ")
if operator == '+':
    print(num1 + num2)
elif operator == '-':
    print(num1 - num2)
elif operator == '*':
    print(num1 * num2)
elif operator == '/':
    print(num1 / num2)
else :
    print("Not a known operator")