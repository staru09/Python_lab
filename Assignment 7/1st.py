print("Hello World")

x = 5
y = 10.5
name = "Bruhh"

print(x,y,name)

print(type(x),type(y),type(name))

print("Addition:", x+y)
print("Subtraction:", x-y)

user = input("ENter: ")
print(user)

x = int(input("Enter Number:"))
if x>0:
    print("Positive")
elif x<0:
    print("Negative")
else:
    print("Zero")


def greet(name):
    return "hello," + name
print(greet("Aru"))


for i in range(5):
    print("Count:",i)

n = 5
while n>0:
    print(n)
    n-=1

