from typing import List

class Movie:
    def __init__(self, title: str, year: int, genres: List[str]):
        self.title = title
        self.year = year
        self.genres = genres

def sort_by_year(movies: List[Movie]) -> List[Movie]:
    """
    Sorts a list of movies by the most recent year first.

    Args:
        movies (List[Movie]): The list of movies to be sorted.

    Returns:
        List[Movie]: The sorted list of movies.
    """
    return insertion_sort(movies, lambda movie: -movie.year)

def sort_alphabetical_ignore_prefix(movies: List[Movie]) -> List[Movie]:
    """
    Sorts a list of movies in alphabetical order while ignoring certain words at the beginning of titles.

    Args:
        movies (List[Movie]): The list of movies to be sorted.

    Returns:
        List[Movie]: The sorted list of movies.
    """
    return insertion_sort(movies, lambda movie: ignore_prefix(movie.title).lower())

def insertion_sort(arr: List[Movie], comparator) -> List[Movie]:
    """
    Performs insertion sort on a list of movies based on a provided comparator.

    Args:
        arr (List[Movie]): The list of movies to be sorted.
        comparator: The comparator function used for determining the order of movies.

    Returns:
        List[Movie]: The sorted list of movies.
    """
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and comparator(arr[j]) > comparator(key):
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr

def ignore_prefix(title: str) -> str:
    """
    Returns the first word of a title after ignoring certain words at the beginning.

    Args:
        title (str): The title of a movie.

    Returns:
        str: The first word of the title after ignoring specified words.
    """
    ignored_words = ["A", "An", "The"]
    words = title.split(" ")
    for word in words:
        if word not in ignored_words:
            return word
    return title

# Comparator functions
def year_comparator(movie: Movie) -> int:
    """
    Comparator function to compare movies based on their year.

    Args:
        movie (Movie): The movie to be compared.

    Returns:
        int: -1 if the movie's year is less than the other movie's year,
             0 if both movies have the same year,
             1 if the movie's year is greater than the other movie's year.
    """
    return movie.year

def title_comparator(movie: Movie) -> str:
    """
    Comparator function to compare movies based on their titles.

    Args:
        movie (Movie): The movie to be compared.

    Returns:
        str: The title of the movie.
    """
    return movie.title

