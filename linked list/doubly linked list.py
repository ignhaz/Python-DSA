class node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class doublylinkedlist:
    def __init__(self):
        self.head = None
    
    def insertionstart(self,ele):
        new_node = node(ele)
        new_node.next = self.head

        #if its the first node.
        if self.head is None:
            self.head = new_node
            return
        
        # if inserting at the first.
        self.head.prev = new_node
        self.head = new_node

    def insertionend(self,ele):  
        new_node = node(ele)

        if self.head == None: #if there is no nodes
            self.head = new_node
            return
        
        temp = self.head
        while temp.next is not None:
            temp = temp.next
        temp.next = new_node
        new_node.prev = temp
    
    def insertatpos(self,ele,pos):

        size = self.calsize()
        if pos<0 or pos>size:
            print('Out of bounds')
            return
        
        if pos == size:
            self.insertionend(ele)
            return

        if pos == 0:
            self.insertionstart(ele)
            return
        
        new_node = node(ele)
 
        temp = self.head
        for i in range(1,pos):
            temp = temp.next

        temp.next.prev = new_node
        new_node.next = temp.next
        temp.next = new_node
        new_node.prev = temp


    def delnode(self,ele):
        if self.head.data == ele: #if element present at first pos.
            temp = self.head
            self.head = temp.next
            self.head.prev = None
            temp.next = None
            return

        temp = self.head
        while temp.data != ele:
            temp = temp.next
        
        if temp.next != None: #if element is not at last pos.
            temp.prev.next = temp.next
            temp.next.prev = temp.prev
            temp.prev = None
            temp.next = None
            return
        else:                 #if element is at last pos
            temp.prev.next = None
            temp.prev = None
            return
        print('Value Not Found')

    def calsize(self):
        temp = self.head
        size = 1
        while temp.next != None:
            temp = temp.next
            size += 1
        return size


    def display (self):
        temp = self.head 
        end = None 
        print ("Linked List in Forward Direction") 
        while temp:
            print (temp.data, end = " ") 
            end = temp 
            temp = temp.next 
        print ("") 
	  
        print ("Linked List in backward direction") 
        while end:
            print (end.data, end = " ") 
            end = end.prev 
        print ("") 

dl = doublylinkedlist()
dl.insertionstart(10)
dl.insertionstart(20)
dl.insertionstart(30)

dl.insertionend(40)
dl.insertionend(50)
dl.insertionend(60)

dl.insertatpos(11,0)

dl.delnode(10)
dl.delnode(20)
dl.delnode(60)

dl.display()
