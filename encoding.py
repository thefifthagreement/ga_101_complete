import random

from answer import ALPHABET

def get_letter():
    return random.choice(ALPHABET)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    return "".join([get_letter() for _ in range(size)])