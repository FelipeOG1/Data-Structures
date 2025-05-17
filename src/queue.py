class Queue: 

    def __init__(self,size):
        self.__size=size
        self.__arr=[0] * size

        self.__read=0
        self.__write=0
    
    def isEmpty(self):
        
        if self.__write==self.__read:
            return True

        return False


    def enqueue(self,value):
        if self.__write==self.__size:
            return "max Capacity"
        self.__arr[self.__write]=value
        self.__write+=1

    def dequeue(self):

        if self.__write==self.__read:
            return "No elements to dequeue"

        elem=self.__arr[self.__read]
        
        self.__read +=1
        
        return elem


        

queue=Queue(5)

queue.enqueue(10)

queue.enqueue(200)

queue.enqueue(2)

queue.enqueue(1)

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.dequeue())

print(queue.isEmpty())
