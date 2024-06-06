import Globals as g

def run_pygame_window():
    running = True

    #menu screen:
    run_menu_screen()
    

    while running:
        for event in g.pygame.event.get():
            if event.type == g.pygame.QUIT:
                running = False
        g.pygame.display.flip()
    g.pygame.quit()

#REQUIRES: g.game_menu = True
#If this is false, the game should be running
def run_menu_screen():
    
    background = g.pygame.Rect(0, 0, g.WINDOW_WIDTH, g.WINDOW_HEIGHT)
    g.pygame.draw.rect(g.screen, "skyblue1", background)

run_pygame_window()