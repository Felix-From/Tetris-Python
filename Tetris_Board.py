import pygame
import time

class TetrisBoard :
    grid = []
    zeroPoint=[]
    gridSize = []
    
    def __init__(self, width, height, lineheight, gamewidth):
        self.zeroPoint = [gamewidth,lineheight]
        self.gridSize = [gamewidth/width,lineheight]
        grid = []
        for i in range(width):
            temp = []
            for j in range(height):
                temp.append(gridItem(i*self.gridSize[0]+self.zeroPoint[0],
                                     j*self.gridSize[1]+self.zeroPoint[1],
                                     self.gridSize[0],self.gridSize[1]))
            grid.append(temp)
        self.grid = grid
        #print(self.grid)
        
    def draw(self, screen):
        for row in self.grid:
            for cell in row:
                if cell.isActive:
                    pygame.draw.rect(screen, cell.getColor(), cell.getRect())
                    #print(screen,cell.getColor(),cell.getRect())
                    
    def draw_tetromino(self, screen, tetromino):
        for row_index, row in enumerate(tetromino.shape):
            for col_index, cell in enumerate(row):
                if cell:
                    #print(cell)
                    x = tetromino.x + col_index
                    y = tetromino.y + row_index
                    if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[0]):  
                        rect = self.grid[x][y].getRect()
                        pygame.draw.rect(screen, tetromino.color, rect)
                        #print(rect)

    
    
class gridItem:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.isActive = False
        self.isFlashing = False
        self.color = (0,0,0)
        self.Rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
    
    def getRect(self):
        return self.Rect
    
    def getColor(self):
        if not self.isFlashing:
            return self.color
        elif self.color == (100,100,100):
            self.color = (10,10,10)
        else:
            self.color = (100,100,100)
        return self.color
    
    def setActive(self, state):
        self.isActive = state
    
class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]],  # I Hero
        [[1, 1], [1, 1]],  # O Smashboy
        [[0, 1, 0], [1, 1, 1]],  # T Teewee
        [[1, 1, 0], [0, 1, 1]],  # S Rhode Island
        [[0, 1, 1], [1, 1, 0]],  # Z Cleveland
        [[1, 1, 1], [1, 0, 0]],  # L Blue Ricky
        [[1, 1, 1], [0, 0, 1]],  # J Orange Ricky
    ]

    def __init__(self, shape_index, color):
        self.shape = self.SHAPES[shape_index]
        self.color = color
        self.x = 3
        self.y = 0

    def move(self, dx, dy, grid):
        self.x += dx
        self.y += dy
        #print(self.x,self.y,dx,dy)
        if self.check_collision(grid):
            self.x -= dx
            self.y -= dy
            return False
        return True

    
    def check_collision(self, grid):
        for row_index, row in enumerate(self.shape):
            for col_index, cell in enumerate(row):
                if cell:  
                    #print(cell)
                    x = self.x + col_index
                    y = self.y + row_index

                    if x < 0 or x >= len(grid) or y >= len(grid[0]):
                        #print("out of box")
                        return True
                    
                    if y >= 0 and grid[x][y].isActive:
                        #print("collision")
                        return True
        return False
    
    def rotate(self, grid):
        original_shape = self.shape
        
        self.shape = [list(row) for row in zip(*self.shape[::-1])]

        if self.check_collision(grid):
            self.shape = original_shape

    

def lock_tetromino(board, tetromino):
    for row_index, row in enumerate(tetromino.shape):
        for col_index, cell in enumerate(row):
            if cell:
                x = tetromino.x + col_index
                y = tetromino.y + row_index
                if y >= 0:
                    board.grid[x][y].setActive(True)
                    board.grid[x][y].color = tetromino.color

def drop_rows(board, row_to_clear):
    for y in range(row_to_clear, 0, -1): 
        for x in range(len(board.grid)):
            board.grid[x][y].isActive = board.grid[x][y - 1].isActive
            board.grid[x][y].color = board.grid[x][y - 1].color
    for x in range(len(board.grid)):
        board.grid[x][0].isActive = False


def clear_lines(board):
    rows_to_clear = []
    
    for y in range(len(board.grid[0]) - 1, -1, -1):
        if all(cell.isActive for cell in [row[y] for row in board.grid]):
            rows_to_clear.append(y)
    
    if rows_to_clear:
        for row in rows_to_clear:
            drop_rows(board, row)

