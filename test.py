import random
import string
from itertools import combinations_with_replacement
from timeit import timeit
from answer import is_answer, answer_len

ALPHABET = string.ascii_letters + " !'."

def get_letter():
    return random.choice(ALPHABET)

def create_chromosome(size):
    # TODO: Create a chromosome as a string of the right size
    return "".join([get_letter() for _ in range(size)])

KEY = "myFavorite"

def get_score(chrom):
    key = KEY
    # TODO: implement the scoring function
    #  * compare the chromosome with the solution (how many character are in the correct position?)
    return sum([a == c for a,c in zip(key, chrom)]) / len(key)

def selection(chromosomes_list):
    GRADED_RETAIN_PERCENT = 0.3     # percentage of retained best fitting individuals
    NONGRADED_RETAIN_PERCENT = 0.2  # percentage of retained remaining individuals (randomly selected)
    # TODO: implement the selection function
    #  * Sort individuals by their fitting score
    s = {c:get_score(c) for c in chromosomes_list}
    s = dict(sorted(s.items(), key=lambda x:x[1], reverse=True))
    #  * Select the best individuals
    top = int(len(chromosomes_list)*GRADED_RETAIN_PERCENT)
    flop = int((len(chromosomes_list) - top)*NONGRADED_RETAIN_PERCENT)
    best = list(s.keys())[:top]

    #  * Randomly select other individuals
    rest = random.sample(list(s.keys())[top:], flop)
    return best + rest

def crossover(parent1, parent2):
    # TODO: implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    h = len(parent1) // 2
    return parent1[:h] + parent2[h:]

def get_letter():
    return random.choice(ALPHABET)
    
def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    m_pos = random.randint(0, len(chrom) - 1)
    new_letter = get_letter()
    while chrom[m_pos] == new_letter:
        new_letter = get_letter()
        
    return chrom[:m_pos] + get_letter() + chrom[m_pos+1:]

def brut():
    for i, c in enumerate(combinations_with_replacement(ALPHABET, answer_len())):
        if i % 1000000 == 0:
            print(f"iter {i*10**-6}")
        if is_answer("".join(c)):
            break

if __name__ == "__main__":
    timeit("brut()", setup="from __main__ import brut", number=1)
