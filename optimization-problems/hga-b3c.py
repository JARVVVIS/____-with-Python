## Maximizing function : -x**2+2*x-y**2+4*y

import random


POPULATION_SIZE = 100 ## NUMBER OF INDIVIDUALS
ELITE_FACTOR = 10
MATING_PER = 45 
MATING_FACTOR = 100-ELITE_FACTOR
N_GEN = 100 ## MAX NUMBER OF GENERATIONS
G_GEN = 10  ## Genetic Algo iterations in each generation
B_GEN = 10  ## B3C Algo iteration in each generation

class Individual(object):
    def __init__(self,chromosome):
        self.chromosome = chromosome
        self.fitness = self.calc_fitness() 
    
    def calc_fitness(self):
        '''
        Function to calculate fitness of given chromosome
        '''
        (x,y) = self.chromosome
        f = -x**2+2*x-y**2+4*y
        return f
    
    @classmethod
    def create_genome(cls):
        '''
        Function to Initialize a genome
        '''
        x = random.uniform(-100,100)
        y = random.uniform(-100,100)
        return [x,y]

    def mate(self,parent):
        '''
        Function to simulate mating 
        '''
        child_chromosome = []
        for gen1,gen2 in zip(self.chromosome,parent.chromosome):
            prob = random.random()
            if prob<0.45:
                child_chromosome.append(gen1)
            elif prob<0.90:
                child_chromosome.append(gen2)
            else:
                gene = random.uniform(-100,100)
                child_chromosome.append(gene)
        
        return Individual(child_chromosome)

def genetic(population):

    for _ in range(1,G_GEN+1):
        new_population = []
        elite_num = int((ELITE_FACTOR*POPULATION_SIZE)/100)
        elite_pop = population[:elite_num]
        new_population.extend(elite_pop) ## update the elite members

        mating_s = int((MATING_FACTOR*POPULATION_SIZE)/100)
        for _ in range(1,mating_s+1):
            parent1 = random.choice(population[:MATING_PER])
            parent2 = random.choice(population[:MATING_PER])

            child = parent1.mate(parent2)
            new_population.append(child)

        population = new_population
    return population



def b3c(population,generation):

    for _ in range(1,B_GEN):

        new_population = []
        fitness = [x.fitness for x in population] ## fitness of all individuals
        com_x = population[0].chromosome[0]
        com_y = population[0].chromosome[1]


        ## generate a new population
        for _ in range(POPULATION_SIZE):
            x_new  = com_x + random.normalvariate(0,1/generation)
            y_new  = com_y + random.normalvariate(0,1/generation)
            child = Individual([x_new,y_new])
            new_population.append(child)
        population = new_population
    return population



def main():
    population = [] ## initialize population
    for _ in range(POPULATION_SIZE):
        genome = Individual.create_genome() ## init a genome 
        ind = Individual(genome) 
        population.append(ind)
    for generation in range(1,N_GEN+1):
        population = sorted(population,key=lambda x:x.fitness,reverse=True) ## sort the population
        print('Generation : {} \t Fitness : {}'.format(generation,population[0].fitness))
        population = genetic(population) ## get the genetic algo output
        population = b3c(population,generation) ## get the b3c phase output


if __name__ == '__main__':
    main()