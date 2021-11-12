import random
import sys

from answer import answer_len, is_answer, get_mean_score
from encoding import create_chromosome
from tools import selection, crossover, mutation


def create_population(pop_size, chrom_size):
    # create the base population
    return [create_chromosome(chrom_size) for _ in range(pop_size)]


def generation(population, graded_retain_percent=0.3, non_graded_retain_percent=0.2, mutate=True):
    
    # selection
    # use the selection(population) function created on exercise 2
    select = selection(population, graded_retain_percent, non_graded_retain_percent)
    
    # reproduction
    # As long as we need individuals in the new population, fill it with children
    children = []
    # completion to len(population)
    child_nb = len(population) - len(select)
    while len(children) < child_nb:
        # crossover
        parents = random.sample(select, k=2) # randomly selected

        # use the crossover(parent1, parent2) function created on exercise 2
        child = crossover(parents[0], parents[1])
        
        # mutation
        # use the mutation(child) function created on exercise 2
        if mutate:
            child = mutation(child)
        children.append(child)
    
    # return the new generation
    return select + children


def algorithm(args):
    chrom_size = answer_len()
    population_size = 50
    max_iter = 1500
    iteration = 0
    max_score = 0.0

    graded_retain_percent = float(args[0])
    non_graded_retain_percent = float(args[1])
    mutate = int(args[2]) == 1

    # create the base population
    population = create_population(population_size, chrom_size)
    
    answers = []
    
    # while a solution has not been found :
    while not answers and iteration < max_iter:
        iteration += 1

        # create the next generation using the generation(population) function
        population = generation(population, graded_retain_percent, non_graded_retain_percent, mutate)
        
        # display the average score of the population
        score = get_mean_score(population)
        max_score = max(max_score, score)

        if iteration % 50 == 0:
            print(f'generation {iteration}: {score:.2%}')
    
        # check if a solution has been found
        for chrom in population:
            if is_answer(chrom):
                answers.append(chrom)
    
    # print the solution
    if answers:
        print(f"Well done the answer was found (generation: {iteration}, {max_score:.2%}): \n{answers[0]}")
    else:
        print(f"no solution found... (best score {max_score:.2%})")


if __name__ == "__main__":
    algorithm(sys.argv[1:])
    
