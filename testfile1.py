
file=open("testflie.txt","r")
print(file.read())
file.close()

file=open("testflie.txt","r")
print(len(file.read()))
file.close()

file=open("testflie.txt","r")
print(len(file.readlines()))
file.close()

file=open("testflie.txt","r")
re=file.read()
ad=re.split()
print(ad)

file=open("testflie.txt","r")
re=file.read()
ad=re.split()
count=0
for i in ad:
    if i=="is":
        count=count+1
print(count)

#for printing the line starting with t
file=open("testflie.txt","r")
re=file.readlines()
count=0
for i in re:
    if i[0]=="t":
        count=count+1
print(count)
#for printing the line ending with y
file=open("testflie.txt","r")
re=file.readlines()
count=0
for i in re:
    if i[-2]=="y":
        count=count+1
        print(i)
