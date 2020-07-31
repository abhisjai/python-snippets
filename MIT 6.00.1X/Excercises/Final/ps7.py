# Implement the class myDict with the methods below, which will represent a dictionary without using a dictionary object. The methods you implement below should have the same behavior as a dict object, including raising appropriate exceptions. Your code does not have to be efficient. Any code that uses a Python dictionary object will receive 0.
# For example:
# With a dict:       With a myDict:
# -------------------------------------------------------------------------------
# d = {}             md = myDict()        # initialize a new object using 
#                                           your choice of implementation

# d[1] = 2           md.assign(1,2)       # use assign method to add a key,value pair

# print(d[1])        print(md.getval(1))  # use getval method to get value stored for key 1

# del(d[1])          md.delete(1)         # use delete method to remove 
#                                           key,value pair associated with key 1

class myDict(object):
    """ Implements a dictionary without using a dictionary """
    def __init__(self):
        """ initialization of your representation """
        self.dList = []
        self.k = None
        self.v = None
        
    def assign(self, k, v):
        """ k (the key) and v (the value), immutable objects  """
        # If list is empty, then add key and value to dictionary
        
        if self.dList == []:
            self.dList.append([k, v])
        else:
            for i in self.dList:
                if i[0] == k:
                    # Call delete function and then append k and v to the list
                    self.delete(k)

            self.dList.append([k, v])
        
    def getval(self, k):
        """ k, immutable object  """
        #FILL THIS IN
        inList = False

        for i in self.dList:
            if i[0] == k:
                return i[1]

        if not inList:
            raise KeyError(k)
        
    def delete(self, k):
        """ k, immutable object """   

        # Check if element is in the list, if not, raise a KeyError
        inList = False

        for i in self.dList:
            if i[0] == k:
                inList = True
                self.dList.remove(i)

        if not inList:
            raise KeyError(k)
    
    def __str__(self):
        strg = "{"
        for i in self.dList:
            strg = strg + str(i[0]) +": " + str(i[1]) + ", "
      
        strg = strg + "}"
        return strg


md = myDict()
print(md)

md.assign(1,4)
md.assign(2,4)
print(md)

md.assign(1,5)
print(md)

md.delete(1)
print(md)

print(md.getval(1))
print(md)

# md.delete(1)
# md.delete(1)

## A dictionary is also a list without an index.
## A list can act as a dictionary if we ignore index.
## At any given index in list of lists, list[0] will be key and list[1] will be value