### build a binary tree, recursive trees with one root, left subtree and right subtree
def BinaryTree(r):
    return[r,[],[]]
    
def insertLeft(root,newBranch):
    left=root.pop(1)
    if len(left)>1:
    ###if already have left subtree, push it down
        root.insert(1,[newBranch,left,[]])
    else:
        root.insert(1,[newBranch,[],[]])
    return root
     
 def insertRight(root, newBranch):
     right=root.pop(2)
     if len(right)>1:
         root.insert(2, [newBranch,[],right])
     else:
         root.insert(2,[newBranch,[],[]])
     return root
      
  def getRootVal(root):
      return root[0]
      
  def setRootVal(root,newVal):
      root[0]=newVal
      
  def getLeftChild(root):
      return root[1]
      
  def getRightChild(root):
      return root[2]
      
  def buildTree(root):
      r=BinaryTree('a')
      insertLeft(r,'b')
      insertRight(r,'c')
      insertRight(getLeftChild(r),'d')
      insertLeft(getRightChild(r),'e')
      insertRight(getRightChild(r),'f')
      return print(r)
