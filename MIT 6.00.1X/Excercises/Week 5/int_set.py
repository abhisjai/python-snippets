class intSet(object):
    """An intSet is a set of integers
    The value is represented by a list of ints, self.vals.
    Each int in the set occurs in self.vals exactly once."""

    def __init__(self):
        """Create an empty set of integers"""
        self.vals = []

    def insert(self, e):
        """Assumes e is an integer and inserts e into self""" 
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        """Assumes e is an integer
           Returns True if e is in self, and False otherwise"""
        return e in self.vals

    def remove(self, e):
        """Assumes e is an integer and removes e from self
           Raises ValueError if e is not in self"""
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found')

    def __str__(self):
        """Returns a string representation of self"""
        self.vals.sort()
        return '{' + ','.join([str(e) for e in self.vals]) + '}'

    """
        Define an intersect method that returns
        a new intSet containing elements that appear in both sets.
        In other words, s1.intersect(s2)
        would return a new intSet of integers that appear in both s1 and s2.
        Think carefully - what should happen if s1 and s2 have no elements in common?
    """

    def intersect(self, other):
        ''' Assumes other is an intSet object
            returns Object of type intSet ''' 

        commonVal = intSet()
        
        # Loop through all elements in self.vals
        for i in self.vals:
            # Check if this element exists in other.vals
            if other.member(i):
                commonVal.insert(i)
        
        # If no intersection is found, it still returns intSet object
        return commonVal
    
    ''' Add the appropriate method(s) so that len(s) returns the number of elements in s '''
    def __len__(self):
        ''' returns length of self.val as int'''
        return len(self.vals)


s1 = intSet()
s1.insert(3)
s1.insert(4)
s1.insert(5)
print(s1)

s2 = intSet()
s2.insert(4)
s2.insert(5)
print(s2)

print(s1.intersect(s2))
print(len(s1.intersect(s2)))