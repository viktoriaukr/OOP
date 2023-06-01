"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers.
    
    >>> serial = SerialGenerator(start=100)
    
    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """
    def __init__(self, start):
        "This function initializes a new serial number generator with the given start value and current value."
        self.start = start
        self.current = start

    def __repr__(self):
        return f'<SerialGenerator start={self.start} next={self.current+1}>'

    def generate(self):
        "This function generates the new sequential incrementing number every time the user requests new number."
        num = self.current
        self.current += 1
        return num
    
    def reset(self):
        "This function reset the current serial number generator to the initial value."
        self.current = self.start
        return self.current

