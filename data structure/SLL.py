class node:
    def __init__(self,data):
        self.data=data
        self.next=None

class SLL:
    def __init__ (self):
        self.head=None
        self.temp=None
    def create (self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp !=None:
            print(self.temp.data,end=' ')
            self.temp=self.temp.next
        print()
    def insert_front(self,data):
        newnode=node(data)
        newnode.next=self.head
        self.head=newnode
    def insert_end(self,data):
        newnode=node(data)
        self.temp=self.head
        while self.temp.next !=None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insert_mid (self,data,pos):
        newnode=node(data)
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
        

obj=SLL()
while 1:
    print("1.Create , 2.Display , 3.Exit , 4.Insert_front , 5.Insert_end , 6.Insert_mid")
    choice=int(input("Enter your choice : "))
    if choice==1:
        data=int(input("Enter your data : "))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        break
    elif choice==4:
        data=int(input("Enter your data : "))
        obj.insert_front(data)
    elif choice==5:
        data=int(input("Enter yout data : "))
        obj.insert_end(data)
    elif choice==6:
        pos=int(input("Enter the position : "))
        data=int(input("Enter your data : "))
        obj.insert_mid(data,pos)
