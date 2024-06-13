import Globals as g
from Button import CenteredButton
from MouseEvent import handle_click

class Font():
    def __init__(self, name, path):
        self.name = name
        self.file_path = path

intro_font = Font("Coffee_Fills", "fonts/CoffeeFills.ttf")

intro_font = g.pygame.font.Font(intro_font.file_path, 50)

play_button = CenteredButton(g.WIDTH / 2, g.HEIGHT - 200, 100, 50, "deepskyblue4")



def run_pygame_window():
    running = True

    #menu screen:
    run_menu_screen()
    

    while running:
        for event in g.pygame.event.get():
            if event.type == g.pygame.QUIT:
                running = False
            elif event.type == g.pygame.MOUSEBUTTONDOWN:
                handle_click(g.pygame.mouse.get_pos(), buttons=[play_button])
        g.pygame.display.flip()
    g.pygame.quit()

#REQUIRES: g.game_menu = True
#If this is false, the game should be running
def run_menu_screen():
    background = g.pygame.Rect(0, 0, g.WINDOW_WIDTH, g.WINDOW_HEIGHT)
    g.pygame.draw.rect(g.screen, "skyblue1", background)

    
    play_button.draw(g.screen)

    title = intro_font.render("Welcome!", True, "black")
    title_pos = title.get_rect(centerx=g.WIDTH / 2, y=10)
    g.screen.blit(title, title_pos)


run_pygame_window()