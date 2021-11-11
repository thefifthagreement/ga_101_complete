import string

ALPHABET = string.ascii_letters + " !'."

KEY = "hGcHWDyYFInCrqNWGvtSfmMUDy!xOoRYjZBpaGAJIpgxMrBMzOfHZA .iJ.q"

def get_mean_score(population):
    global KEY
    
    #  compare each chromosome with the solution (how many character are in the correct position?)
    scores = [sum([a == c for a,c in zip(KEY, chrom)]) / len(KEY) for chrom in population]
    return sum(scores) / len(population)

def is_answer(chrom):
    global KEY
    return chrom == KEY

def answer_len():
    global KEY
    return len(KEY)