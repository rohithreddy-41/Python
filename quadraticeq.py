import cmath
a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
z=(b*b)-(4*a*c)
root1= (-b+cmath.sqrt(z))/(2*a)
root2= (-b-cmath.sqrt(z))/(2*a)
print("root1: {0}, root2: {1}".format(root1,root2))
