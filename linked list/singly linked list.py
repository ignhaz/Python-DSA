class node:
    def __init__(self,ele):
        self.data = ele
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None
    
    def insertstart(self,ele):
        new_node = node(ele)
        new_node.next = self.head
        self.head = new_node
    
    def insertlast(self,ele):
        new_node = node(ele)
        new_node.next = None

        if self.head == None:
            self.head = new_node
            return

        temp = self.head
        while temp.next is not None:
            temp = temp.next         
        temp.next = new_node
    
    def insertmiddle(self,pos,ele):
        size = self.calsize()
        if pos == 0:
            self.insertstart(ele)
        if pos < 0 or size < pos:
            print('Cannot be inserted')
        else:
            new_node = node(ele)
            temp = self.head
        
        for i in range(1,pos):
            temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node        
        

    def calsize(self):
        size = 0
        temp = self.head
        while temp.next is not None:
            temp = temp.next
            size += 1
        return size

    def display(self) :
        temp = self.head 
        while temp : 
            print (temp.data, end = " ") 
            temp = temp.next 

    def delete(self,ele):
        temp = self.head

        if temp.next is None: #when there is only single node.
            self.head = None
            return

        if temp.data == ele: #when the value is in head node only.
            self.head = temp.next
            return
        
        while temp.next != None and temp.data != ele: #when the value is in between somewhere.
            prev = temp
            temp = temp.next
        
        if temp.next == None and temp.data != ele:
            print('Value not found')
            return
        
        prev.next = temp.next


ll = linkedlist() 

ll.insertstart(12) 
ll.insertstart(16) 
ll.insertstart(20)

ll.insertlast(10) 
ll.insertlast(14) 
ll.insertlast(18) 
ll.insertlast(11) 

ll.insertmiddle(3, 25) 

# ll.delete(10)
# ll.delete(20)
# ll.delete(16)
ll.delete(60)

ll.display() 