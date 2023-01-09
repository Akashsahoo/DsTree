class TreeNode:
    def __init__(self,data):
        self.data = data
        self.children = []
    
    def __str__(self,level=0):
        ret = "  "*level + str(self.data)+"\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addchild(self,treenode):
        self.children.append(treenode)
        
Drinks = TreeNode('Drinks')
Cold = TreeNode('Cold')
Coca = TreeNode('Coca')
Pepsi = TreeNode('Pepsi')
Fanta = TreeNode('Fanta')
Hot = TreeNode('Hot')
Tea = TreeNode('Tea')
Coffee = TreeNode('Coffee')
        
        
Drinks.addchild(Cold)
Drinks.addchild(Hot)
Cold.addchild(Coca)
Cold.addchild(Fanta)
Coca.addchild(Pepsi)
Hot.addchild(Tea)
Hot.addchild(Coffee)

print(Drinks)