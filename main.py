import math
import random

POPULATION_SIZE = 100
CHILDREN_NO = 1
BEAM_WIDTH = 100
EPOCHS = 10


def main():
    population = init_population()
    population = sorted(population, key=lambda x: fitness(x), reverse=True)

    for _ in range(EPOCHS):
        next_gen = []
        for index in range(len(population)):
            v1 = population[index]
            v2 = population[(index + 1) % len(population)]
            children = merge(v1, v2)
            next_gen += children

        population = next_gen
        population = sorted(population, key=lambda x: fitness(x), reverse=True)

    maximum = population[0]
    y = fitness(maximum)

    print(f"Maximum: {maximum}, Fitness: {y}")



def merge(v1, v2):
    diff = abs(v1 - v2)
    minimum = min(v1, v2)
    return [minimum + random.uniform(0, diff) for _ in range(CHILDREN_NO)]


def fitness(x):
    return math.sin(10 * math.pi * x) * x + 1


def init_population():
    return [random.random() for _ in range(POPULATION_SIZE)]


if __name__ == "__main__":
    main()
