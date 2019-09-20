fullname= input("Name:")
name=list(fullname.split())


# def two_name():
#     a=name.pop(0)
#     b=name.pop()
#     return a,b

print(name)
print(len(name))
first=name.pop(0)
last=name.pop(-1)
print(first)
print(last)

