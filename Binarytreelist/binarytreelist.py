class BinaryTree:
    def __init__(self,size) :
        self.list = [None]*size
        self.maxsize = size
        self.lastusedindex = 0
    
    def insertNode(self,value):
        if self.lastusedindex + 1 == self.maxsize:
           return "index out of range"
        else:
            self.list[self.lastusedindex + 1]  = value
            self.lastusedindex  += 1
            return "value successfully inserted"
    
    def searchnode(self,node,index=1):
        for ind in range(index,self.lastusedindex+1):
            if self.list[ind] == node:
                return "data found"
        print("data not found")
    
    def preorder(self,index):
        if index > self.lastusedindex:
            return 
        print(self.list[index])
        self.preorder(index*2)
        self.preorder(index*2 + 1)
    
    def inorder(self,index):
        if index > self.lastusedindex:
            return 
        
        self.inorder(index*2)
        print(self.list[index])
        self.inorder(index*2 + 1)
    
    def postorder(self,index):
        if index > self.lastusedindex:
            return 
        
        self.postorder(index*2)
        self.postorder(index*2 + 1)
        print(self.list[index])
    
    def levelorder(self,index=1):
        for i in range(index,self.lastusedindex+1):
            print(self.list[i])
    
    def deletenode(self,value):
        if self.lastusedindex == 0:
            return "There is not any node to delete"
        for i in range(1,self.lastusedindex+1):
            if self.list[i] == value:
                self.list[i] = self.list[self.lastusedindex]
                self.list[self.lastusedindex] = None
                self.lastusedindex -=1
                return "node has been sucessfully deleted"
    
    def deletebt(self):
        self.list = None
        self.lastusedindex = 0








newBt = BinaryTree(8)
newBT = BinaryTree(8)
print(newBT.insertNode("Drinks"))
newBT.insertNode("Hot")
newBT.insertNode("Cold")
newBT.insertNode("Tea")
newBT.insertNode("Coffee")
# print(newBT.searchnode("Col"))
#newBT.preorder(1)
#newBT.inorder(1)
# newBT.postorder(1)
# newBT.levelorder()
# newBT.deletenode("Tea")
# newBT.levelorder()
newBT.deletebt()
newBT.levelorder()
