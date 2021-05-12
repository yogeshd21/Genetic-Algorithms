import numpy as np
import random
class Solution:
        SZ = 9

        def __init__(self):
            self.genome = np.zeros((self.SZ, self.SZ))

        def fill(self, inArr):
            self.genome = inArr
            # self.genome = inArr.reshape(self.genome.shape)

        def numPresent(self, arr, size):
            result = 0
            for incr in range(size):
                condition = arr == (incr + 1)
                if (np.extract(condition, arr).size > 0):
                    result += 1
            return result

        def getFitness(self):  # fitness of the board - max is 243
            fitness = 0  # first check the rows for each value from 1 to 9
            for row in range(self.SZ):
                checkArray = self.genome[row, :].ravel()
                fitness += self.numPresent(checkArray, self.SZ)
            # now check the columns for each value from 1 to 9
            for cols in range(self.SZ):
                checkArray = self.genome[:, cols].ravel()
                fitness += self.numPresent(checkArray, self.SZ)
            # finally check each 3x3 cell...
            for youter in range(3):
                for xouter in range(3):
                    checkArray = self.genome[youter * 3:youter * 3 + 3, xouter * 3:xouter * 3 + 3].ravel()
                    fitness += self.numPresent(checkArray, self.SZ)
            return fitness

        def crossover(self):
            self.row1 = random.randrange(self.SZ)
            self.row2 = random.randrange(self.SZ)
            self.crsoverpt = random.randrange(8)
            while (self.row1 == self.row2):
                self.row1 = random.randrange(self.SZ)
                self.row2 = random.randrange(self.SZ)
            for i in range(self.crsoverpt, 9):
                self.genome[self.row1, i], self.genome[self.row2, i] = self.genome[self.row2, i], self.genome[self.row1, i]
            return self.genome

        def breeding(self):
            self.row1 = random.randrange(self.SZ)
            self.row2 = random.randrange(self.SZ)
            while (self.row1 == self.row2):
                self.row1 = random.randrange(self.SZ)
                self.row2 = random.randrange(self.SZ)
            self.col = random.sample([0, 1, 2, 3, 4, 5, 6, 7, 8], random.randrange(self.SZ))
            for i in range(len(self.col)):
                self.genome[self.row2, self.col[i]] = self.genome[self.row1, self.col[i]]
            return self.genome

        def mutation(self, mutateProb):
            if (mutateProb > 0.01):
                self.row1 = random.randrange(self.SZ)
                self.switch1 = random.randrange(self.SZ)
                self.switch2 = random.randrange(self.SZ)
                while (self.switch1 == self.switch2):
                    self.switch1 = random.randrange(self.SZ)
                    self.switch2 = random.randrange(self.SZ)
                self.genome[self.row1, self.switch1], self.genome[self.row1, self.switch2] = self.genome[self.row1, self.switch2], self.genome[self.row1, self.switch1]
            return self.genome