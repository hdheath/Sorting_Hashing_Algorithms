

class HashTable:
    def __init__(self):

        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self,key,data):

      hashvalue = self.hashfunction(key,len(self.slots))

      if self.slots[hashvalue] == None:
          
          self.slots[hashvalue] = key
          self.data[hashvalue] = data

      else:
          
            if self.slots[hashvalue] == key:
              
                self.data[hashvalue] = data  

            else:

                ## set an initial value
                
                n = 1

                ## try to rehash for a new slot using quadratic probing 
                nextslot = rehash(hashvalue,n,len(self.slots))

                ## increase the n value for the quad. equation 
                n = n + 1

                ## increase the number of slots by one 
                self.slots.extend([None])
                self.data.extend([None])

            while self.slots[nextslot] != None and self.slots[nextslot] != key:

                ## probe once again for a new quadratic hash value 
                nextslot = rehash(hashvalue,n,len(self.slots))

                ## increase quad equation variable once again 
                n = n + 1

                ## append another one slot to hash table 
                self.slots.extend([None])
                self.data.extend([None])

            if self.slots[nextslot] == None:
              
              self.slots[nextslot]=key
              self.data[nextslot]=data
              
            else:
              self.data[nextslot] = data 

    def hashfunction(self,key,size):

        return key%size

def rehash(x,n,size):

        ## return new quadratic hash value 
        return ((x + (n * n)) % size)
        
        
        
             
         
