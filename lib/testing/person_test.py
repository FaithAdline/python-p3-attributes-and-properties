import io
import sys
from person import Person  # Make sure to import the Person class from your implementation

class TestPerson:
    def test_is_class(self):
        '''is a class with the name "Person".'''
        guido = Person(name='Guido', job='Sales')
        assert isinstance(guido, Person)

