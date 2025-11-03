area=lambda a:a*a
side=int(input("Enter the side of square:"))
print("area of square is:",area(side))
recarea=lambda l,b:l*b
l=int(input("Enter the length of rectangle:"))
b=int(input("Enter the breadth of rectangle:"))
print("area of rectangle is:",recarea(l,b))
triarea=lambda a,c:0.5*a*c
a=int(input("Enter the length of triangle:"))
c=int(input("Enter the breadth of triangle:"))
print("area of triangle is:",triarea(a,c))
