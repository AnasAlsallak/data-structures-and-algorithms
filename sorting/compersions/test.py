import pytest
from typing import List
from compersions import Movie, sort_by_year, sort_alphabetical_ignore_prefix

def test_sort_by_year():
    movie1 = Movie("Movie 1", 2022, [])
    movie2 = Movie("Movie 2", 2021, [])
    movie3 = Movie("Movie 3", 2023, [])
    movies = [movie1, movie2, movie3]
    sorted_movies = sort_by_year(movies)
    assert sorted_movies == [movie3, movie1, movie2]

def test_sort_alphabetical_ignore_prefix():
    movie1 = Movie("The Movie", 2022, [])
    movie2 = Movie("An Awesome Movie", 2021, [])
    movie3 = Movie("Movie", 2023, [])
    movies = [movie1, movie2, movie3]
    sorted_movies = sort_alphabetical_ignore_prefix(movies)
    assert sorted_movies == [movie2, movie1, movie3]
