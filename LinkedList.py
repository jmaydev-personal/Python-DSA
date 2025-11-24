"""
LinkedList: Pointers in one direction - Big O of O(n)
Doubly LinkedList: Pointers in both directions

Operations: Traverse, display, search, calculate and get length, append, prepend, insert, delete, pop index, get
"""

class Node:
    def __init__(self, value):
        """ Value of node """
        self.value = value 
        """ Pointer to next node - empty be default as last node has nothing to point to"""
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    """Representation of List - Display values in List"""
    def __repr__(self):
        pass

    """Checks if values exist in List"""
    def __contains__(self):
        pass

    """Length of List"""
    def __len__(self):
        pass

    """Add value to end of list"""
    def append(self, value):
        pass

    """Insert value at beginning of List"""
    def prepend(self, value):
        pass

    """Insert to a specific index"""
    def insert(self, value, index):
        pass

    """Delete value from end of List"""
    def delete(self, value):
        pass

    """Delete value from specific index in List"""
    def pop(self, index):
        pass

    """Get value of specific index"""
    def get(self, value):
        pass

    def print(self):
        pass

if __name__ == "__main__":
    pass