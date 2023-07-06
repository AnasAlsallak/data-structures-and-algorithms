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

# Stretch Goal
# def repeated_word(book: Optional[str], count: int) -> List[str]:
#     """
#     Returns a list of the most frequently used words in the provided book.

#     Args:
#         book: A string representing the book.
#         count: An integer representing the number of most frequent words to return.

#     Returns:
#         A list of the most frequently used words in the book.
#         If the book is not provided (None) or empty, it returns an empty list.
#     """
#     if book is None or book == "":
#         return []

#     words = book.lower().split()
#     word_counts = {}

#     for word in words:
#         word_counts[word] = word_counts.get(word, 0) + 1  # 0 is the default value if the word  doesn't exist

#     sorted_words = sorted(word_counts, key=lambda w: word_counts[w], reverse=True)
#     return sorted_words[:count]









