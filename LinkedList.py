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

    # Checks if values exist in List - return true/false
    # O(n) linear time
    def __contains__(self, value):
        last = self.head
        while last is not None:
            # check value of node against parameter
            if last.value == value:
                return True
            # iterate through each node
            last = last.next
        return False

    """Length of List"""
    def __len__(self):
        pass

    # Append - Add value to end of list - O(n) linear time
    def append(self, value):
        # if no head node, create it
        if self.head == None:
            self.head = Node(value)
        else:
            # traverse the list until you get to the last node
            last = self.head
            while last.next:
                last = last.next
            last.next = Node(value)

    # Insert value at beginning of List - O(1) constant time
    def prepend(self, value):
        # initialise the node with the value to prepend
        first_node = Node(value)
        # point to the current head 
        first_node.next = self.head
        # replace head with new node
        self.head = first_node

    # Insert to a specific index - O(n) - linear time
    def insert(self, value, index):
        # if adding at start of list, prepend
        if index == 0:
            self.prepend(value)
        else:
            # if List is empty, throw error
            if self.head == None:
                raise ValueError("Index out of bounds")
            else:
                # otherwise make last the head node (to point to inserted node later)
                last = self.head

                for i in range(index-1):
                    # if index doesn't exist, throw error
                    if last.next is None:
                        raise ValueError("Index out of bounds")
                    # otherwise make last point to the next node
                    last = last.next
                
                # make node to insert
                new_node = Node(value)
                # point to node at index of insertion
                new_node.next = last.next
                # previous node now points to new node
                last.next = new_node


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