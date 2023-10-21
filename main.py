from cgitb import grey
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

block_map = {'top_left': None, 'top_middle': None, 'top_right': None,
            'mid_left': None, 'mid_middle': None, 'mid_right': None,
            'bot_left': None, 'bot_middle': None, 'bot_right': None}

class Board:
    def __init__(self):
        self.blocks = block_map.values()
    
    def draw_board(self):
        for block in self.blocks:
            block.draw_block()

class Block:
    def __init__(self, pos):
        self.pos = pos
        self.x = pos_map[pos][0]
        self.y = pos_map[pos][1]
        self.has_x = False
        self.has_o = False
        self.letter = ''
        self.pos = pygame.Vector2(self.x, self.y)
        self.block_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)

    def draw_block(self):
        if (self.x + self.y) % 2 == 0:
            color = 'grey'
        else:
            color = 'black'
        pygame.draw.rect(screen, color, self.block_rect)

        if self.letter:
            self.draw_x()

    def draw_x(self):
        # center = self.block_rect.center
        x_font = pygame.font.Font(None, 25)
        x_surf = x_font.render(self.letter, True, 'white')
        # TODO: center x rect
        x_rect = pygame.Rect(self.x * cell_size + cell_size * 1/3, self.y * cell_size + cell_size * 1/3, cell_size, cell_size)
        screen.blit(x_surf, x_rect)
        self.has_x = True

class X:
    def __init__(self, pos):
        self.x = None
        self.y = None

for key in pos_map.keys():
    block = Block(key)
    block_map[key] = block

board = Board()
current_round = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for key in block_map.keys():
                block = block_map[key]
                if block.block_rect.collidepoint(pos) and not block.letter:
                    if current_round % 2 == 0: block.letter = 'X'
                    else: block.letter = 'O'
                    current_round += 1
            
    board.draw_board()
    pygame.display.update()
    screen.fill('beige')

    clock.tick(60)