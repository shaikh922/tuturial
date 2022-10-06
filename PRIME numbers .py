#x=int(input("Enter a numbe"))
#for i in range (2,x):
 #   if (x%i==0):
  #      print ("Not Prime")
   # else:
    #    print ("prime")


#x=int(input("Enter a numbe"))
#flag=0
#for i in range (2,x):
  #  if (x%i==0):
   #     flag=1
    #    break
#if flag==1:
   # print ("Not Prime")
#else:
       # print ("prime")

x=int(input("Enter a numbe"))
count=0
print("2")
for i in range (3,1000):
    if count<=x-2:
        for j in range(2,i):
            if (i%j)==0:
                break
        else:
            print(i)
            count=count+1
        
        
