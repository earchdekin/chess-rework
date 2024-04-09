# import pygame
# import Board.DrawChessBoard

# chess_board = [[5, 2, 3, 9, 10, 3, 2, 5],
#                 [1, 1, 1, 1, 1, 1, 1, 1],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [0, 0, 0, 0, 0, 0, 0, 0],
#                 [1, 1, 1, 1, 1, 1, 1, 1],
#                 [5, 2, 3, 10, 9, 3, 2, 5]]

# class ColumnNames:
#     x = 1

# class Piece:
#     def __init__(self, piece, color, x, y) -> None:
#         self.piece = piece
#         self.color = color
#         self.x = x
#         self.y = y
#         pass

#     def draw():
#         dcb = Board.DrawChessBoard.DrawChessBoard
#         return dcb.screen.blit(pygame.transform.scale(pygame.image.load(self.color + "_" + self.piece + ".png"), (piece_x, piece_y)), ((piece_x * self.x), (piece_y * self.y)))

# class Pawn(Piece): #only move up or down the board
#     ID = 1
#     point_value = 1

# class Knight(Piece): #only move +/- 2 horizontal and +/- 1 on vertical or vice versa
#     ID = 2
#     point_value = 3

# class Bishop: # Diagonal Movement
#     ID = 3
#     point_value = 3

# class Rook(Piece): # Horizontal and Vertical Movement
#     ID = 5
#     point_value = 5

# class Queen(Piece): #Horizontal, Vertical and Diagonal Movement
#     ID = 9
#     point_value = 9

# class King(Piece): #Moves one square away in any direction
#     ID = 10
#     point_value = 200