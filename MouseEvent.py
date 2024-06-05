import Board as b
import Globals as g
import Squares as square

#Event checker when mouse is clicked

#ONLY HANDLE_CLICK SHOULD CALL THIS FUNCTION (for now)
#Converts pixel position to square position
def get_quadrant(mouse_pos):
    x = mouse_pos[0]
    y = mouse_pos[1]

    rX, rY = (0, 0)

    if x >= g.WIDTH or y >= g.HEIGHT:
        print("Position is out of bounds. Tried to Access (" + x + ", " + y + ") but window is of size (" + g.WIDTH + ", " + g.HEIGHT + ")")
        return None
    else:
        rX = int(x / b.square_size_x)
        rY = int(y / b.square_size_y)
    return (rX, rY)

def handle_click(mouse_pos):
    #current position
    current_pos = get_quadrant(mouse_pos)
    x = current_pos[0]
    y = current_pos[1]

    #So far, if there are no selected pieces or the previous selected piece has the same color as the current turn,
    #check if the square has a selectable piece of the same color as curr_turn
    #if the square is empty or returns false, check if legal move for current selected piece
    if g.selected_piece == None or g.selected_piece.color == g.curr_turn:
        if square.contains_selectable_piece(current_pos): #if square contains selectable piece, global var selected_piece = current_pos
            g.selected_piece = square.piece_positions[y][x]
            print(g.selected_piece.piece + " selected")
        else: 
            #check if legal move for current selected piece if one selected
            if g.selected_piece != None:
                if g.selected_piece.is_legal_move(current_pos):
                    source = (g.selected_piece.x, g.selected_piece.y)
                    #Update numbers on piece
                    square.update_squares(source, current_pos, g.selected_piece)
                    g.selected_piece = None
                    if g.curr_turn == "W":
                        g.curr_turn = "B"
                    else:
                        g.curr_turn = "W"
                else:
                    print(g.selected_piece.piece + " Deselected")
                    g.selected_piece = None

    
