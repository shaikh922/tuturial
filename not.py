'''x=int(input("enter age"))
if not(x>=18):
    print("Not eligible")
else:
    print("eligible")

Garage=("name","car","model",2017,"style","vintage","price",600000)'''
def findsum(a1,a2):
    sum=a1+a2
    return sum
a=int(input("enter marks1:"))
c=int(input("enter marks2:"))
sum=findsum(a,c)
print(sum)

def findaverage(a3,a4):
    ans=findsum(a,c)
    return ans/2
avg=findaverage(a,c)
print(avg)

def findpercentage(a5,a6):
    ans=findsum(a,c)
    return(ans/200)*100
per=findpercentage(a,c)
print(per,"%")

def findgrade(a7,a8):
    ans=findsum(a,c)
    if ans>=150:
        return("A")
    elif ans>=100 and ans<150:
        return("B")
    else:
        return("C")
grade=findgrade(a,c)
print(grade)


