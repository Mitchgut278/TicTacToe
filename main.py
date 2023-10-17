import pygame, sys
from pygame import Vector2

pygame.init()

cell_size = 150
cell_number = 3

screen = pygame.display.set_mode((cell_number * cell_size, cell_number * cell_size))
clock = pygame.time.Clock()

test_surf = pygame.Surface((100,200))
test_surf.fill('white')

pos_map = {'top_left': (0,0), 'top_middle': (1,0), 'top_right': (2,0),
           'mid_left': (0,1), 'mid_middle': (1,1), 'mid_right': (2,1),
           'bot_left': (0,2), 'bot_middle': (1,2), 'bot_right': (2,2),}

class Block:
    def __init__(self, pos):
        self.pos = pos
        self.x = pos_map[pos][0]
        self.y = pos_map[pos][1]
        self.pos = pygame.Vector2(self.x, self.y)
        self.block_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)
        pygame.draw.rect(screen, 'grey', self.block_rect)
        self.draw_x()
    
    def draw_x(self):
        center = self.block_rect.center
        x_font = pygame.font.Font(None, 25)
        x_surf = x_font.render('X', True, 'white')
        x_rect = x_surf.get_rect(center = center)
        pygame.draw.rect(screen, 'white', x_rect)

class X:
    def __init__(self, pos):
        self.x = None
        self.y = None


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    screen.fill('beige')
    
    for key in pos_map.keys():
        block = Block(key)
    # screen.blit(test_surf, (50,100))

    clock.tick(60)