class BinaryTree:
    def __init__(self):
        self.root=None


    def insert(self,value):
        
        def _insert(current,value):
            if value<current.value:
                if current.left is None:
                    current.left=Node(value)
                else:
                    _insert(current.left,value)

            else:
                if current.right is None:
                    current.right=Node(value)

                else:
                    _insert(current.right,value)

            
        if self.root is None:
            self.root=Node(value)
        else:
            _insert(self.root,value)
    def inorden(self):
        result=[]

        def _inorden(current):
            if current is None:
                return
            _inorden(current.left)
            result.append(current.value)
            _inorden(current.right)

        _inorden(self.root)
        return result
    def preorden(self):
        result=[]
        def _preorden(current):
            if current is None:
                return
            result.append(current.value)
            _preorden(current.left)
            _preorden(current.right)
        _preorden(self.root)
        return result

    def postorden(self):
        result=[]
        def _postorden(current):
            if current is None:
                return
            _postorden(current.left)
            _postorden(current.right)
            result.append(current.value)
        _postorden(self.root)
        return result

class Node:

    def __init__(self,value):
        self.value=value
        self.right=None
        self.left=None


if __name__=="__main__":

    tree=BinaryTree()
    tree.insert(10)
    tree.insert(2)
    tree.insert(1)
    result_inorden=tree.inorden()

    result_preorden=tree.preorden()

    result_postorden=tree.postorden()

    final={"inorder":result_inorden,"postorden":result_postorden,"preorden":result_preorden}

    print(final)


