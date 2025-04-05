def main():
    z=input("what")
    print(shorten(z))
def shorten(s):
    i ="aeiouAEIOU"
    for _ in i:
        s=s.replace(_,"")
    return s

if __name__ == "__main__":
    main()