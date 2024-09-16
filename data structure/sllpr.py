class node:
    def __init__(self, data):
        self.data=data
        self.next=None

class SLL:
    def __init__ (self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head is None :
            self.head=newnode
            self.temp=newnode
        else :
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp != None :
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
        while self.temp.next!=None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insert_mid(self,data):
        newnode=node(data)
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        newnode.next=self.temp.next
        self.temp.next=newnode
    def del_front(self):
        self.temp=self.head
        self.head=self.head.next
        self.temp=None
    def del_end(self):
        self.temp=self.head
        while selt.temp.next.next is not None:
            self.temp=self.temp.next
        self.temp.next=None
    def del_mid(self):
        self.temp=self.head
        i=1
        while i<pos-1:
            self.temp=self.temp.next
            i=i+1
        self.temp.next=self.temp.next.next
        self.temp.next.next=None


obj=SLL()
while 1:
    print("1.create ,2.display ,3.insert_front ,4.insert_end ,5.insert_mid ,6.del_front ,7.del_end ,8.del_mid ,9.exit")
    n=int(input("enter your choice : "))
    if n==1:
        data=int(input("enter the data : "))
        obj.create(data)
    elif n==2:
        obj.display()
    elif n==3:
        data=int(input("enter the data : "))
        obj.insert_front(data)
    elif n==4:
        data=int(input("enter the data : "))
        obj.insert_end(data)
    elif n==5:
        pos=int(input("enter the position: "))
        data=int(input("enter the data : "))
        obj.insert_mid(data)
    elif n==6:
        obj.del_front()
    elif n==7:
        obj.del_end()
    elif n==8:
        pos=int(input("enter the position :"))
        obj.del_mid()
    elif n==9:
        break
    else:
        print("you enter the invalid number ")



        
        
        
        
