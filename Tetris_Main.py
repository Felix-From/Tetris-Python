import pygame
from pygame import mixer
from Tetris_Board import TetrisBoard as TB
from Tetris_Board import Tetromino
import Tetris_Board as T
import MyRandom


size_x = 150*3
size_y = 15*22

colors = [
    (173, 216, 230),  # Hellblau
    (255, 255, 0),    # Gelb
    (238, 130, 238),  # Lila
    (0, 128, 0),      # Grün
    (255, 140, 0),    # Dunkel-Orange
    (0, 0, 139),      # Dunkel-Blau
    (255, 165, 0)     # Orange
]


linesheight = int(size_y / 22)
gamewidth = (size_x/3)

def main():
    global size_x, size_y, linesheight, gamewidth
    pygame.init()
    pygame.display.set_caption("Tetris")
    mixer.init()
    mixer.music.load("Tetris.mp3")
    mixer.music.set_volume(0.3)
    mixer.music.play()
    screen = pygame.display.set_mode((size_x, size_y))
    clock = pygame.time.Clock()
    isRunning = True

    board = TB(10, 20, linesheight, gamewidth)
    pieceNr = MyRandom.RandomRange(0,6)
    current_tetromino = Tetromino(pieceNr, colors[pieceNr])

    fall_time = 0
    fall_speed = 500
    
    pause = False
    
    pygame.font.init()
    font = pygame.font.SysFont('Comic Sans MS', 30)
    text = font.render("",False,(0,0,0))

    while isRunning:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                isRunning = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    current_tetromino.rotate(board.grid)
                elif event.key == pygame.K_p:
                    pause = not pause
                    if pause:
                        text = font.render("Pause! - 'P' Drücken!",False,(255,0,0))
                        screen.blit(text, (size_x/3,size_y/2))
                        pygame.display.flip()
                    else:
                        text = font.render("",False,(0,0,0))
                        screen.blit(text, (size_x/3,size_y/2))
        
        if not pause:
                        
            dt = clock.tick(30)
            fall_time += dt
            
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                current_tetromino.move(-1, 0, board.grid)
            if keys[pygame.K_RIGHT]:
                current_tetromino.move(1, 0, board.grid)
            if keys[pygame.K_DOWN]:
                current_tetromino.move(0, 1, board.grid)
            
            if fall_time >= fall_speed:
                if not current_tetromino.move(0, 1, board.grid):
                    T.lock_tetromino(board, current_tetromino)
                    if board.grid[3][0].isActive:
                        text = font.render("Game Over!",False,(255,0,0))
                        mixer.music.load("GameOver.mp3")
                        mixer.music.set_volume(1)
                        mixer.music.play()
                        screen.blit(text, (size_x/3,size_y/2))
                        pygame.display.flip()
                        pygame.time.wait(10000)
                        isRunning = False
                    for i in range(4):
                        T.clear_lines(board)
                    pieceNr = MyRandom.RandomRange(0,6)
                    current_tetromino = Tetromino(pieceNr, colors[pieceNr])
                fall_time = 0
            
            screen.fill("black")
            
            borders = []
            borders.append(pygame.rect.Rect(0,0,size_x,linesheight))
            borders.append(pygame.rect.Rect(0,size_y-linesheight,size_x,size_y))
            borders.append(pygame.rect.Rect(0,0,gamewidth,size_y))
            borders.append(pygame.rect.Rect(gamewidth*2,0,size_x,size_y))
            
            #Draw Borders
            for border in borders:
                pygame.draw.rect(screen,(123,123,123),border)
            
                
            board.draw(screen)
            board.draw_tetromino(screen, current_tetromino)
            
            pygame.display.flip()
    
    pygame.quit()

if __name__ == "__main__":
    main()
