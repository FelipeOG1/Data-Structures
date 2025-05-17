class Stack:

    def __init__(self,capacity):
        self.__capacity=capacity
        self.__arr=[0]*self.__capacity
        self.__top = -1

    def push(self,value):
        self.__top+=1

        self.__arr[self.__top]=value
        
       

    def keyTop(self):

        return self.__arr[self.__top]       


    def pop(self):
        value=self.__arr[self.__top]
        
        self.__arr[self.__top]=0
        self.__top-=1




stack=Stack(3)

stack.push(30)

stack.push(20)

stack.pop()
print(stack.keyTop())






