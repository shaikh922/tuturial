'''class employe:
    #initializing/ construct
    def __init__(self):
        print("Employee created :")
    #deleting 
    def __del__(self):
        print ("desctructor called , employee deleted ")
        

obj=employe()
del obj


class employe:
    #initializing/ construct
    def __init__(self):
        print("Employee created :")
    #deleting 
    def __del__(self):
        print ("desctructor called , employee deleted ")

def create_obj():
    print("Marking object")
    obj=employe()
    print("function end")
    return obj
print("calling create_obj")
o1=create_obj()
print("programe")
del o1
'''

#acess specificers
class student:
    def _callme(self):
        print("you got it")

class student2(student):
    def normal(self):
        self._callme()
 
s=student2()
s.normal()



























