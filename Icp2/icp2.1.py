def main():
    s=input("enter a string")
    k=string_alternative(s)
    return k


def string_alternative(s):
    var=s[::2]
    print(s)
    b=""
    for i in range(len(s)):
        if (i % 2) == 0:
          b+= s[i]
    return var

print(main())
