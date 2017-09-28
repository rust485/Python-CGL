import sys
from random import randint

class Life:

    def __init__(self, size_x, size_y, alive, dead, preset=None):
        self.alive = alive
        self.dead = dead
        self.size_x = size_x
        self.size_y = size_y
        self.grid = {}
        if preset == None or len(preset) % 2 != 0:
            for x in range(self.size_x):
                for y in range(self.size_y):
                    if randint(0, 1) == 1: self.grid[x, y] = self.alive
                    else: self.grid[x, y] = self.dead
        else:
            for x in range(self.size_x):
                for y in range(self.size_y):
                    self.grid[x, y] = self.dead
            for i in preset:
                x = preset[i]
                y = preset[i + 1]
                self.grid[x, y] = self.alive
                i += 1

    def update(self):
        tempGrid = {}
        for x in range(self.size_x):
            for y in range(self.size_y):
                tempGrid[x, y] = self.grid[x, y];
        for x in range(self.size_x):
            for y in range(self.size_y):
                tempGrid[x, y] = self.alive if self.check(x, y) else self.dead
        for x in range(self.size_x):
            for y in range(self.size_y):
                self.grid[x, y] = tempGrid[x, y]

    # returns true if cell should be alive, false otherwise
    def check(self, x, y):
        if self.grid[x, y] == self.alive:
            if self.numOfNeighbors(x, y) < 2 or self.numOfNeighbors(x, y) > 3:
                return False
            if self.numOfNeighbors(x, y) == 2 or self.numOfNeighbors(x, y) == 3:
                return True
        elif self.numOfNeighbors(x, y) == 3:
            return True
        return False



    def numOfNeighbors(self, targetX, targetY):
        startX = startY = None

        startX = targetX - 1 if targetX > 0 else self.size_x - 1
        startY = targetY - 1 if targetY > 0 else self.size_y - 1

        x = startX
        y = startY

        count = 0
        for countY in range(0, 3):
            for countX in range(0, 3):
                if not (x == targetX and y == targetY) and self.grid[x, y] == self.alive:
                    count += 1
                x += 1
                if x == self.size_x: x = 0
            x = startX
            y += 1
            if y == self.size_y: y = 0

        return count

    def __str__(self):
        ret = ''
        for x in range(self.size_x):
            for y in range(self.size_y):
                ret += str(self.grid[x, y])
            ret += '\n'

        return ret
