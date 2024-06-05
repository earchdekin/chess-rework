import pygame

pygame.init()


#Offset needed in combination with WIDTH & HEIGHT during chess game for board to be centered
WIDTH, HEIGHT = (600, 600)

#W_WIDTH, W_HEIGHT 600, 600 temporarily, to be changed
#TODO: Change this width and height to user screen size
WINDOW_WIDTH, WINDOW_HEIGHT = (600, 600)

#THIS OFFSET ASSUMES WINDOW WIDTH AND HEIGHT ARE BOTH > 600
GAME_X_OFFSET, GAME_Y_OFFSET = ((WINDOW_WIDTH / 2) - (WIDTH / 2), (WINDOW_HEIGHT / 2) - (HEIGHT / 2))

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

selected_piece = None
curr_turn = "W"

game_menu = True