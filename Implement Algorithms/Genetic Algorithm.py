import random
import numpy as np


# Problem: Maximize the function f(x) = -x^2 + 5x (quadratic optimization problem)

# Define the fitness function
def fitness_function(x):
    # A sample objective function: maximize -x^2 + 5x (can be replaced by your own function)
    return -x ** 2 + 5 * x


# Generate initial population
def generate_population(size, lower_bound, upper_bound):
    return [random.uniform(lower_bound, upper_bound) for _ in range(size)]


# Selection: Roulette Wheel Selection
def selection(population, fitnesses):
    total_fitness = sum(fitnesses)
    probabilities = [f / total_fitness for f in fitnesses]
    selected_index = np.random.choice(len(population), p=probabilities)
    return population[selected_index]


# Crossover: Single-point crossover
def crossover(parent1, parent2):
    # Assuming numerical values for simplicity; blend the two parents
    alpha = random.uniform(0, 1)
    child = alpha * parent1 + (1 - alpha) * parent2
    return child


# Mutation: Randomly alter a solution
def mutate(individual, mutation_rate, lower_bound, upper_bound):
    if random.uniform(0, 1) < mutation_rate:
        mutation_value = random.uniform(-1, 1)
        individual += mutation_value
        # Clip to ensure within bounds
        individual = min(max(individual, lower_bound), upper_bound)
    return individual


# Genetic Algorithm
def genetic_algorithm(fitness_func, generations=50, population_size=20,
                      lower_bound=-10, upper_bound=10, mutation_rate=0.1):
    # Step 1: Initialize population
    population = generate_population(population_size, lower_bound, upper_bound)

    for generation in range(generations):
        # Step 2: Evaluate fitness
        fitnesses = [fitness_func(ind) for ind in population]

        # Step 3: Create a new population
        new_population = []
        for _ in range(population_size):
            # Select parents
            parent1 = selection(population, fitnesses)
            parent2 = selection(population, fitnesses)

            # Perform crossover
            child = crossover(parent1, parent2)

            # Mutate child
            child = mutate(child, mutation_rate, lower_bound, upper_bound)

            new_population.append(child)

        # Update population
        population = new_population

        # Print the best solution for this generation
        best_fitness = max(fitnesses)
        best_solution = population[fitnesses.index(best_fitness)]
        print(f"Generation {generation + 1}: Best Solution = {best_solution:.2f}, Fitness = {best_fitness:.2f}")

    # Final best solution
    final_fitnesses = [fitness_func(ind) for ind in population]
    best_solution = population[final_fitnesses.index(max(final_fitnesses))]
    print("\nOptimal Solution:", best_solution)
    print("Optimal Fitness:", fitness_func(best_solution))


# Run the Genetic Algorithm
if __name__ == "__main__":
    genetic_algorithm(fitness_function, generations=5, population_size=20, lower_bound=0, upper_bound=5)
