class HashTable:
    def __init__(self):

        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size
        self.items = 0

    def put(self,key,data):

      hashvalue = self.hashfunction(key,len(self.slots))

    ## if the number of items is going to exceed capacity : 
      if self.items == self.size:

    ## extend the hash table to the length of the returned value 
          self.slots.extend([None]*(self.get_prime()-self.items))
          self.data.extend([None]*(self.get_prime()-self.items))

    ## change the variable size to equal the returned value 
          self.size = self.get_prime()
          
      if self.slots[hashvalue] == None:

        self.slots[hashvalue] = key
        self.data[hashvalue] = data
        self.items = self.items + 1
        
      else:

        if self.slots[hashvalue] == key:
          self.data[hashvalue] = data  #replace

        else:

          nextslot = self.rehash(hashvalue,len(self.slots))

          while self.slots[nextslot] != None and self.slots[nextslot] != key:
              
              nextslot = self.rehash(nextslot,len(self.slots))

          if self.slots[nextslot] == None:

            self.slots[nextslot]=key
            self.data[nextslot]=data
            self.items = self.items + 1

          else:

            self.data[nextslot] = data #replace

    def hashfunction(self,key,size):
        return key%size

    def rehash(self,oldhash,size):
        return (oldhash+1)%size

    def get_prime(self):

        ## double the initial number of items 
        prime = self.items * 2

        ## divide the doubled number by numbers ranging from 2
        ## to the doubled number 
        for i in range(2,prime):

        ## if doubled number is divisible, increase doubled
        ## number by one 
            if (prime % i == 0):
                prime = prime + 1

        ## if doubled number is not divisible by a number in the
        ## range, return that as the new size 
            else:
                return prime 
           
        

