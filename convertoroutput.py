'''
import convertor
x=float(input("Enter doller :"))
y=float(input("Enter pound :"))
z=float(input("Enter euro :"))
convertor.doller(x)
convertor.pound(y)
convertor.euro(z)
'''

class  datatypes:
    def __init__(self,a1,a2,a3,a4):
        self.a1=a1
        self.a2=a2
        self.a3=a3
        self.a4=a4
    def convertortolist(self):
        l=[self.a1,self.a2,self.a3,self.a4]
        print(l)
    def convertortoset(self):
        s={self.a1,self.a2,self.a3,self.a4}
        print(s)
    def convertortotup(self):
        t=(self.a1,self.a2,self.a3,self.a4)
        print(t)

x=int(input("Enter first nuymber :"))
x1=int(input("Enter second nuymber :"))
x2=int(input("Enter third nuymber :"))
x3=int(input("Enter four nuymber :"))
d=datatypes(x,x1,x2,x3)
d.convertortolist()
d.convertortoset()
d.convertortotup()
