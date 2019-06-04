def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str


s = "PYTHON"
l="python is good"
k=s.replace("PYTHON","PYTN")
m= l.replace(l[0:6],s)
print(m)
print(reverse(m))
print("The original string  is : ")
print(s)
print("The reversed string is : ")
print(reverse(k))
l="python"
k=l[0:3]+l[5:]
print(k)
print(reverse(k))