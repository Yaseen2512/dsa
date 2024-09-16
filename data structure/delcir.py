class node:
    def init(self, data):
        self.data = data
        self.next = None

class CLL:
    def init(self):
        self.head = None
        self.tail = None

    def create(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
            self.tail = newnode
            self.tail.next = self.head
        else:
            self.tail.next = newnode
            self.tail = newnode
            self.tail.next = self.head

    def display(self):
        temp=self.head
        while True:
            print(temp.data, end=' ')
            temp = temp.next
            if temp == self.head:
                break
        print()

    def delete_at_front(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head

    def delete_at_end(self):
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp

    def delete_at_mid(self, pos):
        temp = self.head
        i = 1
        while i < pos - 1:
            temp = temp.next
            if temp.next == self.head:
                print("Position out of bounds")
                return
            i += 1
        temp.next = temp.next.next
        if temp.next == self.head:
            self.tail = temp
obj = CLL()
while True:
    print("1. Create 2. Display 3.Delete at front 4. Delete at end 5. Delete at mid 6.Exit")
    choice = int(input("Enter the choice: "))
    if choice == 1:
        data = int(input("Enter the data: "))
        obj.create(data)
    elif choice == 2:
        obj.display()
       elif choice == 3:
        obj.delete_at_front()
    elif choice == 4:
        obj.delete_at_end()
    elif choice == 5:
        pos = int(input("Enter the position: "))
        obj.delete_at_mid(pos)
    else:
        print("Invalid choice")
