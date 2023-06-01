import random

class WordFinder:
    """Word Finder: finds random words from a dictionary."""
    def __init__(self, filename):
        words = open(filename)

        self.words = self.file_lines(words)
        words.close()
        
    
    def file_lines(self, words):
        lines = words.readlines()
        word = [line.strip() for line in lines]
        return word
    
    def random(self):
        return random.choice(self.words)
        

class SpecialWordFinder(WordFinder):
    """Special Word Finder: finds random words from a dictionary that doesn't start with '#' and aren't blank."""
    def file_lines(self, words):
        w = []
        for line in words:
            line = line.strip()
            if line and not line.startswith("#"):
                w.append(line)
        return w
    