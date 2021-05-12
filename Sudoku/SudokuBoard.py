# SudokuBoard Creed Jones ECE4524 Feb 1 2021
# Based on the Java version from December 27, 2017
# this class represents a single Sudoku Board
import numpy as np
class SudokuBoard:
    SZ = 9 # all boards are 3 by 3

    def __init__(self):
        self.cells = np.zeros((self.SZ, self.SZ))

    def toString(self):
        res = ""
        for yinc in range(self.SZ):
            if ( (yinc == 3) or (yinc == 6) ):
                res = res + "------------------------\n\r"
            for xinc in range(self.SZ):
                if ( (xinc == 3) or (xinc == 6) ):
                    res = res + " | "
                res = res + str(self.cells[yinc][xinc]) + " "
            res += "\n\r"
        return res

    def fill(self, inArr):
        self.cells = inArr.reshape(self.cells.shape)

    def numPresent(self, arr, size):
        result = 0
        for incr in range(size):
            condition = arr==(incr+1)
            if (np.extract(condition, arr).size > 0):
                result += 1
        return result

    def getFitness(self): # fitness of the board - max is 243
        fitness = 0 # first check the rows for each value from 1 to 9
        for row in range(self.SZ):
            checkArray = self.cells[row, :].ravel()
            fitness += self.numPresent(checkArray, self.SZ)
        # now check the columns for each value from 1 to 9
        for cols in range(self.SZ):
            checkArray = self.cells[:, cols].ravel()
            fitness += self.numPresent(checkArray, self.SZ)
        # finally check each 3x3 cell...
        for youter in range(3):
            for xouter in range(3):
                checkArray = self.cells[youter*3:youter*3+3, xouter*3:xouter*3+3].ravel()
                fitness += self.numPresent(checkArray, self.SZ)
        return fitness