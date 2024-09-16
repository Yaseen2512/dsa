class node:
    def __init__ (self,co,ex):
        self.co=co
        self.ex=ex
        self.next=None

class POLY:
    def __init__(self):
        self.head=None
        self.temp=None

    def create(self,ex,co):
        newnode=node(co,ex)
        if self.head is None:
            self.head=newnode
            self.temp=newnode
        else:
            self.temp.next=newnode
            self.temp=newnode

    def display(self):
        self.temp=self.head
        while self.temp!=None:
            
            
