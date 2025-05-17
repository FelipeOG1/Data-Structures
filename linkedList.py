
class LinkedList:
    def __init__(self):
        self.head=None

    def pushFront(self,value):
        newNode=Node(value)
        
        if not self.head:
            self.head=newNode
            return
        newNode.next=self.head
        self.head=newNode

    def keyTopFront(self):
        
        if not self.head:
            print("La lista se encuentra vacia")
            return
        
        return self.head.value

    def popTopFront(self):
        x=self.head
        if not self.head:
            print("La lista esta vacia")
            return
        self.head=self.head.next
        
        x.next=None
        return x.value


    def pushBack(self,value):
        newNode=Node(value)
        if not self.head:
            self.head=newNode
        current=self.head
        while current.next:
            current=current.next

        current.next=newNode

        print(f"Agregaste el numero {newNode.value} al final de la lista")
    
    def keyTopBack(self):
        current=self.head
        while current.next:
            current=current.next
        
        return current.value
    def popTop(self):

        if not self.head:
            print("Ingrese un elemento primero")
            return

        current=self.head

        while current.next:
            prev=current
            current=current.next
        
        x=current
        prev.next=None
        
        return x.value
    
    def eraseElement(self,key):
        
        if not self.head.next:
            self.head=None
            return self.head
        
        current=self.head
        
        while current.next:
            if currente.next.value==key:
                current.next=currente.next.next
                return
            
            current=current.next

    def mostarElementos(self):
        current=self.head

        
        print(self.head.value)
        while current.next:
            print(current.next.value)
            current=current.next
            

                    
    
        
class Node:
    
    def __init__(self,value):
        self.value=value
        self.next=None



li=LinkedList()

li.pushFront(30)
li.pushFront(20)
li.pushFront(10)
li.pushBack(1000)
li.mostarElementos()




