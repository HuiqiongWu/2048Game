'''
1. input: a 4*4 board with 2 numbers, 2, at random plaid
2. user chooses to press 'w', 's', 'a', 'd' to decide the numbers moving to up, down, left, right
3. merge the numbers based on the choice of user: same 2 numbers next to each other at the same line can be added together
4. keep track of the maximum value at each session
5. test for the temination of the game 
'''
import random
import copy
class Game:
    
    def __init__(self):
        self.grid = [[0] * 4 for i in range(4)] # not use [[0]*4]*4, because one value changed will cause the values of the whole column changed 
        self.boardsize = len(self.grid)
        

    def won(self):
        for row in self.grid:
            if 2048 in row:
                return True
        return False

    # the new value generator 
    def pickNewvalue(self):
        if random.randint(1,8)== 1:
            return 4
        else:
            return 2

    
    # get 2 random places for the 2 display numbers
    def initialization(self):
        numneeded = 2
        while numneeded > 0:
            rowNum = random.randint(0, self.boardsize-1)
            colNum = random.randint(0, self.boardsize-1)

            if self.grid[rowNum][colNum] == 0:
                self.grid[rowNum][colNum] = self.pickNewvalue()
                numneeded = numneeded-1

    def random_generator(self):
        rowNum = random.randint(0, self.boardsize-1)
        colNum = random.randint(0, self.boardsize-1)

        while self.grid[rowNum][colNum] != 0:
            rowNum = random.randint(0, self.boardsize-1)
            colNum = random.randint(0, self.boardsize-1)
            
        self.grid[rowNum][colNum] = self.pickNewvalue()

    def mergeRowleft(self, row):
        # test if there is any empty space
        for j in range(self.boardsize-1):
            for i in range(self.boardsize-1, 0, -1):
                if self.grid[row][i-1] == 0:
                    self.grid[row][i-1] = self.grid[row][i]
                    self.grid[row][i] = 0
        # test if there is any current value identical to the next one (merge to left)
        for i in range(self.boardsize-1):
            if self.grid[row][i+1] == self.grid[row][i]:
                self.grid[row][i] *=2
                self.grid[row][i+1] = 0
        # move everything to the left again
        for i in range(self.boardsize-1, 0, -1):
            if self.grid[row][i-1] == 0:
                self.grid[row][i-1] == self.grid[row][i]
                self.grid[row][i] == 0

    def merge_left(self):
        for i in range(self.boardsize):
            self.mergeRowleft(i)

    def mergeRowright(self, row):
        # test if there is any empty space
        for j in range(self.boardsize-1):
            for i in range(0, self.boardsize-1):
                if self.grid[row][i+1] == 0:
                    self.grid[row][i+1] = self.grid[row][i]
                    self.grid[row][i] = 0
        # test if there is any current value identical to the next one (merge to left)
        for i in range(self.boardsize-1):
            if self.grid[row][i-1] == self.grid[row][i]:
                self.grid[row][i] *=2
                self.grid[row][i-1] = 0
        # move everything to the left again
        for i in range(0, self.boardsize-1):
            if self.grid[row][i+1] == 0:
                self.grid[row][i+1] == self.grid[row][i]
                self.grid[row][i] == 0

    def merge_right(self):
        for i in range(self.boardsize):
            self.mergeRowright(i)

    def mergeRowdown(self, col):
        # test if there is any empty space
        for j in range(self.boardsize-1):
            for i in range(0, self.boardsize-1):
                if self.grid[i+1][col] == 0:
                    self.grid[i+1][col] = self.grid[i][col]
                    self.grid[i][col] = 0
        # test if there is any current value identical to the next one (merge to left)
        for i in range(self.boardsize-1):
            if self.grid[i-1][col] == self.grid[i][col]:
                self.grid[i][col] *=2
                self.grid[i-1][col] = 0
        # move everything to the left again
        for i in range(0, self.boardsize-1):
            if self.grid[i+1][col] == 0:
                self.grid[i+1][col]== self.grid[i][col]
                self.grid[i][col] == 0

    def merge_down(self):
        for i in range(self.boardsize):
            self.mergeRowdown(i)

    def mergeRowup(self, col):
        # test if there is any empty space
        for j in range(self.boardsize-1):
            for i in range(self.boardsize-1, 0, -1):
                if self.grid[i-1][col] == 0:
                    self.grid[i-1][col] = self.grid[i][col]
                    self.grid[i][col] = 0
        # test if there is any current value identical to the next one (merge to left)
        for i in range(self.boardsize-1):
            if self.grid[i+1][col] == self.grid[i][col]:
                self.grid[i][col] *=2
                self.grid[i+1][col] = 0
        # move everything to the left again
        for i in range(self.boardsize-1, 0, -1):
            if self.grid[i-1][col] == 0:
                self.grid[i-1][col] == self.grid[i][col]
                self.grid[i][col] == 0

    def merge_up(self):
        for i in range(self.boardsize):
            self.mergeRowup(i)

    # process user input
    def determine_movement(self, move):
        if move == 'w':
            self.merge_up()

        elif move == 's':
            self.merge_down()
        
        elif move == 'a':
            self.merge_left()
        else:
            self.merge_right()

    # test lost
    def no_move(self):
        temp_grid1 = copy.deepcopy(self.grid)
        temp_grid2 = copy.deepcopy(self.grid)

        # test if the temp grid1 if still the same with the temp grid2 
        temp_grid1 = self.merge_down()
        if temp_grid1 == temp_grid2:
            temp_grid1 = self.merge_up()
        if temp_grid1 == temp_grid2:
            temp_grid1 = self.merge_left()
        if temp_grid1 == temp_grid2:
            temp_grid1 = self.merge_right()
        if temp_grid1 == temp_grid2:
            return True
        return False

    








