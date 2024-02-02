## class that represents a person
class Person:
    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name

    def __str__(self):
        return self._first_name + " " + self._last_name


# override the compare method


    def __eq__(self, other):
        # check if the other object is a Person
        if not isinstance(other, Person):
            return False
        if (self._first_name == other._first_name
                and self._last_name == other._last_name):
            return True
        return False

    def __lt__(self, other):
        if self._last_name < other._last_name:
            return True
        elif self._last_name == other._last_name:
            if self._first_name < other._first_name:
                return True
        return False

    def __gt__(self, other):
        if self._last_name > other._last_name:
            return True
        elif self._last_name == other._last_name:
            if self._first_name > other._first_name:
                return True
        return False


##################################################################
# The unit tests for the Person class
##################################################################
import unittest
class TestPerson(unittest.TestCase):

    def setUp(self):
        pass


    def test_init(self):
        p = Person("John", "Doe")
        self.assertEqual("John", p._first_name)
        self.assertEqual("Doe", p._last_name)


    def test_str(self):
        p = Person("John", "Doe")
        self.assertEqual("John Doe", str(p))

    def test_eq(self):
        p1 = Person("John", "Doe")
        p2 = Person("John", "Doe")
        p3 = Person("Jane", "Doe")
        self.assertTrue(p1 == p2)
        self.assertFalse(p1 == p3)

    def test_lt(self):
        p1 = Person("John", "Doe")
        p2 = Person("Jane", "Doe")
        p3 = Person("John", "Smith")
        self.assertTrue(p2 < p1) # Jane < John
        self.assertTrue(p1 < p3) # Doe < Smith
        self.assertTrue(p2 < p3) # Doe < Smith

    def test_gt(self):
        p1 = Person("John", "Doe")
        p2 = Person("Jane", "Doe")
        p3 = Person("John", "Smith")
        self.assertTrue(p1 > p2) # John > Jane
        self.assertTrue(p3 > p1) # Smith > Doe
        self.assertTrue(p3 > p2) # Smith > Doe