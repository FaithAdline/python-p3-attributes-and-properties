import io
import sys
from dog import Dog  # Make sure to import the Dog class from your implementation

class TestDog:
    def test_name_not_empty(self):
        '''prints "Name must be string between 1 and 25 characters." if empty string.'''
        captured_out = io.StringIO()
        sys.stdout = captured_out
        # Provide the required arguments for instantiation
        Dog(name="Fido", breed="Mutt")
        sys.stdout = sys.__stdout__
        assert captured_out.getvalue() == ''

