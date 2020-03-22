##define binary trees as nodes with two references, left and right:
##define binary trees as nodes with two references, left and right:
from test import testEqual

##define binary trees as nodes with two references, left and right:
class BinaryTree:
    def __init__(self, rootObj):
        self.key=rootObj
        self.leftChild=None
        self.rightChild=None
        
    def insertLeft(self, newNode):
        if self.leftChild==None:
            self.leftChild=BinaryTree(newNode)
        else:
            temp=BinaryTree(newNode)
            temp.leftChild=self.leftChild
            self.leftChild=temp
             
    def insertRight(self, newNode):
        if self.rightChild==None:
            self.rightChild=BinaryTree(newNode)
        else:
            temp=BinaryTree(newNode)
            temp.rightChild=self.rightChild
            self.rightChild=temp
              
    def getRightChild(self):
        return self.rightChild
          
    def getLeftChild(self):
        return self.leftChild
          
    def setRootVal(self, obj):
        self.key=obj
         
    def getRootVal(self):
        return self.key
    
r=BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
left=r.getLeftChild()
left.insertRight('d')
right=r.getRightChild()
right.insertLeft('e')
right.insertRight('f')
print(r.getRightChild().getRightChild().getRootVal())

