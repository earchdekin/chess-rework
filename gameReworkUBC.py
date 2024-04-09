import pygame
import time

pygame.init()
WIDTH, HEIGHT = (600, 600)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

board_size_x, board_size_y = (8, 8)
total_squares = 64
square_size_x, square_size_y = ((WIDTH / board_size_x), (HEIGHT / board_size_x))

white_turn = True



#DRAWS PIECES
piece_x, piece_y = (WIDTH / board_size_x), (HEIGHT / board_size_y)

#COPIED TO PIECE.PY (Not Pieces.py)
class Piece:
    def __init__(self, piece, x, y, color) -> None:
        self.piece = piece
        self.x = x
        self.y = y
        self.color = color
        self.isSelected = False
        self.first_move = True

    #draws the png of the piece onto the screen
    def draw(self):
        return screen.blit(pygame.transform.scale(pygame.image.load("imgs/" + self.color + "_" + self.piece + ".png"), (piece_x, piece_y)), ((piece_x * self.x), (piece_y * self.y)))



#COPIED TO PIECES.PY (not to be mistaken w/ Piece.py)
pieces_b = [Piece("Rook", 0, 0, "B"), 
            Piece("Rook", 7, 0, "B"), 
            Piece("Bishop", 2, 0, "B"), 
            Piece("Bishop", 5, 0, "B"), 
            Piece("Knight", 1, 0, "B"), 
            Piece("Knight", 6, 0, "B"),
            Piece("Queen", 3, 0, "B"), 
            Piece("King", 4, 0, "B"), 
            Piece("Pawn", 0, 1, "B"), 
            Piece("Pawn", 1, 1, "B"), 
            Piece("Pawn", 2, 1, "B"), 
            Piece("Pawn", 3, 1, "B"),
            Piece("Pawn", 4, 1, "B"), 
            Piece("Pawn", 5, 1, "B"), 
            Piece("Pawn", 6, 1, "B"), 
            Piece("Pawn", 7, 1, "B")]

pieces_w = [Piece("Rook", 0, 7, "W"), 
            Piece("Rook", 7, 7, "W"), 
            Piece("Bishop", 2, 7, "W"),
            Piece("Bishop", 5, 7, "W"),
            Piece("Knight", 1, 7, "W"),
            Piece("Knight", 6, 7, "W"),
            Piece("Queen", 3, 7, "W"),
            Piece("King", 4, 7, "W"),
            Piece("Pawn", 0, 6, "W"),
            Piece("Pawn", 1, 6, "W"),
            Piece("Pawn", 2, 6, "W"),
            Piece("Pawn", 3, 6, "W"),
            Piece("Pawn", 4, 6, "W"),
            Piece("Pawn", 5, 6, "W"),
            Piece("Pawn", 6, 6, "W"),
            Piece("Pawn", 7, 6, "W")]

class Rook(Piece):
    def moves(self):
        self.horizontal = []
        self.vertical = []
        x_line = 0
        more_moves = True
        if white_turn == True:
            while x_line < board_size_x:
                for w in pieces_w:
                    if w.x == x_line and w.y == self.y:
                        more_moves = False
                if more_moves == True:
                    self.horizontal.append((x_line, self.y))
                x_line += 1
            y_line = 0
            more_moves = True
            while y_line < board_size_y:
                for w in pieces_w:
                    if w.x == self.x and w.y == y_line:
                        more_moves = False
                if more_moves == True:
                    self.vertical.append((self.x, y_line))
                y_line += 1
        print (self.horizontal, self.vertical)

blue = Rook("Rook", 4, 3, "B")
blue.moves()

#COPIED TO BOARD.PY
def board_initialize(): #DRAW CHESS BOARD

    screen.fill("white")
 
    x = 0
    y = 0
    while y < board_size_y:
        left_corner = ((WIDTH / board_size_x) * x)
        squares = pygame.Rect(left_corner, (HEIGHT / board_size_y) * y, square_size_x, square_size_y)
        x_is_even, y_is_even = (x % 2, y % 2)

        if y_is_even == 0 and x_is_even != 0:
            pygame.draw.rect(screen, "black", squares)
        elif y_is_even != 0 and x_is_even == 0:
            pygame.draw.rect(screen, "black", squares)
        x += 1
        if x >= 8:
            y += 1
            x = 0

