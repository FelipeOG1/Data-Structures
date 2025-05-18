import sys

class StackWithMax():
    def __init__(self):
        self.__stack = []
        self.__max=0
        self.__maxStack=[]

    def Push(self, a):
        if  self.__max<=a:
                self.__max=a
                self.__maxStack.append(a)
        self.__stack.append(a)

    def Pop(self):
        assert(len(self.__stack))
        if self.__stack.pop() == self.__maxStack[-1]:
            self.__maxStack.pop()

    def Max(self):
        assert(len(self.__stack))
        return self.__maxStack[-1]
if __name__ == '__main__':
    stack = StackWithMax()

    num_queries = int(sys.stdin.readline())
    for _ in range(num_queries):
        query = sys.stdin.readline().split()

        if query[0] == "push":
            stack.Push(int(query[1]))
        elif query[0] == "pop":
            stack.Pop()
        elif query[0] == "max":
            print(stack.Max())
        else:
            assert(0)
