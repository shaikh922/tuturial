class Food:
    food={'F_id':[],'F_name':[],'F_type':[],'price':[]}
    def __init__(self,foodId,foodName,foodType,foodPrice):
        self.id=foodId
        self.name=foodName
        self.type=foodType
        self.price=foodPrice
        self.fooddict()
        
    def fooddict(self):
        self.food["F_id"].append(self.id)
        self.food["F_name"].append(self.name)
        self.food["F_type"].append(self.type)
        self.food["price"].append(self.price)
    # Food List  
    def display(self):
        print("The Food menu is:=")
        for i,j,k,l in zip (self.food["F_id"],self.food["F_name"],self.food["F_type"],self.food["price"]):
            print(i,"\t",j,"\t",k,"\t",l)
    # Food By Id
    def Find_byid(self):
        ok=int(input("\nplease enter the id:"))
        print("\nThe Enter id Food details are following:")
        for i in self.food.values():
            print("\t","\t","\t","\t","\t",i[ok])
    #Food by names
    def Find_byname(self):
        x=self.food["F_id"]
        y=self.food["F_name"]
        print("\nThe Food names are following:")
        for i,j in zip(x,y):
            print("\t","\t","\t","  ",i,"  ",j)
    # Food by Types
    def Find_bytype(self):
        a=self.food["F_type"]
        b=self.food["F_name"]
        l=[]
        m=[]
        for i,j in zip (a,b):
            if i=="non-veg":
                l.append(j)               
            else:
                m.append(j)
        print("\nThe Non-Vageterian food are:=")
        print("                              ",l)
        print("\nThe vageterian food are:=")
        print("                              ",m)
#Delete all Food Details
    def delete_food(self):
        print("\nEnter the delete food detail:")
        id1=int(input("Enter the id:"))
        name=input("Enter the name:")
        type1=input("Enter the Food Type:")
        price=int(input("Enter the price"))
        
        x=self.food["F_id"]
        y=self.food["F_name"]
        z=self.food["F_type"]
        a=self.food["price"]
        x.remove(id1)
        y.remove(name)
        z.remove(type1)
        a.remove(price)
        print(self.food)

    #Food sort by names
    def Sort_byname(self):
        print("\n The food list by sorting names=")
        self.food["F_name"].sort()
        print("\t","\t","\t       ",self.food["F_name"])

    #Food sort by price
    def Sort_byprice(self):
        self.food["price"].sort()
        y=self.food["F_name"]
        for i,j in zip(self.food["price"],y):
            print("\n",i,j)

    #Add new Food items
    def add_food(self):
        print("\nEnter the Food Details which you want to add:")
        id1=int(input("Enter the id:"))
        name=input("Enter the name:")
        type1=input("Enter the Food Type:")
        price=int(input("Enter the price"))
        self.food["F_id"].append(id1)
        self.food["F_name"].append(name)
        self.food["F_type"].append(type1)
        self.food["price"].append(price)
        print(self.food)
    #def update_food(self):
        

        
#Add the Food values
f1=Food(1,"vadapav","veg",500)
f2=Food(2,"misal ","veg",10)
f3=Food(3,"tanduri","non-veg",1000)
f4=Food(4,"chiken","non-veg",200)
#display list
f4.display()
#display list by id
f4.Find_byid()
#display list  by name
f4.Find_byname()
#display list by type
f4.Find_bytype()
#Delete Food items 
f4.delete_food()
#display list by sorting names 
f4.Sort_byname()
#display list by sorting price
f4.Sort_byprice()
#Add Food items
f4.add_food()



