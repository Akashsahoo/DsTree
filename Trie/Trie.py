class TrieNode:
    def __init__(self) :
        self.children = {}
        self.endofstring = False

class Trie:
    def __init__(self) :
        self.root = TrieNode()
    
    def insertstring(self,word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if not node:
                node = TrieNode()
                current.children.update({ch:node})
            current = node
        current.endofstring = True
        print("sucessfully inserted")
    
    def searchstring(self,word):
        current = self.root
        for i in word:
            node = current.children.get(i)
            if not node:
                return False
            current = node
        if current.endofstring == True:
            return True
        else:
            return False

def deletestring(root,word,index):
    ch = word[index]
    currentnode = root.children.get(ch)
    canthisnodedeleted = False

    if len(currentnode.children)> 1:
        deletestring(currentnode,word,index+1)
        return False
    if index == len(word) - 1 :
        if len(currentnode.children) >= 1:
            currentnode.endofstring = False
            return False
        else:
            root.children.pop(ch)
            return True
    if currentnode.endofstring == True:
        deletestring(currentnode,word,index+1)
        return False

    canthisnodedeleted = deletestring(currentnode,word,index+1)
    if canthisnodedeleted == True:
        root.children.pop(ch)
        return True
    else:
        return False
            





trie = Trie()
trie.insertstring("Akash")
trie.insertstring("Priya")
trie.insertstring("Shubham")
deletestring(trie.root,"Shubham",0)
print(trie.searchstring("Shubham"))