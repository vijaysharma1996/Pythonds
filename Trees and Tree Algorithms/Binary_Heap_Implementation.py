##define functions for min heap: append, delmin
##Note: complete binary trees: parent's position = i, leftChild=i*2, rightChild=i*2+1(position 0 is 0)

class BinHeap:
    def __init__(self):
        self.heaplist=[0]
        self.currentSize=0
        
    ###when append, append it first to the end of the heap, and swap with parent until it follows the order
    ##first define a swap up function
    def percUp(self,i):
      while i//2>0:
        if self.heaplist[i]< self.heaplist[i//2]:
            temp=self.heaplist[i//2]
            selfheaplist[i//2]=selfheaplist[i]
            selfheaplist[i]=temp
        i=i//2
        
     def insert(self,k):
         self.heaplist.append(k)
         self.currentSize=self.currentSize+1
         self.percUp(self.currentSize)
         
     ###delete the minimal: the minimal will be in position 1, remove it, reduce the size, and move the last element to position 1, and 
     ###keep move it down until it follows the order again
     ##when compare downward, need to compare with both children, only swap with the smaller child
     def minChild(self, i):
     ###if there is no right child
         if i*2+1>self.currentSize:
            return i*2
         else:
             if self.heaplist[i*2]>self.heaplist[i*2+1]:
                 return i*2+1
             else:
                 return i*2
       
      def percDown(self,i):
          while i*2 <= self.currentSize:
          minc=self.minChild(i)
          if heaplist[i]> heaplist[minc]:
             temp=heaplist[minc]
             heaplist[minc]=heaplist[i]
             heaplist[i]=temp
          i=minc
          
       def delMin(self):
           retVal=self.heaplist[1]
           self.heapList[1]=self.heaplist[self.currentSize]
           self.currentSize=self.currentSize-1
           self.heaplist.pop()
           self.percDown(1)
           return retval
           
       def buildHeap(self,alist):
           i= len(alist)//2
           self.currentSize=len(alist)+1
           self.heaplist=[0]+alist[:]
           while (i>0):
               self.percDown(i)
               i -= 1 ##check all parents in every level
       
       
       
           
     
         
      
        
           
        
        
        
