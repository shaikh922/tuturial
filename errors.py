'''
try:
    x=int(input("Enter the first number :"))
    y=int(input("Enter the second number :"))
    print(x/y)
except ZeroDivisionError:
    print("this is a division by 0 error.please enter a number without 0 for better answer")
except ValueError:
    print("please enter only numbers")

def fun(a):
    if a<4:
        b=a/(a-3)
        print(b)
    

fun(2)
try:
    fun(5)
except ZeroDivisionError:
    print("hello")
finally:
    print("done")
    
def Abyb(a,b):
    try:
        c=((a+b)/(a-b))
    except ZeroDivisionError:
        print("a/b result in 0")
    else:
        print(c)
    finally:
        print("done")

Abyb(10,10)

'''

x=int(input("Enter the first number :"))
y=int(input("Enter the second number :"))
if x==0 and y==0:
    raise ValueError

else:
    print(x/y)











































































