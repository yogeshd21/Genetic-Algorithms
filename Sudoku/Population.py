import numpy as np
import random
import Solution
class Population:
    SZ = 9
    sol = Solution.Solution()

    def __init__(self, popsize, elitism, antielitism):
        self.NUMGENERATIONS = 100000000
        self.PERFECTSCORE = 243
        self.mutateProb = 0.001
        self.popsize = popsize
        self.elitism = elitism
        self.antielitism = antielitism
        self.maxfit = []
        self.elitepop = np.zeros((self.elitism, self.SZ, self.SZ))
        self.elitepopindex = []
        self.antielitepop = np.zeros((self.antielitism, self.SZ, self.SZ))
        self.antielitepopindex = []
        self.yofit = []
        self.docrossover = True          #switch between crossover and breeding

    def toString(self):
        res = ""
        for yinc in range(self.SZ):
            if ((yinc == 3) or (yinc == 6)):
                res = res + "------------------------\n\r"
            for xinc in range(self.SZ):
                if ((xinc == 3) or (xinc == 6)):
                    res = res + " | "
                res = res + str(self.sol.genome[yinc][xinc]) + " "
            res += "\n\r"
        return res

    def initialize(self):
        self.population = np.zeros((self.popsize, self.SZ, self.SZ))
        for i in range(self.SZ):
            for j in range(self.popsize):
                self.population[j, :, i] = random.sample([1, 2, 3, 4, 5, 6, 7, 8, 9], self.SZ)

    def newGeneration(self):
        fitpop = []
        fit = []
        for i in range(self.popsize):
            inArr = self.population[i]
            self.sol.fill(inArr)
            fitpop.append(self.sol.getFitness())

        fitindex = np.argsort(fitpop)
        breedsort = np.sort(fitpop)[(self.antielitism):] #variable for fitness without elitefitness and antielitefitness
        if self.elitism > 0:
            self.elitepopindex = fitindex[-(self.elitism):]
            for i in range(len(self.elitepopindex)):
                self.elitepop[i] = self.population[self.elitepopindex[i]]
            breedsort = np.sort(fitpop)[(self.antielitism):-(self.elitism)]
        if self.antielitism > 0:
            self.antielitepopindex = fitindex[:self.antielitism]
            for i in range(len(self.antielitepopindex)):
                self.antielitepop[i] = self.population[self.antielitepopindex[i]]

        for i in range(len(breedsort)):
            fit.append(breedsort[i] / (np.sum(breedsort)))
        chs = np.random.choice(breedsort, 1, p = fit)  #random choosing but based on fitness probablity
        for i in range(self.popsize):
            inArr = self.population[i]
            self.sol.fill(inArr)
            idfit = self.sol.getFitness()
            if idfit == chs:
                id = i
                break
        inArr = self.population[id]
        self.sol.fill(inArr)
        if self.docrossover == True:
            self.sol.crossover()            #for crossover
        else:
            self.sol.breeding()             #for breeding
        self.sol.mutation(self.mutateProb)  #for mutation

        return (fitpop[fitindex[-1]])