# the driver class for the movie database.

from Movie import Movie
from EmptyMovie import EmptyMovie
from Person import Person


class MovieDatabaseIterative:
    def __init__(self):
        self._movies_head = EmptyMovie()

    def getMoviesHead(self) -> Movie:
        return self._movies_head


    ##############################################################
    # Add a movie to the database at the end of the list
    # @param title: the title of the movie
    # @param year: the year the movie was released
    # @param director: the director of the movie
    ##############################################################

    def addMovieAtEnd(self, movies_head: Movie, title:str, year:int, director:Person) -> Movie:
        new_movie =  Movie(title, year, director)
        new_movie._next = None

        current_movie = movies_head
        # the end of the list is a node of type EmptyMovie

        #if the head of the
        if isinstance(current_movie, EmptyMovie):
            new_movie._next = movies_head
            movies_head = new_movie
            return movies_head

        while not isinstance(current_movie._next, EmptyMovie):
            current_movie = current_movie._next

        # the current_movie is the last movie in the list
        new_movie._next = current_movie._next # current_movie._next is the EmptyMovie
        current_movie._next = new_movie
        return movies_head

    ##############################################################
    # Add a movie to the database at the beginning of the list
    # @param title: the title of the movie
    # @param year: the year the movie was released
    # @param director: the director of the movie
    ##############################################################
    def addMovieAtBeginning(self, movies_head: Movie, title:str, year:int, director:Person) -> Movie:
        new_movie = Movie(title, year, director)
        new_movie._next = movies_head
        movies_head = new_movie
        return movies_head

    ##############################################################
    # add a movie to the database in sorted order
    # @param title: the title of the movie
    # @param year: the year the movie was released
    # @param director: the director of the movie
    ##############################################################
    def addMovieInOrder(self, movies_head, title:str, year:int, director:Person) -> Movie:
        new_movie = Movie(title, year, director)

        if isinstance(movies_head, EmptyMovie):
            new_movie._next = movies_head
            movies_head = new_movie
            return movies_head


        # if the new movie is less than the first movie in the list
        if new_movie < movies_head:
            new_movie._next = movies_head
            movies_head = new_movie
            return movies_head

        # now we walk down the list and find the correct position for the
        # new movie
        current_movie = movies_head
        while not isinstance(current_movie._next, EmptyMovie)  and current_movie._next < new_movie:
            current_movie = current_movie._next

        new_movie._next = current_movie._next
        current_movie._next = new_movie
        return movies_head

    ##############################################################`
    # return the list of movies by a given director
    # @param director: the director of the movies
    # @return the list of movies by the given director
    ##############################################################
    def getMoviesByDirector(self, director:Person) -> list:
        movies = None
        current_movie = self._movies_head
        while current_movie is not None:
            if current_movie.getDirector() == director:
                new_movie = Movie.Movie(current_movie.getTitle(), current_movie.getYear(), current_movie.getDirector())
                new_movie._next = movies
            current_movie = current_movie._next
        return movies




##############################################################
# the tests for the movie database
##############################################################
import unittest
class TestMovieDatabaseIterative(unittest.TestCase):
    def test_addMovieAtEnd(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieAtEnd(database._movies_head, "The Shawshank Redemption", 1994, Person("Frank", "Darabont"))
        database._movies_head = database.addMovieAtEnd(database.getMoviesHead(), "The Godfather", 1972, Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieAtEnd(database.getMoviesHead(), "The Dark Knight", 2008, Person("Christopher", "Nolan"))
        self.assertEqual("The Shawshank Redemption", database._movies_head._title)
        self.assertEqual("The Godfather", database._movies_head._next._title)
        self.assertEqual("The Dark Knight", database._movies_head._next._next._title)

    def test_addMovieAtBeginning(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(),"The Shawshank Redemption", 1994, Person("Frank", "Darabont"))
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(),"The Godfather", 1972, Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(),"The Dark Knight", 2008, Person("Christopher", "Nolan"))
        self.assertEqual("The Dark Knight", database._movies_head._title)
        self.assertEqual("The Godfather", database._movies_head._next._title)
        self.assertEqual("The Shawshank Redemption", database._movies_head._next._next._title)

    def test_addMovieInOrder(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(),"The Shawshank Redemption", 1994, Person("Frank", "Darabont"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(),"The Godfather", 1972, Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(),"The Dark Knight", 2008, Person("Christopher", "Nolan"))
        self.assertEqual("The Godfather", database._movies_head._title)
        self.assertEqual("The Shawshank Redemption", database._movies_head._next._title)
        self.assertEqual("The Dark Knight", database._movies_head._next._next._title)