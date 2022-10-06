age=[45,21,17,38,13,25,18]
el=list(filter(lambda x:x>=18,age))
print(el)

l1=[10,11,20,31,40,51,60,71]
l2=list(filter(lambda x:x%2==0,l1))
print(l2)

l3=list(filter(lambda x:x%2!=0,l1))
print(l3)

l4=list(map(lambda x:x*2,age))
print(l4)

l5=list(map(lambda x:x**2,age))
print(l5)

import functools
c3=(functools.reduce(lambda x,y:x if x>y else y,age))
print(c3)




