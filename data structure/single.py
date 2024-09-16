class node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class linked_list:
    def __init__(self):
        self.head=None
        self.temp=None
    def create(self,data):
        newnode=node(data)
        if self.head is None:
            self.head=newnode
            self.temp=self.head
        else:
            self.temp.next=newnode
            self.temp=newnode
    def display(self):
        self.temp=self.head
        while self.temp is not None:
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
        while self.temp.next is not None:
            self.temp=self.temp.next
        self.temp.next=newnode
    def insert_mid(self,data):
        newnode=node(data)
        i=1
        self.temp=self.head
        while i
