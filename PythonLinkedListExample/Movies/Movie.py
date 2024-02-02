# a class to store movie information

#import Person from Person.py
from Person import Person
class Movie:
    def __init__(self, title: str, year: int, director:Person):
        self._title:str = title
        self._year:int = year
        self._director:Person = director
        self._next:Movie = None


    def getTitle(self) -> str:
        return self._title

    def getYear(self) -> int:
        return self._year

    def getDirector(self) -> Person:
        return self._director

    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        if (self._title == other._title
                and self._year == other._year
                and self._director == other._director):
            return True
        return False

    def __lt__(self, other):

        if self._year < other._year:
            return True
        if self._year > other._year:
            return False
        if self._title < other._title:
            return True
        if self._title > other._title:
            return False
        if self._director < other._director:
            return True
        return False

    def __gt__(self, other):
        if self._year > other._year:
            return True
        if self._year < other._year:
            return False
        if self._title > other._title:
            return True
        if self._title < other._title:
            return False
        if self._director > other._director:
            return True
        return False

    ###############################################################
    # implement the __str__ method
    # return String.format(this.title + " (" + this.director.toString() + ", %d)", this.year);
    # the above from the java code is not working in python
    ###############################################################
    def __str__(self):
        return self._title + " (" + str(self._director) + ", " + str(self._year) + ")"


import unittest

########################
# The unit tests for the Movie class


class TestMovie(unittest.TestCase):
    def setUp(self):

        self.billyWild = Person("Billy", "Wilder")
        self.federicoFellini = Person("Federico", "Fellini")
        self.stanleyKubrick = Person("Stanley", "Kubrick")
        self.apartment = Movie("The Apartment", 1960, self.billyWild)

        self.ladolcevita = Movie("La Dolce Vita", 1960, self.federicoFellini)
        self.strangelove = Movie("Dr. Strangelove", 1964, self.stanleyKubrick)


    def test_eq(self):
        self.assertEqual(self.apartment, self.apartment)
        self.assertEqual(self.apartment, Movie("The Apartment", 1960, self.federicoFellini))
        self.assertNotEqual(self.apartment, self.ladolcevita)
        self.assertNotEqual(self.apartment, self.strangelove)

    def test_lt(self):
        self.assertLess(self.ladolcevita, self.apartment)
        self.assertLess(self.apartment, self.strangelove)
        self.assertLess(self.ladolcevita, self.strangelove)

    def test_str(self):
        self.assertEqual("The Apartment (Billy Wilder, 1960)", str(self.apartment))
        self.assertEqual("La Dolce Vita (Federico Fellini, 1960)", str(self.ladolcevita))
        self.assertEqual("Dr. Strangelove (Stanley Kubrick, 1964)", str(self.strangelove))




