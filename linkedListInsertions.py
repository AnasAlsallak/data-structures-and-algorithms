from typing import Union, List


class Node:
    """
    A node in a linked list
    """

    def __init__(self, value):
        self.value = value
        self.next: Union[Node, None] = None


class LinkedList:
    """
    A linked list

    Attributes:
        head (Node): The head of the linked list
        length (int): The length of the linked list
    """

    def __init__(self):
        self.head = None
        self.length = 0

    count = 0    

    def __str__(self):
        return self.to_string()
    
    def insert(self, value):
        """
        Insert a new node at the head of the linked list

        Args:
            value (any): The value of the new node
        """
        old_node = self.head
        new_node = Node(value)

        new_node.next = old_node
        self.head = new_node
        self.length += 1


    def includes(self, value):
        """
        Check if a node with a given value exists

        Args:
            value (any): The value of the node to check for

        Returns:
            bool: True if the node exists, False otherwise  
        """
        curr = self.head
        while (curr is not None):
            if (curr.value == value):
                return True
            curr = curr.next
        return False

    def to_string(self):
        """
        Converts the linked list to a string

        Returns:
            str: The string representation of the linked list
        """
        output = ""
        curr = self.head
        while (curr is not None):
            output += f"{{ {curr.value} }} -> "
            curr = curr.next
        output += "NONE"
        return output
    
    def get_values(self) -> List:
        """
        Returns a list of all the values in the linked list

        Returns:
            List: A list of all the values in the linked list
        """
        values = []
        curr = self.head
        while curr is not None:
            values.append(curr.value)
            curr = curr.next
        return values
    
    def append(self,value):        
        """        
        Append a new node with the given value to the end of the linked list.        
        Parameters:            
        value: any            
        The value to be stored in the new node.            
        Returns:            
        None
        """        
        node = Node(value)                
        if self.head is None:            
            self.head = node        
        else:            
            current = self.head            
            while current.next is not None:                
                current = current.next            
            current.next = node
        self.length += 1

    def insert_before(self, target, value):
        """
        Insert a new node with the given value before a specified target value in the linked list.

        Parameters:
            target: any
                The target value before which the new node should be inserted.
            value: any
                The value to be stored in the new node.

        Returns:
            None
        """
        if self.includes(target):
            node = Node(value)

            if self.head == None or self.head.value == target:
                self.insert(value)

            else:
                current = self.head
                while current.next.value is not target:
                    current = current.next
                target = current 
                node.next = target.next
                target.next = node

        else:
            print("This target value doesn't exist.")

        self.length += 1

    def insert_after(self, target, value):
        """
        Insert a new node with the given value after a specified target value in the linked list.

        Parameters:

            target: any
                The target value after which the new node should be inserted.
            value: any
                The value to be stored in the new node.

        Returns:

            None
        """
        if self.includes(target):
            node = Node(value)

            if self.head == None:
                self.insert(value)

            else:
                current = self.head
                while current.value is not target:
                    current = current.next
                target = current 
                node.next = target.next
                target.next = node

        else:
            print("This target value doesn't exist.")
            
        self.length += 1


