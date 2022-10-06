# wrie a rectangle class in pyhton language allowing you to build a rectangle
# with lenght and width attributes.
'''
class rectangle:
    length=None
    width=None

    def __init__(self,l,w):
        self.length=l
        self.width=w

    def premeter(self):
        return 2*(self.length+self.width)
    def area(self):
        return (self.length*self.width)
    def display(self):
        print("The length of rectangle is",self.length)
        print("The width of rectangle is",self.width)
        print("The premeter is",self.premeter())
        print("The area  is",self.area())

class parallelepipede(rectangle):
    def __init__(self,length,width,height):
        rectangle.__init__(self,length,width)
        self.height=height

    def volume(self):
        return (self.length*self.width*self.height)
    

x=int(input("Enter the length :"))
y=int(input("Enter the width :"))
z=int(input("Enter the height :"))

s2=parallelepipede(x,y,z)
s2.display()
print("The volume of parallelepipede is :",s2.volume())

class Bankaccount:
   
    def __init__(self,ac,name,balance):
        self.accountnumber=ac
        self.name=name
        self.balance=balance

    def deposit(self,amt):
        self.balance=self.balance+amt
    def withdrawal(self,wi):
        if(self.balance<wi):
            print("OOPS Sorry ,Amount can't be withdrawal due to insufficient balance !")
        else:
            self.balance=self.balance-wi
    def bankfess(self):
        self.balance=self.balance-(5/100)*self.balance
    def display(self):
        print("Account Number :",self.accountnumber)
        print("Account Name :",self.name)
        print("Account Balance :",self.balance)

x=int(input("Enter Account Number :"))
y=input("Enter your name :")
z=int(input("Enter your current balance :"))
print("1.deposit")
print("2.withdrawal")
if choice==1:
    
x1=Bankaccount(x,y,z)
x1.display()
'''

class person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def display(self):
        print("Your name is :",self.name)
        print("Your age is :",self.age)

class childclass(person):
    def __init__(self,name,age,section):
        person.__init__(self,name,age)
        self.section=section

    def displaystudent(self):
        person.display(self)
        print("Your section is ",self.section)

x=input("Enter your name :")
y=int(input("Enter your age :"))
z=input("Enter your section :")
a1=childclass(x,y,z)
a1.displaystudent()

































        
        
































