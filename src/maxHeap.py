
#Max heap se compone de un arbol binario donde vamos a hacer un insert en cada hoja, si el padre de la hoja es menor, debemos de hacer un sift up.

#Un caso donde se puede hacer un sift down, seria si extraemos el root ya que queremos el elemento con mayor prioridad. Pues este se debe de de reemplazar por una hoja, la cual puede ser menor que sus hijos.




class MaxHeap:

    def __init__(self):

        self.root=None
        self.elems=0

    def insert(self,value):
            self.elems+=1
            def _insert(current,value):

                if value>current.value:
                    if current.right is None:

                        current.right=Node(value)
                    else:

                        _insert(current.right,value)

                else:
                    if current.left is None:
                        current.left=Node(value)

                    else:

                        _insert(current.left,value)

                
        

            if self.root is None:
                self.root=Node(value)
            else:
                
              _insert(self.root,value)


    def inorden(self):
        mamas=[]

        def _inorden(current):
            if current is None:
                return
            _inorden(current.left)
            mamas.append(current.value)
            _inorden(current.right)
            
            
            
    

        if self.root is None:

            return "No existen elementos para mostrar"

        else:
            _inorden(self.root)
            return mamas
            

    

class Node:

    
    def __init__(self,value):

        self.value=value

        self.left=None

        self.right=None






newHeap=MaxHeap()
newHeap.insert(20)
newHeap.insert(10)
arr=newHeap.inorden()


print(arr)