#COPIED TO MOUSEEVENT.PY
def get_quadrant(position): #GETS POSITION OF QUADRANT THAT MOUSE IS IN
    x = 0
    y = 0
    while y < board_size_y:
        if position[0] >= square_size_x * x and position[0] < square_size_x * (x + 1) and position[1] >= square_size_y * y and position[1] <= square_size_y * (y + 1):
            quadrant_location = (x, y)

        x += 1
        if x >= 8:
            y += 1
            x = 0
    return quadrant_location

def in_front_check(piece, mouse_pos, boolean): #CHECKS IF THERE IS SAME COLOUR PIECE IN FRONT 
    global white_turn
    test = False
    if white_turn == True:
        for i in pieces_w:
            if mouse_pos[0] == i.x and mouse_pos[1] == i.y and i.color == piece.color:
                test = True
                piece.isSelected = False
        if test == False:
            piece.x = mouse_pos[0]
            piece.y = mouse_pos[1]
            capture_check(piece)
            piece.isSelected = False
            white_turn = boolean           
    else:
        test = False
        for i in pieces_b:
            if mouse_pos[0] == i.x and mouse_pos[1] == i.y and i.color == piece.color:
                test = True
                piece.isSelected = False
        if test == False:
            piece.x = mouse_pos[0]
            piece.y = mouse_pos[1]
            capture_check(piece)
            piece.isSelected = False
            white_turn = boolean

def rook_check(piece, mouse_pos, boolean):
    global white_turn
    test = False
    if white_turn == True:
        for i in pieces_w:
            if (mouse_pos[0] == i.x and mouse_pos[1] == i.y and i.color == piece.color):
                    test = True
                    piece.isSelected = False
        if test == False:
            piece.x = mouse_pos[0]
            piece.y = mouse_pos[1]
            capture_check(piece)
            piece.isSelected = False
            white_turn = boolean           
    else:
        test = False
        for i in pieces_b:
            if mouse_pos[0] == i.x and mouse_pos[1] == i.y and i.color == piece.color:
                test = True
                piece.isSelected = False
        if test == False:
            piece.x = mouse_pos[0]
            piece.y = mouse_pos[1]
            capture_check(piece)
            piece.isSelected = False
            white_turn = boolean 





def show_available_moves():
    if white_turn == True:
        for w in pieces_w:
            if w.isSelected == True:
                if w.piece == "Rook":
                    x = w.x
                    y = w.y
                    


