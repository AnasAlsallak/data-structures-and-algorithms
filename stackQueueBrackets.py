from stackAndQueue import Stack

def validate_brackets(string):
    stack = Stack()
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    
    for char in string:
        if char in opening_brackets:
            stack.append(char)
        elif char in closing_brackets:
            if len(stack) == 0:
                return False  # There is a closing bracket without a matching opening bracket
            opening_bracket = stack.pop()
            if opening_brackets.index(opening_bracket) != closing_brackets.index(char):
                return False  # Opening and closing brackets do not match
        
    return len(stack) == 0  # Return True if all brackets are balanced, False otherwise
