'''
def sum(n):
    if n>=1:
        sum(n-1)
        print(n)
sum(10)


def tum(n):
    if n<=10:
        tum(n+1)
        print(n)
tum(1)


def find(n):
    if n==1:
        return n
    else:
        return n*find(n-1)
num=find(4)
print(num)


str ='mumbai'
for i in str:
    if i=='b':
        continue
    else:
        print(i)
        '''
       

a =[1,2,3,4,5,6,7,8,9,10]
for i in a:
    if i==6:
        continue
    else:
        print(i)



a =['java','css','react','python','html',]
for i in a:
    if i=='python':
      pass
    else:
        print(i)

























































        
