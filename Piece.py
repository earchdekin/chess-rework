import Board as b
import Globals as g
import Squares as squares

class Piece:
    def __init__(self, piece, x, y, color, value) -> None:
        self.piece = piece
        self.x = x
        self.y = y
        self.color = color
        self.value = value

    #draws the png of the piece onto the screen
    def draw(self):
        return g.screen.blit(g.pygame.transform.scale(g.pygame.image.load("imgs/" + self.color + "_" + self.piece + ".png"), (b.square_size_x, b.square_size_y)), ((b.square_size_x * self.x), (b.square_size_y * self.y)))
    
    #compares self position  (x and y) with given arguement "pos" and returns true if legal move
    def is_legal_move(self, pos): 
        #TODO: Implement the movement functionality of each piece
        return True
    
    #changes piece location (in name only. real movement changes in squares)
    def move(self, newPos):
        x = newPos[0]
        y = newPos[1]
        self.x = x
        self.y = y

class Rook(Piece):
    def __init__(self, x, y, color):
        super().__init__("Rook", x, y, color, 5)
    
    def is_legal_move(self, pos):
        if self.x == pos[0] and self.y != pos[1] or self.x != pos[0] and self.y == pos[1]:
            if self.is_blocked_by_piece(pos):
                return False
            
            return True
        
        return False
    
    #NOTE: Helper function for is_legal_move
    #REQUIRES: either x = pos[0] or y = pos[1]
    def is_blocked_by_piece(self, pos):
        x = self.x
        y = self.y

        dest = (x, y)

        posX = pos[0]
        posY = pos[1]

        #While x and y are not equal to the destination position, check for obstructions in path
        while dest != pos:
            
            if x >= b.BOARD_SIZE_X or x < 0:
                return False
            if y >= b.BOARD_SIZE_Y or y < 0:
                return False

            #Checks for obstruction in path
            if squares.piece_positions[y][x] != None and squares.piece_positions[y][x] != self:
                print("blocked by " + squares.piece_positions[y][x].piece, x, y)
                return True

            #increment or decrement of x or y based on position's relative location to self
            if x == posX:
                if y < posY:
                    y += 1
                else:
                    y -= 1
            else: #implied that y = posY
                if x < posX:
                    x += 1
                else:
                    x -= 1
            dest = (x, y)
        return False

                

    
class Knight(Piece):
    def __init__(self, x, y, color):
        super().__init__("Knight", x, y, color, 3)

    def is_legal_move(self, pos):
        newX = pos[0]
        newY = pos[1]
        if newY == self.y + 2 or newY == self.y - 2:
            if newX == self.x - 1 or newX == self.x + 1:
                return True
        elif newX == self.x + 2 or newX == self.x - 2:
            if newY == self.y - 1 or newY == self.y + 1:
                return True
        return False

class Bishop(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__("Bishop", int(x), int(y), color, 3)
    
    def is_legal_move(self, pos):
        newX = pos[0]
        newY = pos[1]

        dx = abs(newX - self.x)
        dy = abs(newY - self.y)
        if (dx == dy) and (dx > 0):
            if self.is_blocked_by_piece(pos):
                return False
            
            return True
        return False
    
    #private
    def is_blocked_by_piece(self, pos):
        newX = pos[0]
        newY = pos[1]
        
        x = int(self.x)
        y = int(self.y)
        while x != newX and y != newY: #stop just short of position to avoid detecting captures as blocks
            
            #if index out of bounds, return false
            if x >= b.BOARD_SIZE_X or x < 0:
                return False
            if y >= b.BOARD_SIZE_Y or y < 0:
                return False

            if squares.piece_positions[y][x] != None and squares.piece_positions[y][x] != self:
                print("blocked by " + squares.piece_positions[y][x].piece, x, y)
                return True
            if newX > x:
                if newY > y:
                    x += 1
                    y += 1
                else:
                    x += 1
                    y -= 1
            else:
                if newY > y:
                    x -= 1
                    y += 1
                else:
                    x -= 1
                    y -= 1
        return False


class Queen(Bishop, Rook):
    def __init__(self, x, y, color) -> None:
        Piece.__init__(self, "Queen", x, y, color, 9)
    
    def is_legal_move(self, pos):
        if Bishop.is_legal_move(self, pos):
            return True
        elif Rook.is_legal_move(self, pos):
            return True
        return False

class King(Piece):
    def __init__(self, x, y, color) -> None:
        super().__init__("King", x, y, color, 1000)
    
    def is_legal_move(self, pos):
        newX = pos[0]
        newY = pos[1]
        if newY >= int(self.y - 1) and newY <= int(self.y + 1):
            if newX >= int(self.x - 1) and newX <= int(self.x + 1):
                return True
        return False

class Pawn(Piece):
    def __init__(self, x, y, color):
        super().__init__("Pawn", x, y, color, 1)
        self.is_first_move = True

    def is_legal_move(self, pos):
        if self.can_capture_diagonally(pos):
            return True
        
        if self.color == "W":
            #only -1 or -2 in y
            if self.is_first_move:
                if self.x == pos[0] and self.y >= pos[1] and self.y - 2 <= pos[1]:
                    return True
            else:
                if self.x == pos[0] and self.y >= pos[1] and self.y - 1 <= pos[1]:
                    return True
            
        else:
            #only +1 or +2 in y
            if self.is_first_move:
                if self.x == pos[0] and self.y <= pos[1] and self.y + 2 >= pos[1]:
                    return True
            else:
                if self.x == pos[0] and self.y <= pos[1] and self.y + 1 >= pos[1]:
                    return True
        

        print("not legal pawn move")
        return False
    

    #changes piece location (in name only. real movement changes in squares)
    def move(self, newPos):
        super().move(newPos)
        if self.is_first_move:
            self.is_first_move = False
    
    #private pawn function - checks if pawn can capture diagonally 
    def can_capture_diagonally(self, pos):
        x = pos[0]
        y = pos[1]
        if squares.piece_positions[y][x] != None:  
            if self.color == "W":
                if y == self.y - 1:
                    if x == self.x - 1 or x == self.x + 1:
                        return True
            else:
                if y == self.y + 1:
                    if x == self.x - 1 or x == self.x + 1:
                        return True
        return False
    