def piece_check(piece, mouse_pos, boolean): #THE WAY EACH PIECE MOVES - E.G. WHICH DIRECTION IT GOES IN
    global white_turn
    if (piece.piece == "Pawn" and piece.color == "B"):
        if (piece.x == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x == mouse_pos[0] and piece.y + 2 == mouse_pos[1] and piece.first_move == True):
            piece.x = mouse_pos[0]
            piece.y = mouse_pos[1]
            piece.isSelected = False
            piece.first_move = False
            white_turn = boolean
        elif (piece.x + 1 == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x - 1 and piece.y + 1 == mouse_pos[1]):
            for w in pieces_w:
                if mouse_pos[0] == w.x and mouse_pos[1] == w.y:
                    piece.x = mouse_pos[0]
                    piece.y = mouse_pos[1]
                    capture_check(piece)
                    piece.isSelected = False
                    piece.first_move = False
                    white_turn = boolean
    elif (piece.piece == "Pawn" and piece.color == "W"):
        if (piece.x == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x == mouse_pos[0] and piece.y - 2 == mouse_pos[1] and piece.first_move == True):
            in_front_check(piece, mouse_pos, boolean)
        elif (piece.x + 1 == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x - 1 and piece.y - 1 == mouse_pos[1]):
            for b in pieces_b:
                if mouse_pos[0] == b.x and mouse_pos[1] == b.y:
                    piece.x = mouse_pos[0]
                    piece.y = mouse_pos[1]
                    capture_check(piece)
                    piece.isSelected = False
                    piece.first_move = False
                    white_turn = boolean
    elif piece.piece == "Rook":
        if piece.x == mouse_pos[0] and piece.y != mouse_pos[1] or piece.x != mouse_pos[0] and piece.y == mouse_pos[1]:
            in_front_check(piece, mouse_pos, boolean)
    elif piece.piece == "Bishop":
        x = 0
        while x < board_size_x:
            if (piece.x + x == mouse_pos[0] and piece.y + x == mouse_pos[1]) or (piece.x - x == mouse_pos[0] and piece.y + x == mouse_pos[1]) or (piece.x - x == mouse_pos[0] and piece.y - x == mouse_pos[1]) or (piece.x + x == mouse_pos[0] and piece.y - x == mouse_pos[1]):
                in_front_check(piece, mouse_pos, boolean)
            x += 1
    elif piece.piece == "Knight":
        if (piece.x + 2 == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x + 2 == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x - 2 == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x - 2 == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x + 1 == mouse_pos[0] and piece.y + 2 == mouse_pos[1]) or (piece.x + 1 == mouse_pos[0] and piece.y - 2 == mouse_pos[1]) or (piece.x - 1 == mouse_pos[0] and piece.y + 2 == mouse_pos[1]) or (piece.x - 1 == mouse_pos[0] and piece.y -2 == mouse_pos[1]):
            in_front_check(piece, mouse_pos, boolean)
    elif piece.piece == "King":
            if (piece.x + 1 == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x + 1 == mouse_pos[0] and piece.y == mouse_pos[1]) or (piece.x + 1 == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x - 1 == mouse_pos[0] and piece.y + 1 == mouse_pos[1]) or (piece.x - 1 == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x - 1 == mouse_pos[0] and piece.y == mouse_pos[1]) or (piece.x == mouse_pos[0] and piece.y - 1 == mouse_pos[1]) or (piece.x == mouse_pos[0] and piece.y + 1 == mouse_pos[1]):
                in_front_check(piece, mouse_pos, boolean)
    elif piece.piece == "Queen":
        x = 0
        while x < board_size_x:
            if (piece.x + x == mouse_pos[0] and piece.y + x == mouse_pos[1]) or (piece.x - x == mouse_pos[0] and piece.y + x == mouse_pos[1]) or (piece.x - x == mouse_pos[0] and piece.y - x == mouse_pos[1]) or (piece.x + x == mouse_pos[0] and piece.y - x == mouse_pos[1]) or (piece.x == mouse_pos[0] and piece.y != mouse_pos[1]) or (piece.x != mouse_pos[0] and piece.y == mouse_pos[1]):
                in_front_check(piece, mouse_pos, boolean)
            x += 1
    else:
        return

def capture_check(piece): #CHECKS IF MOVE IS A CAPTURE- IF CAPTURE, PIECE IS TAKEN
    if piece.piece != "Pawn":
        if white_turn == True:
            for b in pieces_b: #looping through black pieces to check if capturable
                if piece.x == b.x and piece.y == b.y:
                    pieces_b.remove(b)
        elif white_turn == False:
            for w in pieces_w: #looping through white pieces
                if piece.x == w.x and piece.y == w.y:
                    pieces_w.remove(w)

def which_turn(boolean, mouse_pos, piece): #WHOSE TURN IT IS (WHITE TO MOVE UPON START)
    global white_turn
    if mouse_pos == (piece.x, piece.y):
                piece.isSelected = True

    if piece.isSelected == True and mouse_pos != (piece.x, piece.y):
        piece_check(piece, mouse_pos, boolean)

#BASIC MOVEMENT OF PIECES
def move_pieces(piece): #ONLY ACCEPTS piece FROM CHESS CLASS
    mouse_pos = get_quadrant(pygame.mouse.get_pos())
    global white_turn

    if white_turn and piece.color == "W":
        which_turn(False, mouse_pos, piece)
    elif white_turn == False and piece.color == "B":
        which_turn(True, mouse_pos, piece)

#COPIED TO PIECES.PY   
def draw_pieces():
    #Black Pieces
    for piece in pieces_b:
        piece.draw()
    
    #White Pieces
    for piece in pieces_w:
        piece.draw()


def move_all_pieces():
    for piece in pieces_b:
        move_pieces(piece)

    #White
    for piece in pieces_w:
        move_pieces(piece)

def main():
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                move_all_pieces()
        board_initialize()
        draw_pieces()
        
        
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()