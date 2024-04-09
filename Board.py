#WORKS WITH MAIN.PY IN UBC_REWORK
import Globals as g

#Responsible for drawing the background of the board on screen

#board size in squares
BOARD_SIZE_X, BOARD_SIZE_Y = (8, 8)
TOTAL_SQUARES = 64

#square size in pixels
square_size_x, square_size_y = (int(g.WIDTH / BOARD_SIZE_X), int(g.HEIGHT / BOARD_SIZE_Y))


#Draws board of chess game in checkered black and white pattern (all squares on the board)
def draw():
    g.screen.fill("white")

    x = 0
    y = 0
    while y < BOARD_SIZE_Y:
        left_corner = ((g.WIDTH / BOARD_SIZE_X) * x)
        squares = g.pygame.Rect(left_corner, square_size_y * y, square_size_x, square_size_y)
        x_is_even, y_is_even = (x % 2, y % 2)

        if y_is_even == 0 and x_is_even != 0:
            g.pygame.draw.rect(g.screen, "black", squares)
        elif y_is_even != 0 and x_is_even == 0:
            g.pygame.draw.rect(g.screen, "black", squares)
        x += 1
        if x >= 8:
            y += 1
            x = 0

#REQUIRES: pos to be tuple and draws single square on board
#Used to update a single square (typically drawn first before drawing a piece)
def draw_single_square(pos):
    sqX = pos[0]
    sqY = pos[1]

    draw_black = True

    left_corner = int(square_size_x * sqX)
    square = g.pygame.Rect(left_corner, int(square_size_y * sqY), square_size_x, square_size_y)

    if sqY % 2 == 0: #if y is even,
        if sqX % 2 == 0:
            #white
            draw_black = False
        else:
            #black
            draw_black = True
    else:
        if sqX % 2 == 0:
            #black
            draw_black = True
        else:
            #white
            draw_black = False

    if draw_black == True:
        g.pygame.draw.rect(g.screen, "black", square)
    else:
        g.pygame.draw.rect(g.screen, "white", square)

