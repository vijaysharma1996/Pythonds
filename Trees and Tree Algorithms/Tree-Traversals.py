##preorder, inorder, postorder
##preorder: follow an order of reading a book:
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())
        
 ##inorder: translate a tree into expreesions of operations       
 define inorder(tree):
        if tree!=None:
            inorder(tree.getLeftChild())
            print(tree.getRootVal())
            inorder(tree.getRightChild())
 
 ##application:
 
 def printexp(tree):
     sVal=""
     if tree:
        sVal='('+ printexp(tree.getLeftChild())
        sVal=sVal+printexp(tree.getRootVal())
        sVal=sVal+printexp(tree.getRightChild())+')'
      return sVal
      
 ##postorder, useful for evaluate the tree expression:
 def postorder(tree):
     if tree != None:
         postorder(tree.getLeftChild())
         postorder(tree.getRightChild())
         print(tree.getRootVal())
  
  ##application: rewrite evaluation:
  def postordereval(tree):
       opers = {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
       res1=None
       res2=None
       if tree:
           res1=tree.getLeftTree()
           res2=tree.getRightTree()
           if res1 and res2:
               return opers[tree.getRootVal()](res1,res2)
           else:
               return tree.getRootVal()
               
               
  
  
 
 
       
