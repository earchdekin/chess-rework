import pygame

pygame.init()


WIDTH, HEIGHT = (600, 600)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

selected_piece = None
curr_turn = "W"