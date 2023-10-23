import pygame, sys

pygame.init()
game_active = True
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
        self.winner = None

    def draw_board(self):
        for block in self.blocks:
            block.draw_block()

    def check_win(self):
        board = [0,0,0,0,0,0,0,0,0]
        for i, block in enumerate(self.blocks):
            board[i] = block.letter
        
        winning_combinations = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal lines
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical lines
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for combo in winning_combinations:
            if board[combo[0]] == board[combo[1]] == board[combo[2]] and board[combo[0]] != 0:
                return board[combo[0]]  # Return the winning player's value (X or O, for example)
        
        if 0 not in board:
            return 'Draw!'
        
        return None

    def clear_board(self):
        for block in self.blocks:
            block.letter = 0

class Block:
    def __init__(self, pos):
        self.pos = pos
        self.x = pos_map[pos][0]
        self.y = pos_map[pos][1]
        self.has_x = False
        self.has_o = False
        self.letter = 0
        self.pos = pygame.Vector2(self.x, self.y)
        self.block_rect = pygame.Rect(self.pos.x * cell_size, self.pos.y * cell_size, cell_size, cell_size)

    def draw_block(self):
        if (self.x + self.y) % 2 == 0:
            color = 'grey'
        else:
            color = 'black'
        pygame.draw.rect(screen, color, self.block_rect)

        if self.letter:
            self.draw_letter()

    def draw_letter(self):
        center = self.block_rect.center
        letter_font = pygame.font.Font(None, 25)
        letter_surf = letter_font.render(self.letter, True, 'white')
        letter_rect = letter_surf.get_rect(center=center)
        screen.blit(letter_surf, letter_rect)
        self.has_x = True

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
        
        if game_active and event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            pos = pygame.mouse.get_pos()
            for key in block_map.keys():
                block = block_map[key]
                if block.block_rect.collidepoint(pos) and not block.letter:
                    if current_round % 2 == 0: block.letter = 'X'
                    else: block.letter = 'O'
                    current_round += 1
                    result = board.check_win()
                    
                    if result:
                        game_active = False 

        if game_active:
            board.draw_board()
            pygame.display.update()

    
        else:
            screen.fill('beige')
            end_screen_font = pygame.font.Font(None, 25)
            if result != 'draw':
                result_message = end_screen_font.render(f'{result} Wins!', False, (111,196,169))
            else:
                result_message = end_screen_font.render(result, False, (111,196,169))
            result_message_rect = result_message.get_rect(center=(225, 175))

            end_game_message = end_screen_font.render('Press any button to Play Again!', False, (111,196,169))
            end_game_message_rect = end_game_message.get_rect(center=(225, 250))    

            screen.blit(result_message, result_message_rect)
            screen.blit(end_game_message, end_game_message_rect)
            pygame.display.update()

            # restart game on button click
            if event.type == pygame.KEYDOWN:
                game_active = True
                board.clear_board()
                current_round = 0
    

    clock.tick(60)