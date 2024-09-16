class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class SLL:
    def __init__ (self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head==None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp!=None:
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
        while self.temp.next is  not None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insert_mid(self,data):
        newnode=node(data)
        i=1
        self.temp=self.head
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        print(i)
        newnode.next=self.temp.next
        self.temp.next=newnode

        

obj=SLL()
while 1:
    print("1.Create 2.Display 3.Insert_front 4.Exit 5.Insert_end 6.Insert_mid")
    choice=int(input("Enter a choice : "))
    if choice==1:
        data=int(input("Enter a data : "))
        obj.create(data)
    elif choice==2:
        obj.display()
    elif choice==3:
        data=int(input("Enter a data : "))
        obj.insert_front(data)
    elif choice==4:
        break
    elif choice==5:
        data=int(input("Enter a data :"))
        obj.insert_end(data)
    elif choice==6:
        data=int(input("Enter a data :"))
        pos=int(input("enter position"))
        obj.insert_mid(data)
