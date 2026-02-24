import pygame
import random

pygame.init()

### ====== Pygame Settings ====== ###
WIDTH, HEIGHT = 800,600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Rock Paper Scissor - Pygame')

font = pygame.font.Font(None, 40)
big_font = pygame.font.Font(None, 60)

WHITE = (255,255,255)
BLACK = (0,0,0)
GRAY = (200,200,200)
BLUE = (100,150,230)
CYAN = (55,139,139)

### ====== Game Function ====== ###
def get_machine_choice():
    machine = random.choice(['Rock','Paper', 'Scissor'])
    return machine

def decide_winner(player, machine):
    if player == machine:
        return 'Draw!'
    elif (player == 'Rock' and machine == 'Scissor') \
    or (player == 'Paper' and machine == 'Rock') \
    or (player == 'Scissor' and machine == 'Paper'):
        return 'You Win!'
    else:
        return 'You lose!'

def draw_button(text, x, y, width, height):
    rect = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, BLUE, rect)
    label = font.render(text, True, WHITE)
    screen.blit(label, (x + 20, y + 15))
    return rect

def draw_text(text, font_obj, color, x, y):
    label = font_obj.render(text, True, color)
    screen.blit(label, (x, y))

### ====== Game Variables ====== ###
player_choice = ""
machine_choice = ""
result = ""

running = True

### ====== Game Loop ====== ###
while running:
    screen.fill(GRAY)

    rock_btn = draw_button('Rock', 100, 350, 150, 60)
    paper_btn = draw_button('Paper', 275, 350, 150, 60)
    scissor_btn = draw_button('Scissor', 450, 350, 150, 60)

    draw_text('Rock Paper Scissor', big_font, BLACK, 150, 50)
    draw_text(f'Your Choice: {player_choice}', font, BLACK, 200, 150)
    draw_text(f'Machine Choice: {machine_choice}', font, BLACK, 200, 200)
    draw_text(result, big_font, BLACK, 230, 260)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = event.pos

            if rock_btn.collidepoint(mouse_pos):
                player = 'Rock'
            elif paper_btn.collidepoint(mouse_pos):
                player = 'Paper'
            elif scissor_btn.collidepoint(mouse_pos):
                player = 'Scissor'
            else:
                continue

            machine_choice = get_machine_choice()
            result = decide_winner(player_choice, machine_choice)

    pygame.display.update()

pygame.quit()
