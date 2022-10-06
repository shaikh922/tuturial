
print ("1 area of a circle")
print ("2 area of a rectangle")
print ("3 area of a cube")
choice=int(input("enter the choice "))
if (choice==1):
    r=int(input("enter radious "))
    print(3.14*r*r)
elif (choice==2):
    a=float(input("enter length "))
    b=float(input("enter breath "))
    print(a*b)
elif (choice==3):
    a=float(input("enter length "))
    b=float(input("enter breath "))
    c=float(input("enter heigth "))
    print(a*b*c)

else:
    print("select a valid number")
