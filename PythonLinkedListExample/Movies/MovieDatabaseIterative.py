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

    def addMovieAtEnd(self, movies_head: Movie, title: str, year: int, director: Person) -> Movie:
        new_movie = Movie(title, year, director)
        new_movie._next = None

        current_movie = movies_head
        # the end of the list is a node of type EmptyMovie

        # if the head of the
        if isinstance(current_movie, EmptyMovie):
            new_movie._next = movies_head
            movies_head = new_movie
            return movies_head

        while not isinstance(current_movie._next, EmptyMovie):
            current_movie = current_movie._next

        # the current_movie is the last movie in the list
        new_movie._next = current_movie._next  # current_movie._next is the EmptyMovie
        current_movie._next = new_movie
        return movies_head

    ##############################################################
    # Add a movie to the database at the beginning of the list
    # @param title: the title of the movie
    # @param year: the year the movie was released
    # @param director: the director of the movie
    ##############################################################
    def addMovieAtBeginning(self, movies_head: Movie, title: str, year: int, director: Person) -> Movie:
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
    def addMovieInOrder(self, movies_head, title: str, year: int, director: Person) -> Movie:
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
        while not isinstance(current_movie._next, EmptyMovie) and current_movie._next < new_movie:
            current_movie = current_movie._next

        new_movie._next = current_movie._next
        current_movie._next = new_movie
        return movies_head

    # #############################################################`
    # return the list of movies by a given director
    # @param director: the director of the movies
    # @return the list of movies by the given director
    # #############################################################
    def getMoviesByDirector(self, director: Person) -> Movie:
        movies = EmptyMovie()
        current_movie = self._movies_head
        while not isinstance(current_movie, EmptyMovie):
            if current_movie.get_director() == director:
                movies = self.addMovieAtEnd(movies, current_movie.get_title(), current_movie.get_year(),
                                            current_movie.get_director())
            current_movie = current_movie._next
        return movies

    ##############################################################
    # Count the number of movies in a list
    # @param movies_head: the head of the list of movies
    # @return the number of movies in the list
    ##############################################################
    def count(self, movies_head: Movie) -> int:
        return movies_head.count()


##############################################################
# the tests for the movie database
##############################################################
import unittest


class TestMovieDatabaseIterative(unittest.TestCase):
    def test_addMovieAtEnd(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieAtEnd(database._movies_head, "The Shawshank Redemption", 1994,
                                                       Person("Frank", "Darabont"))
        database._movies_head = database.addMovieAtEnd(database.getMoviesHead(), "The Godfather", 1972,
                                                       Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieAtEnd(database.getMoviesHead(), "The Dark Knight", 2008,
                                                       Person("Christopher", "Nolan"))
        self.assertEqual("The Shawshank Redemption", database._movies_head._title)
        self.assertEqual("The Godfather", database._movies_head._next._title)
        self.assertEqual("The Dark Knight", database._movies_head._next._next._title)

    def test_addMovieAtBeginning(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(), "The Shawshank Redemption", 1994,
                                                             Person("Frank", "Darabont"))
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(), "The Godfather", 1972,
                                                             Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieAtBeginning(database.getMoviesHead(), "The Dark Knight", 2008,
                                                             Person("Christopher", "Nolan"))
        self.assertEqual("The Dark Knight", database._movies_head._title)
        self.assertEqual("The Godfather", database._movies_head._next._title)
        self.assertEqual("The Shawshank Redemption", database._movies_head._next._next._title)

    def test_addMovieInOrder(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Shawshank Redemption", 1994,
                                                         Person("Frank", "Darabont"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather", 1972,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Dark Knight", 2008,
                                                         Person("Christopher", "Nolan"))
        self.assertEqual("The Godfather", database._movies_head._title)
        self.assertEqual("The Shawshank Redemption", database._movies_head._next._title)
        self.assertEqual("The Dark Knight", database._movies_head._next._next._title)

    def test_getMoviesByDirector(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Shawshank Redemption", 1994,
                                                         Person("Frank", "Darabont"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather", 1972,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather Part II", 1974,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather Part III", 1990,
                                                         Person("Francis", "Ford Coppola"))

        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Dark Knight", 2008,
                                                         Person("Christopher", "Nolan"))
        movies = database.getMoviesByDirector(Person("Frank", "Darabont"))
        self.assertEqual("The Shawshank Redemption", movies.get_title())

        movies = database.getMoviesByDirector(Person("Francis", "Ford Coppola"))
        self.assertEqual("The Godfather", movies.get_title())
        self.assertEqual("The Godfather Part II", movies._next.get_title())

        movies = database.getMoviesByDirector(Person("Christopher", "Nolan"))
        self.assertEqual("The Dark Knight", movies.get_title())

    def test_count(self):
        database = MovieDatabaseIterative()
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Shawshank Redemption", 1994,
                                                         Person("Frank", "Darabont"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather", 1972,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather Part II", 1974,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Godfather Part III", 1990,
                                                         Person("Francis", "Ford Coppola"))
        database._movies_head = database.addMovieInOrder(database.getMoviesHead(), "The Dark Knight", 2008,
                                                         Person("Christopher", "Nolan"))
        self.assertEqual(5, database.count(database.getMoviesHead()))
