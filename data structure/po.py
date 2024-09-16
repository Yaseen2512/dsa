class node:
    def __init__(self,ex,co):
        self.ex=ex
        self.co=co
        self.next=None

class poly:
    def __init__(self):
        self.head=None
        self.temp=None

    def create(self,co,ex):
        newnode=node(co,ex)
        if self.head is None :
            self.head=newnode
            self.temp-newnode
        else :
            self.temp.next=newnode
            self.temp=newnode

    def display(self):
        self.temp=self.head
        while self.temp !=None:
            print(f"{self.temp.co}^{self.temp.ex}",end = " ")
            self.temp=self.temp.next
        print()

def add(poly1,poly2):
    p1=poly1.head
    p2=poly2.head
    obj=poly()
    while p1 is not None and p2 is not None:
        if p1.ex>p2.ex:
            obj.create(p1.co,p1.ex)
            p1=p1.next
        elif p1.ex<p2.ex:
            obj.create(p2.co,p2.ex)
            p2=p2.next
        else:
            obj.create(p1.co+p2.co,p1.ex)
            p1=p1.next
            p2=p2.next
    
            
            
