from hash.hash_table import HashTable
from typing import Optional

hashtable = HashTable()

def repeated_word(book: Optional[str]) -> str:
    """
    Finds the first repeated word in a given book.

    Args:
        book: A string representing the book.

    Returns:
        The first repeated word found in the book, or "No repeated word found."
        if no repeated word is found. If the book is not provided (None), it
        returns "No book provided."
    """
    if book is None or book == "":
        return "No book provided."

    words = book.lower().split()

    for word in words:
        if hashtable.has(word):
            return word
        hashtable.set(word, True)

    return "No repeated word found."
    

if __name__ == "__main__":

    print("Once upon a time there was a man :",repeated_word("Once upon a time there was a man"))
    hashtable.__str__()








