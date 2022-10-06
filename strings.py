#a="alibag"
#b="bombay"
#a+b
#a+" "+b
#len(a)
#len(b)
#x=a+b
#x="Hello world"
#x.ljust(50)
#x.rjust(50)
#x.center(50)
#x.split("l")
#x.replace("l","$")
#x.strip

x=input("Enter string:")
for i in range (0,len(x)):
    print(x[i])


    

x=input("Enter string:")
for i in range (len(x)-1,-1,-1):
    print(x[i])#PRINT BACKWARDS 

x=input("Enter string:")
for i in range (1,len(x)+1):
    print(x[-i])#REVERSE
