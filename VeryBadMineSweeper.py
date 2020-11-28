from random import randint
from numpy import array

class game:
    def __init__(self):
        self.op = [0, 0, 0, 0, 9]
        self.player = input("Qual seu nome? ")
        self.matrix = array([[self.op[randint(0, 4)] for _ in range(9)] for _ in range(9)])
        self.playerView = array([["-" for _ in range(9)] for _ in range(9)])
        self.CreateAdj()

    def CreateAdj(self):
        for r, row in enumerate(self.matrix):
            for c, col in enumerate(row):
                if col == 9: continue
                else:
                    for i in range(-1, 2):
                        if  r + i >= 0 and r + i < 9:
                            for j in range(-1, 2):
                                if  c + j >= 0 and c + j < 9:
                                    if self.matrix[r+i][c+j] == 9: self.matrix[r][c] += 1

    def SearchZeros(self, x, y):
        #BFS
        from collections import deque
        mem = {}
        queue = deque()
        queue.appendleft((x, y))
        while queue:
            current = queue.popleft()
            if self.matrix[current[0]][current[1]] >= 0 and self.matrix[current[0]][current[1]] < 9: 
                self.playerView[current[0]][current[1]] = str(self.matrix[current[0]][current[1]])
            if self.matrix[current[0]][current[1]] >= 1: continue
            for i in range(-1, 2):
                if current[0] + i >= 0 and current[0] + i < 9:
                    for j in range(-1, 2):
                        if current[1] + j >= 0 and current[1] + j < 9:
                            if (current[0]+i, current[1]+j) not in mem:
                                queue.appendleft((current[0]+i, current[1]+j))
                                mem[(current[0]+i, current[1]+j)] = None

    def StartGame(self):
        x, y = randint(0, 8), randint(0, 8)
        while (1):
            if self.matrix[x][y] == 9:
                self.playerView[x][y] = "*"
                for row in self.playerView:
                    print(row) 
                print("GAME OVAH!!!")
                break
            elif self.matrix[x][y] == 0: 
                self.SearchZeros(x, y)
            else:
                self.playerView[x][y] = str(self.matrix[x][y])
            for row in self.playerView:
                print(row)
            x, y = input("Posição do toque: ").split(" ")
            x, y = int(x), int(y)
            
                

test = game()
test.StartGame()


            