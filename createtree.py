#   Created by Elshad Karimov on 05/06/2020.
#   Copyright © 2020 AppMillers. All rights reserved.

class TreeNode:
    def __init__(self, data, children = []):
        self.data = data
        self.children = children
    
    def __str__(self, level=0):
        ret = "  " * level + str(self.data)  + "\n"
        for child in self.children:
            ret += child.__str__(level + 1)
        return ret
    
    def addChild(self, TreeNode):
        self.children.append(TreeNode)

class Tree:
      root = None
      def __str__(self):
        return str(self.root)
         
        

          


tree = TreeNode('Drinks', [])
cold = TreeNode('Cold', [])
hot = TreeNode('Hot', [])
coca = TreeNode('Coca',[])
pepsi = TreeNode('Pepsi',[])
tree.addChild(cold)
tree.addChild(hot)
tea = TreeNode('Tea', [])
coffee = TreeNode('Coffee', [])
cola = TreeNode('Cola', [])
fanta = TreeNode('Fanta', [])
cold.addChild(cola)
cold.addChild(fanta)
cola.addChild(coca)
cola.addChild(pepsi)
hot.addChild(tea)
hot.addChild(coffee)
# print(tree)

tree1 = Tree()
tree1.root = tree
print(tree1)