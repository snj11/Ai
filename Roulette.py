import random


class Roulette:
    def __init__(self):
        self.fitness_vector = []
        self.cumulative_boundary = []
        self.fractions = []

    def set_fitness_vector(self, fitness_vector):
        self.fitness_vector = fitness_vector
        self.fractions = list()
        totalsum = 0
        current_boundary = 0
        for fitness in fitness_vector:
            totalsum += fitness
        for fitness in fitness_vector:
            current_boundary += fitness/totalsum
            self.cumulative_boundary.append(current_boundary)
            self.fractions.append(fitness / totalsum)
        # print(self.fractions)
        # print(self.cumulative_boundary)

    def spin(self):
        num = random.random()
        index = 0
        while num > self.cumulative_boundary[index]:
            index += 1
        return self.fitness_vector[index]


def rwheel():
    values = input('Enter the data: ').split(",")
    fitness_vector = list()
    for value in values:
        fitness_vector.append(int(value))
    rw = Roulette()
    rw.set_fitness_vector(fitness_vector)
    freq = dict()
    for i in range(100):
        winner = rw.spin()
        if winner not in freq:
            freq[winner] = 0
        old_freq = freq[winner]
        freq[winner] = old_freq+1
    for key in freq:
        print(f"{key} won {freq[key]} times")


rwheel()
