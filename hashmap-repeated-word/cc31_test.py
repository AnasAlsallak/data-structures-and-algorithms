import pytest
from hashmap_repeated_word import repeated_word

def test_repeated_word_exists():
    # Happy path: Repeated word exists in the book
    book = "Once upon a time, there was a brave princess who..."
    expected = "a"
    assert repeated_word(book) == expected

def test_repeated_word_exists_case_insensitive():
    # Happy path: Repeated word exists in the book with different cases
    book = "The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog."
    expected = "the"
    assert repeated_word(book) == expected

def test_no_repeated_word():
    # Edge case: No repeated word in the book
    book = "This book is with no repeated word."
    expected = "No repeated word found."
    assert repeated_word(book) == expected

def test_empty_book():
    # Edge case: Empty book string
    book = ""
    expected = "No book provided."
    assert repeated_word(book) == expected

def test_single_word():
    # Edge case: Book with a single word
    book = "Hello"
    expected = "No repeated word found."
    assert repeated_word(book) == expected

def test_repeated_word_at_beginning():
    # Edge case: Book with a repeated word at the beginning
    book = "Apple banana cherry apple"
    expected = "apple"
    assert repeated_word(book) == expected

def test_repeated_word_at_end():
    # Edge case: Book with a repeated word at the end
    book = "cat dog elephant elephant"
    expected = "elephant"
    assert repeated_word(book) == expected

def test_book_argument_none():
    # Expected error: book argument is None
    assert repeated_word(None) == "No book provided."