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