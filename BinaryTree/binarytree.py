from customqueue import Queue 
class TreeNode:
    def __init__(self,data):
        self.data = data
        self.leftchild = None
        self.rightchild = None

# left root right
# a + b inorder
# binarytree = TreeNode('Drinks')
# lefttree = TreeNode('Hot')
# righttree = TreeNode('Cold')
# binarytree.leftchild = lefttree
# binarytree.rightchild = righttree

newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftchild = tea
leftChild.rightchild = coffee
rightChild = TreeNode("Cold")
newBT.leftchild = leftChild
newBT.rightchild = rightChild

def preorder(root):
    if not root:
        return None
    else:
        print(root.data)
        preorder(root.leftchild)
        preorder(root.rightchild)

#preorder(binarytree)

def inorder(root):
    if not root:
        return None
    else:
        
        inorder(root.leftchild)
        print(root.data)
        inorder(root.rightchild)
#inorder(binarytree)

def postorder(root):
    if not root:
        return None
    else:
        postorder(root.leftchild)
        postorder(root.rightchild)
        print(root.data)
# postorder(binarytree)
        
def levelorder(root):
    if not root:
        return 
    else:
         customqueue = Queue()
         customqueue.enqueue(root)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            print(treenode.value.data)
            leftchild = treenode.value.leftchild
            if leftchild:
                customqueue.enqueue(leftchild)
            rightchild = treenode.value.rightchild
            if rightchild:
                customqueue.enqueue(rightchild)
            


#levelorder(newBT)   
# levelorder(binarytree)
# customqueue = customqueue()

# customqueue.enqueue(1)
# customqueue.enqueue(2)
# customqueue.enqueue(3)
# print(customqueue)
# print(customqueue.peek())

# print(customqueue.dequeue())
# print(customqueue)
    

def searchbt(root,searchnodevalue):
    if not root:
        return 
    else:
         customqueue = Queue()
         customqueue.enqueue(root)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            if treenode.value.data == searchnodevalue:
                print(treenode.value.data)
                return

            leftchild = treenode.value.leftchild
            if leftchild:
                customqueue.enqueue(leftchild)
            rightchild = treenode.value.rightchild
            if rightchild:
                customqueue.enqueue(rightchild)
         print("not found") 

def insertNodeBT(rootNode, newvalue):
    newNode = TreeNode(newvalue)
    if not rootNode:
        rootNode = newNode
        return "data inserted"
    else:
         customqueue = Queue()
         customqueue.enqueue(rootNode)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            leftchild = treenode.value.leftchild
            if leftchild:
                customqueue.enqueue(leftchild)
            else:
                treenode.value.leftchild = newNode
                return "data inserted"
            rightchild = treenode.value.rightchild
            if rightchild:
                customqueue.enqueue(rightchild)
            else:
                treenode.value.rightchild = newNode
                return "data inserted"

         

#searchbt(newBT,"Cold")

# levelorder(newBT)
# insertNodeBT(newBT,'momos')
# levelorder(newBT)


def getdeepestNodeBT(rootNode):
    
    if not rootNode:
        
        return None
    else:
         customqueue = Queue()
         customqueue.enqueue(rootNode)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            leftchild = treenode.value.leftchild
            if leftchild:
                customqueue.enqueue(leftchild)
            
            rightchild = treenode.value.rightchild
            if rightchild:
                customqueue.enqueue(rightchild)
         return treenode.value


def deletedeepestNodeBT(rootNode,deepNode):
    
    if not rootNode:
        
        return None
    else:
         customqueue = Queue()
         customqueue.enqueue(rootNode)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            if treenode.value == deepNode:
                treenode.value = None
                return

            leftchild = treenode.value.leftchild
            if leftChild == deepNode:
                treenode.value.leftchild = None
                return
            elif leftchild:
                customqueue.enqueue(leftchild)
            
            rightchild = treenode.value.rightchild
            if rightchild == deepNode:
                treenode.value.rightchild = None
                return
            elif rightchild:
                customqueue.enqueue(rightchild)
        
# levelorder(newBT)
#print(getdeepestNodeBT(newBT).data)
# deepest_node = getdeepestNodeBT(newBT)
# deletedeepestNodeBT(newBT,deepest_node)

print("Before \n")
levelorder(newBT)
print("\n")

def deleteNodeBT(rootNode,dNode):
    if not rootNode:
        return None
    else:
         customqueue = Queue()
         customqueue.enqueue(rootNode)
         while not  customqueue.isEmpty():
            treenode = customqueue.dequeue()
            if treenode.value.data == dNode:
                deepnode = getdeepestNodeBT(rootNode)
                treenode.value.data = deepnode.data
                deletedeepestNodeBT(newBT,deepnode)
                
                
                return

            leftchild = treenode.value.leftchild
            # if leftChild == dNode:
            #     treenode.value.leftchild = None
            #     return
            if leftchild:
                customqueue.enqueue(leftchild)
            
            rightchild = treenode.value.rightchild
            # if rightchild == dNode:
            #     treenode.value.rightchild = None
            #     return
            if rightchild:
                customqueue.enqueue(rightchild)
deleteNodeBT(newBT,'Coffee')
print("after \n")
# levelorder(newBT)

def deleteBT(rootNode):
    rootNode.data = None
    rootNode.leftchild = None
    rootNode.rightchild = None
    return "The BT has been successfully deleted" 

# levelorder(newBT)
# deleteBT(newBT)
levelorder(newBT)