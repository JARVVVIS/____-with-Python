## Genetic Algorithm for finding maxima of function : -x^2+2*x-y^2+4*y

import random


POPULATION_SIZE = 100 ## NUMBER OF INDIVIDUALS IN THE POPULATION
ELITISM_FACTOR = 10   ## %AGE ELITES TO BE PRESERVED
MATING_FACTOR = 100-ELITISM_FACTOR
MATING_PER = int(POPULATION_SIZE/2) 


class Individual(object): ## Individual object

    def __init__(self,chromosome):
        self.chromosome = chromosome 
        self.fitness = self.calc_fitness() ## calculate the fitness of this individual


    def calc_fitness(self):
        '''
        A function to calculate fitness of an Individual
        '''

        x = self.chromosome[0]
        y = self.chromosome[1]
        f = -x**2+2*x-y**2+4*y ## fitness value; what we are trying to maximize
        return f

    @classmethod 
    def create_genome(cls):
        '''
        Function to create a new genome
        '''
        x = (random.uniform(-100,100))
        y = (random.uniform(-100,100))
        return [x,y] ## return the genome

    def mate(self,parent):
        '''
        Function to simulate mating between two parents
        '''
        child_chromosome = []
        for gen1,gen2 in zip(self.chromosome,parent.chromosome):
            prob = random.random() ## to select from where the gene will com

            if prob <= 0.45:
                child_chromosome.append(gen1)
            elif prob <= 0.90:
                child_chromosome.append(gen2)
            else:
                ## do some mutation
                gene = (random.uniform(-100,100)) ## a mutated gene
                child_chromosome.append(gene)

        return Individual(child_chromosome) ## return the child chromosome

def genetic():
    global POPULATION_SIZE
    global MATING_FACTOR
    global MATING_PER

    population = [] ## Initial population
    solved = False  ## to keep track wheter the task has been solved
    generation = 0  ## to keep count of generations passed
    max_val = 5
    ## initialize the population
    for _ in range(POPULATION_SIZE):
        genome = Individual.create_genome() ## create a genmode
        ind = Individual(genome) ## create Individual Object
        population.append(ind) ## append to the population list
    
    while not solved: 
        ## sort the population based on fitness
        population = sorted(population,key=lambda x:x.fitness,reverse=True)
        current_max = population[0] # get the maximum in current generation
        print('Generation : {} \t Maxima : {}'.format(generation,current_max.fitness))
        if max_val-current_max.fitness<=1e-2:
            solved = True # dont solve more
            continue 
        new_gen = []

        elite_num = int((POPULATION_SIZE*ELITISM_FACTOR)/100)
        elite_pop = population[:elite_num] ## Elite performers
        new_gen.extend(elite_pop) ## add elite members

        mate_num = int((POPULATION_SIZE*MATING_FACTOR)/100) ## How many children I want
        for _ in range(mate_num):
            parent_1 = random.choice(population[:MATING_PER])
            parent_2 = random.choice(population[:MATING_PER])

            child = parent_1.mate(parent_2) 
            new_gen.append(child)
        
        population = new_gen
        generation+=1


if __name__ == '__main__':
    genetic()
