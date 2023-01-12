from customqueue import Queue 
class BSTNode:
    def __init__(self,data) :
        self.data = data
        self.left = None
        self.right = None

def levelorder(root):
    if not root:
        return 
    else:
         customqueue = Queue()
         customqueue.enqueue(root)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            print(treenode.value.data)
            leftchild = treenode.value.left
            if leftchild:
                customqueue.enqueue(leftchild)
            rightchild = treenode.value.right
            if rightchild:
                customqueue.enqueue(rightchild)

def preorder(root):
    if root:
        print(root.data)
        preorder(root.left)
        preorder(root.right)

def inorder(root):
    if root:
        inorder(root.left)
        print(root.data)
        inorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.data)
    

def insertnode(root,value):
    if not root:
        root = BSTNode(value)
    elif value < root.data:
        if not root.left:
           root.left = BSTNode(value)
           
        else:
            root.left = insertnode(root.left,value)
            
    elif value > root.data:
        if not root.right:
            root.right = BSTNode(value)
        else:
            root.right = insertnode(root.right,value)
    # print("node inserted sucessfully")
    return root

def searchnode(root,value):
    if not root:
        print("Data not found")
        return 
    else:
        if root.data < value:
            searchnode(root.right,value)
            return
        elif root.data > value:
            searchnode(root.left,value)
            return
        else:
            print("Data found")
            return

def minvaluenode(bstNode):
    current = bstNode
    while (current.left is not None):
        current = current.left
    return current


def deletenode(root,value):
    if not root:
        print("Data not found")
        return
    if root.data < value:
        root.right = deletenode(root.right,value)
    elif root.data > value:
        root.left = deletenode(root.left,value)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        if not root.right:
            temp = root.left
            root = None
            return temp
        
        temp = minvaluenode(root.right)
        root.data = temp.data
        root.right = deletenode(root.right,temp.data)
    return root

def deletetree(root):
    root.data = None
    root.left = None
    root.right = None
    

        
      
 
#root = BSTNode(10)
root = insertnode(None,12)
# levelorder(root)
root = insertnode(root,11)
root = insertnode(root,18)
root = insertnode(root,19)
levelorder(root)
# preorder(root)
# inorder(root)
# postorder(root)
# searchnode(root,19)
root = deletenode(root,12)
print(" "*20)
levelorder(root)