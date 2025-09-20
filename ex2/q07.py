class Person:
    
    def __init__(self, first, last):
        self._first = first
        self._last = last

    @property
    def first(self):
        return self._first
    
    @first.setter
    def first(self, value):
        if not value:
            raise ValueError("First name cannot be empty")
        if len(value) < 2:
            raise ValueError("First name must be at least 2 characters long")
        self._first(value)
    
    @property
    def last(self):
        return self._last
    
    @last.setter
    def last(self, value):
        if not value:
            raise ValueError("Last name cannot be empty")
        if len(value) < 2:
            raise ValueError("Last name must be at least 2 characters long")
        self._last = value