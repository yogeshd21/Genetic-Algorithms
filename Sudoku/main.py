# main.py Creed Jones ECE4524 Feb 1 2021
# Based on the Java version from December 27, 2017
# this module tests the SudokuBoard evaluation and then runs the GA solver
import numpy as np
import time
import traceback
import SudokuBoard
import Population
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.\
    print(f'Hi, {name}') # Press Ctrl+F8 to toggle the breakpoint.
def testBoard():
    sampData = np.array( (2, 9, 5, 7, 4, 3, 8, 6, 1,
                          4, 3, 1, 8, 6, 5, 9, 2, 7,
                          8, 7, 6, 1, 9, 2, 5, 4, 3,
                          3, 8, 7, 4, 5, 9, 2, 1, 6,
                          6, 1, 2, 3, 8, 7, 4, 9, 5,
                          5, 4, 9, 2, 1, 6, 7, 3, 8,
                          7, 6, 3, 5, 2, 4, 1, 8, 9,
                          9, 2, 8, 6, 7, 1, 3, 5, 4,
                          1, 5, 4, 9, 3, 8, 6, 7, 2) )
    sampData2 = np.array( (1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9,
                           1, 2, 3, 4, 5, 6, 7, 8, 9) )
    sampData3 = np.array( (1, 2, 3, 4, 5, 6, 7, 8, 9,
                           4, 5, 6, 7, 8, 9, 1, 2, 3,
                           7, 8, 9, 1, 2, 3, 4, 5, 6,
                           2, 3, 4, 5, 6, 7, 8, 9, 1,
                           5, 6, 7, 8, 9, 1, 2, 3, 4,
                           8, 9, 1, 2, 3, 4, 5, 6, 7,
                           3, 4, 5, 6, 7, 8, 9, 1, 2,
                           6, 7, 8, 9, 1, 2, 3, 4, 5,
                           9, 1, 2, 3, 4, 5, 6, 7, 8) )
    sb = SudokuBoard.SudokuBoard()
    sb.fill(sampData)
    aaa = sb.getFitness()
    print("Fitness is: " + str(sb.getFitness()))
    sb.fill(sampData2)
    print("Fitness is: " + str(sb.getFitness()))
    sb.fill(sampData3)
    print("Fitness is: " + str(sb.getFitness()))
def runTests():
    popsize = 100
    elitism = 5
    antielitism = 0
    numtrials = 1
    printEachStep = True
    for trial in range(numtrials):
        pop = Population.Population(popsize, elitism, antielitism)
        pop.initialize()
        print("Population = " + str(popsize) + ", elitism = " + str(elitism) + ", antielitism = " + str(antielitism))
        maxFitness = 0
        lastFitness = 0
        generation = 0
        startTime = time.monotonic()
        lastTime = startTime
        try:
            while (True):
                if (generation >= pop.NUMGENERATIONS):
                    break
                generation += 1
                lastFitness = maxFitness
                #print('in loop')
                maxFitness = pop.newGeneration()
                #print(maxFitness)
                if (printEachStep and ((lastFitness) != maxFitness)):
                    elapsedTime = time.monotonic() - lastTime
                    lastTime = time.monotonic()
                    print("Python; Generation: " + str(generation) + ", Fitness = "
                          + str(maxFitness) + " mutateProb = " + str(pop.mutateProb)
                          + " elapsedTime = " + str(elapsedTime))
                if (maxFitness == pop.PERFECTSCORE):
                    break
                if ((pop.mutateProb < 0.01) and (generation % 1000) == 0):
                    pop.mutateProb *= 1.01
        except:
            print("Exception in user code:")
            print("-" * 60)
            traceback.print_exc()
            print("-" * 60)
    print(pop.toString())
    print("Process finished in " + str(generation) + " generations and " + str(time.monotonic() - startTime) + "seconds.")
if __name__ == '__main__':
    testBoard()
    runTests()