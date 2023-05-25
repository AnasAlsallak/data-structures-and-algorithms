from stackAndQueue import Stack

def validate_brackets(string):
    """
    Validates if the brackets in the given string are balanced.

    Args:
        string (str): The string to be validated.

    Returns:
        bool: True if the brackets are balanced, False otherwise.
    """
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in string:
        if char in opening_brackets:
            stack.push(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False  # There is a closing bracket without its matching opening bracket
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False  # There is no matching bwn opening and closing brackets

    return len(stack) == 0  # It will return True if all brackets are balanced out, and False otherwise
