#lambda with add
ans1=lambda a,b:a+b
x=int(input("Enter frist value:"))
y=int(input("enter second value:"))
print(ans1(x,y))

#lambda with sub
ans2=lambda a,b:a-b
print(ans2(x,y))
#lambda with condition
ans3=lambda a,b:print("yes") if a+b>100 else print("no")
print(ans3(x,y))
