import pygame
import Board as b
import Squares as squares
import Globals as g
import MouseEvent as me


def main():
    running = True

    #TODO: DELETE WHEN INTRO_SCREEN HAS BEEN IMPLEMENTED
    g.game_menu = False

    #Draw Pieces outside of loop and only update when need be (e.g. mouse is clicked)
    b.draw()
    squares.draw_pieces()
    

    while running:
        
        for event in g.pygame.event.get():
            if event.type == g.pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                me.handle_click(g.pygame.mouse.get_pos())
        g.pygame.display.flip()
    g.pygame.quit()


if __name__ == "__main__":
    main()
