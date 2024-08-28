a = int(input("Enter the length of 1st side : "))
b = int(input("Enter the length of 2nd side : "))
c  = int(input("Enter the length of 3rd side : "))

sides = sorted([a,b,c])

if(sides[2] ** 2 == sides[0] ** 2 + sides[1] ** 2):
    print("The triangle is a right triangle.")
else:
    print("The triangle is not a right triangle.")