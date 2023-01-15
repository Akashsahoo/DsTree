class Heap:
    def __init__(self,size) :
        self.customlist = [None] *(size + 1)
        self.heapsize = 0
        self.maxsize = size + 1

def peekofHeap(rootNode):
    if not rootNode:
        return 
    else:
        return rootNode.customlist[1]

def sizeofHeap(rootNode):
    if not rootNode:
        return
    else:
        return rootNode.heapsize

def levelorder(rootNode):
    if not rootNode:
        return
    else:
        for i in range(1,rootNode.heapsize+1):
            print(rootNode.customlist[i])

def heapifyTreeInsert(rootNode,index,heapType):
    parentIndex = int(index/2)
    if index <=1:
        return
    if heapType == "Min":
        if rootNode.customlist[index] < rootNode.customlist[parentIndex]:
            temp = rootNode.customlist[index]
            rootNode.customlist[index] = rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)
    elif heapType == "Max":
        if rootNode.customlist[index] > rootNode.customlist[parentIndex]:
            temp = rootNode.customlist[index]
            rootNode.customlist[index] = rootNode.customlist[parentIndex]
            rootNode.customlist[parentIndex] = temp
        heapifyTreeInsert(rootNode,parentIndex,heapType)

def insertNode(rootNode,value,heapType):
    if rootNode.heapsize + 1 == rootNode.maxsize:
        return "The Binary Heap is full"
    rootNode.customlist[rootNode.heapsize + 1] = value
    rootNode.heapsize +=1
    heapifyTreeInsert(rootNode,rootNode.heapsize,heapType)
    return "The value has been sucessfully inserted"

def heapifyTreeExtract(rootNode,index,heapType):
    leftIndex = index * 2
    rightIndex = index * 2 +1
    swapchild = -1
    if rootNode.heapsize < leftIndex:
        return
    elif rootNode.heapsize == leftIndex:
        if heapType == "Min":
            if rootNode.customlist[index] > rootNode.customlist[leftIndex]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[leftIndex]
                rootNode.customlist[leftIndex] = temp
            return
        else:
            if rootNode.customlist[index] < rootNode.customlist[leftIndex]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[leftIndex]
                rootNode.customlist[leftIndex] = temp
            return
    
    else:
        if heapType == "Min":
            if rootNode.customlist[leftIndex] < rootNode.customlist[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex
            if rootNode.customlist[index] > rootNode.customlist[swapchild]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[swapchild]
                rootNode.customlist[swapchild] = temp
        
        else:
            if rootNode.customlist[leftIndex] > rootNode.customlist[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex
            if rootNode.customlist[index] < rootNode.customlist[swapchild]:
                temp = rootNode.customlist[index]
                rootNode.customlist[index] = rootNode.customlist[swapchild]
                rootNode.customlist[swapchild] = temp
            heapifyTreeExtract(rootNode,swapchild,heapType)

def extractNode(rootNode,heapType):
    if rootNode.heapsize == 0 :
        return
    else:
        extractNode = rootNode.customlist[1]
        rootNode.customlist[1] = rootNode.customlist[rootNode.heapsize]
        rootNode.customlist[rootNode.heapsize] = None
        rootNode.heapsize -=1
        heapifyTreeExtract(rootNode,1,heapType)
        return extractNode

    
def deletionEntireBH(rootNode):
    rootNode.customlist = None
    



    
newBinaryHeap = Heap(5)
insertNode(newBinaryHeap,4,"Max")
insertNode(newBinaryHeap,5,"Max")
insertNode(newBinaryHeap,2,"Max")
insertNode(newBinaryHeap,1,"Max")
print(extractNode(newBinaryHeap,"Max"))
levelorder(newBinaryHeap)