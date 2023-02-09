class node:
    def __init__(self,data):
        self.data = data
        self.next = None

class circularLL:
    def __init__(self):
        self.head = None
    
    def insertStart(self,data):
        new_node = node(data)

        if self.head == None:   #if there are no nodes present and its the first node.
            self.head = new_node
            new_node.next = self.head
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head
        self.head = new_node 
    
    def OinsertStart(self,data):
        new_node = node(data)

        if self.head == None:   #if there are no nodes present and its the first node.
            self.head = new_node
            new_node.next = self.head
            return
        
        new_node.next = self.head.next # inserting the new node just after head.
        self.head.next = new_node

        new_node.data, self.head.data = self.head.data, new_node.data #exchanging the values of new node and head.

    def Oinsertend(self,data):
        new_node = node(data)

        if self.head == None:   #if there are no nodes present and its the first node.
            self.head = new_node
            new_node.next = self.head
            return

        new_node.next = self.head.next #inserting the new node just after head.
        self.head.next = new_node

        new_node.data, self.head.data = self.head.data, new_node.data #exchanging the values of new node and head.
        self.head = self.head.next #moving the head to next the node.
    
    
    def delstart(self):
        if self.head == None:   # when the LL is empty.
            print('LL empty')
            return
        
        if self.head.next == self.head:  # when there is only one node.
            self.head = None
            return
        
        curr = self.head
        while curr.next != self.head:
            curr = curr.next
        
        curr.next = self.head.next
        self.head.next = None
        self.head = curr.next

    def Odelstart(self):
        if self.head == None:   # when the LL is empty.
            print('LL empty')
            return
        
        if self.head.next == self.head:  # when there is only one node.
            self.head = None
            return
        
        temp = self.head.next
        self.head.data = temp.data #storing the data of head.next in the head value itself.

        self.head.next = temp.next # changing the pointer of head.next to temp.next.
        temp.next = None #the pointer of temp.next to None.


    def display (self):
        temp = self.head 
        if temp == None:
            return 
 
        while True:
            print (temp.data, end = " ") 
            temp = temp.next 
            if temp== self.head:
                break
    


#Drive Code
ll = circularLL () 
	    
ll.OinsertStart (12) 
ll.insertStart (16) 
ll.insertStart (20) 
	    
ll.insertStart (24) 
ll.insertStart (22) 

ll.OinsertStart(30)
ll.OinsertStart(31)

ll.Oinsertend(100)
ll.Oinsertend(99)

ll.delstart()
ll.delstart()

ll.Odelstart()
ll.Odelstart()
ll.Odelstart()
 
ll.display ()