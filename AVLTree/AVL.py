from customqueue import Queue 
class AVLNode:
    def __init__(self,value):
        self.data = value
        self.left = None
        self.right = None
        self.height = 1

def getHeight(node):
    if node:
        return node.height
    else:
        return 0

def balance(node):
    if node:
        return getHeight(node.left) - getHeight(node.right)

def rightrotation(node):
    newroot = node.left
    temp = newroot.right
    newroot.right = node
    node.left = temp
    newroot.height = 1 + max(getHeight(newroot.left),getHeight(newroot.right))
    node.height = 1 + max(getHeight(node.left),getHeight(node.right))
    return newroot

def leftrotation(node):
    newroot = node.right
    temp = newroot.left
    newroot.left = node
    node.right = temp
    newroot.height = 1 + max(getHeight(newroot.left),getHeight(newroot.right))
    node.height = 1 + max(getHeight(node.left),getHeight(node.right))
    return newroot


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
    
def insert(root,value):
    if not root:
        root = AVLNode(value)
        return root
    elif value < root.data:
        root.left = insert(root.left,value)
    elif value > root.data:
        root.right = insert(root.right,value)
    
    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    # left left condition
    if balance(root) > 1 and balance(root.left)>=0 :
        return rightrotation(root)
    # right right condition
    if balance(root) < -1 and balance(root.right) <= 0:
        return leftrotation(root)
    # left right condition
    if balance(root) > 1 and balance(root.right) <= -1:
        root.left = leftrotation(root.left)
        return rightrotation(root)
    # right left condition
    if balance(root) < -1 and balance(root.left) >= 1:
        root.right = rightrotation(root.right)
        return leftrotation(root)
    return root



def getminvalue(root):
    if not root:
        return root
    temp = root
    while temp.left:
        temp = temp.left
    return temp

def deletion(root,value):
    if not root:
        return
    elif value < root.data:
        root.left = deletion(root.left,value)
    elif value > root.data:
        root.right = deletion(root.right,value)
    else:
        if not root.left:
            temp = root.right
            root = None
            return temp
        if not root.right:
            temp = root.left
            root = None
            return temp
        
        temp = getminvalue(root.right)
        root.data = temp.data
        root.right = deletion(root.right,temp.data)

    root.height = 1 + max(getHeight(root.left),getHeight(root.right))
    # left left condition
    if balance(root) > 1 and balance(root.left)>=0 :
        return rightrotation(root)
    # right right condition
    if balance(root) < -1 and balance(root.right) <= 0:
        return leftrotation(root)
    # left right condition
    if balance(root) > 1 and balance(root.right) <= -1:
        root.left = leftrotation(root.left)
        return rightrotation(root)
    # right left condition
    if balance(root) < -1 and balance(root.left) >= 1:
        root.right = rightrotation(root.right)
        return leftrotation(root)
    return root

def deletetree(root):
    if root:
        root.data = None
        root.left = None
        root.right = None


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
    
    




        
        
    




root = insert(None,12)
root = insert(root,19)
root = insert(root,29)
root = insert(root,39)
root = insert(root,49)
root = insert(root,59)
levelorder(root)
print(" "*25)
root = deletion(root,39)
levelorder(root)
deletetree(root)
levelorder(root)

