class BinaryTree:

    def __init__(self,rootObj):

        self.key = rootObj
        self.leftChild = None
        self.rightChild = None

    def insertLeft(self,newNode):
        
        if self.leftChild == None:

            self.leftChild = BinaryTree(newNode)
        
        else:

            t = BinaryTree(newNode)
            t.leftChild = self.leftChild
            self.leftChild = t

    def insertRight(self,newNode):
        
        if self.rightChild == None:

            self.rightChild = BinaryTree(newNode)
            
        else:

            t = BinaryTree(newNode)
            t.rightChild = self.rightChild
            self.rightChild = t

    def getRightChild(self):
        return self.rightChild

    def getLeftChild(self):
        return self.leftChild

    def setRootVal(self,obj):
        self.key = obj

    def getRootVal(self):
        return self.key

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)
    
def levelOrder(btree):

    if btree.key == None:
        return

    ## create a queue 
    queue = Queue()

    ## place first value into queue 
    queue.enqueue(btree.key)

    ## create place holders for children of root 
    a = btree.getLeftChild()
    b = btree.getRightChild()


    ## continue while all queue items have not been removed 
    while queue.isEmpty() == False:

        ## remove and print the first value 
        first = (queue.dequeue())
        print (first)

        ## check for left child 
        if (a) != None:

        ## add left child to queue 
            queue.enqueue(a.key)

        ## move to the next level 
            a = a.getLeftChild()
    
        ## check for right child 
        if (b) != None:

        ## add right child to queue
            queue.enqueue(b.key)

        ## move to the next level 
            b = b.getRightChild()
            
            


                
