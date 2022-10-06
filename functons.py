'''def findminmax(a):
    min=a[0]
    max=a[0]
    for i in a:
        if i<min:
            min=i
        if i>max:
            max=i
    print(min,max)
x=[3,4,6,8,2]
findminmax(x)

def evenodd(a):
    if (a%2==0):
        print("even")
    else:
        print("odd")

a=int(input("enter a number to check even odd"))
evenodd (a)
    
def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact=fact*i
    print(fact)
# 7=  7*6*5*4*3*2*1
n=int(input("Enter the number"))
factorial(n)

def findavg(x):
    sum=0
    for i in range(0,len(x)):
        sum=sum+x[i]
    avg=sum/len(x)
    print(avg)
a=[]
x=int(input("Enter the number of elements in the list:"))
for i in range(0,x):
    y=int(input("Enter the number:"))
    a.append(y)
print(a)
findavg(a)
'''

