def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s):
    return all([
        two_letters(s),
        characters(s),
        Alpha_After_Digits(s),
        Special_Characters(s),
        cant_zero(s),
    ])

def two_letters(s):
    if s[0:1].isalpha():
        return True
    else:
        return False
def characters(s):
    if 2<=len(s)<=6:
        return True
    else:
        return False
def Alpha_After_Digits(s):
    digit_found = False
    for char in s:
        if char.isdigit():
            digit_found = True
        elif digit_found and char.isalpha():
            return False
    return True

def Special_Characters(s):
    for i in s:
        if not(i.isalpha() or i.isdigit()):
            return False
    else:
        return True
def cant_zero(s):
    for t in s:
        if t.isdigit():
            if t == "0":
                return False
            else:
                return True
main()