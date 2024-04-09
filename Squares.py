#Might merge w/ Piece because they're basically the same
from Piece import Piece
import Piece as p
import Globals as g
import Board as b
#Contains array of pieces along with draw() for simple drawing of all pieces
selected = None

piece_positions = [ [p.Rook(0, 0, "B"), p.Knight(1, 0, "B"), p.Bishop(2, 0, "B"), p.Queen(3, 0, "B"), p.King(4, 0, "B"), p.Bishop(5, 0, "B"), p.Knight(6, 0, "B"), p.Rook(7, 0, "B")],
                    [p.Pawn(0, 1, "B"), p.Pawn(1, 1, "B"),   p.Pawn(2, 1, "B"),   p.Pawn(3, 1, "B"),  p.Pawn(4, 1, "B"), p.Pawn(5, 1, "B"),   p.Pawn(6, 1, "B"),   p.Pawn(7, 1, "B")],
                    [None,              None,                None,                None,               None,              None,                None,                None],
                    [None,              None,                None,                None,               None,              None,                None,                None],
                    [None,              None,                None,                None,               None,              None,                None,                None],
                    [None,              None,                None,                None,               None,              None,                None,                None],
                    [p.Pawn(0, 6, "W"), p.Pawn(1, 6, "W"),   p.Pawn(2, 6, "W"),   p.Pawn(3, 6, "W"),  p.Pawn(4, 6, "W"), p.Pawn(5, 6, "W"),   p.Pawn(6, 6, "W"),   p.Pawn(7, 6, "W")],
                    [p.Rook(0, 7, "W"), p.Knight(1, 7, "W"), p.Bishop(2, 7, "W"), p.Queen(3, 7, "W"), p.King(4, 7, "W"), p.Bishop(5, 7, "W"), p.Knight(6, 7, "W"), p.Rook(7, 7, "W")]]

#REQUIRES: position to be tuple in form of (x, y)
#Checks if the requested position is selectable for the caller
def contains_selectable_piece(position):
    x = position[0]
    y = position[1]
    piece = piece_positions[y][x]
    print(x, y)
    if piece != None:
        #if position is the correct color for turn
        if piece.color == g.curr_turn:
            return True
    return False

def draw_pieces():
    #Black Pieces
    for array in piece_positions:
        for piece in array:
            if piece != None:
                piece.draw()

#redraws square moved to and square moved from
def redraw_squares(source, dest):
    piece = piece_positions[dest[1]][dest[0]]

    b.draw_single_square(source)
    b.draw_single_square(dest)

    #redraw piece2
    if piece != None:
        piece.draw()

def update_squares(source, dest, piece):
    if piece_positions[dest[1]][dest[0]] == None:
        #change piece's x and y coords
        piece.move(dest)

        #move piece in matrix
        piece_positions[dest[1]][dest[0]] = piece
        piece_positions[source[1]][source[0]] = None
    else:
        piece.move(dest)
        piece_positions[dest[1]][dest[0]] = piece
        piece_positions[source[1]][source[0]] = None

        #TODO: Implement capture functionality and delete or rework code above (w/ point system instead of just deleting the piece)

        
    #redraw the current squares
    redraw_squares(source, dest)