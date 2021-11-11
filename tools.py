import random

from answer import ALPHABET, get_mean_score  

def selection(chromosomes_list, graded_retain_percent, non_graded_retain_percent):
    # graded_retain_percent = percentage of retained best fitting individuals
    # non_graded_retain_percent = percentage of retained remaining individuals (randomly selected)
    
    # Sort individuals by their fitting score
    s = {c:get_mean_score([c]) for c in chromosomes_list}
    s = dict(sorted(s.items(), key=lambda x:x[1], reverse=True))

    # Select the best individuals
    top = int(len(chromosomes_list)*graded_retain_percent)
    flop = int((len(chromosomes_list) - top)*non_graded_retain_percent)
    best = list(s.keys())[:top]

    # Randomly select other individuals
    rest = random.sample(list(s.keys())[top:], flop)

    return best + rest

def crossover(parent1, parent2):
    # implement the crossover function
    #  * Select half of the parent genetic material
    #  * child = half_parent1 + half_parent2
    #  * Return the new chromosome
    #  * Genes should not be moved
    h = len(parent1) // 2
    return parent1[:h] + parent2[h:]

def _get_letter():
    return random.choice(ALPHABET)
    
def mutation(chrom):
    # TODO: implement the mutation function
    #  * Random gene mutation : a character is replaced
    m_pos = random.randint(0, len(chrom) - 1)
    new_letter = _get_letter()
    while chrom[m_pos] == new_letter:
        new_letter = _get_letter()

    mutant = chrom[:m_pos] + new_letter + chrom[m_pos+1:]
    
    return mutant