##application of tree data structure
##use stack to track the parent and children of a tree
from pythonds.basic import Stack
from pythonds.trees import BinaryTree

def buildParseTree(fpexp):
####tokenize the expression to follow the rules:
    fplist=fpexp.split()
    pStack=Stack()
    eTree=BinaryTree('')
    pStack.push(eTree)
    currentTree=eTree
    
    for i in fplist:
        if i == '(':
           currentTree.insertLeft('')
           pStack.push(currentTree)
           currentTree=currentTree.getLeftChild()
           
        elif i in ['+', '-', '*', '/']:
            currentTree.setRootVal(i)
            currentTree.insertRight('')
            pStack.push(currentTree)
            currentTree=currentTree.getRightChild()
            
         elif i == ')':
             currentTree=pStack.pop()
             
         elif i not in ['+', '-', '*', '/',')']:
            try:
                 currentTree.setRootVal(int(i))
                 parent=pStack.pop()
                 currentTree=parent
            except ValueError:
                 raise ValueError("token '{}' is not a valid interger'.format(i))
                 
       return eTree  
       
 
 ###use operator to calculate/evaluate the parsed tree
 import operator
 def evaluate(parseTree):
     opers =  {'+':operator.add, '-':operator.sub, '*':operator.mul, '/':operator.truediv}
     ##calculate the operation results as long as there are left and right child
     left=parseTree.getLeftChild()
     right=parseTree.getRightChild()
     
     if left and right:
          ##get the operation
          fn=opers[parseTree.getRootVal()]
          return fn(evaluate(left),evaluate(right))
          
     else:
         return parseTree.getRootVal()
        
          
 
 
 
 
          
             
             
             
           
