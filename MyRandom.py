import time
import math
import pygame

pygame.init()

previous_seed = None

def RandomRange(min, max):
    global previous_seed
    
    if previous_seed is None:
        previous_seed = int(time.time() * math.pi+pygame.mouse.get_pos()[0]*1000) % (max - min + 1)
    else:
        previous_seed = (previous_seed * (31*previous_seed) + int(time.time() *math.pi+pygame.mouse.get_pos()[0] * 1000)) % (max - min + 1)
    
    return previous_seed + min

def RandomSelect(array):
    return array[RandomRange(0, len(array) - 1)]
