x=int(input("Enter the number"))
ans1=lambda x:x+5
print(ans1(x))

ans2=lambda x:x+x
print(ans2(x))

ans3=lambda x:x**2
print(ans3(x))

ans4=lambda x:x**3
print(ans4(x))

ans5=lambda x:print("number is greater")if x>100 else print("false")
print(ans5(x))
