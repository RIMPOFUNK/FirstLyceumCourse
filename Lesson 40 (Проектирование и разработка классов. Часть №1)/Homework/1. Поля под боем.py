class Figure:
    def __init__(self, row, col, color):
        self.row, self.col = row, col
        self.color = color

    def set_position(self, row, col):
        self.row, self.col = row, col

    def get_color(self):
        return self.color


def correct_coords(row, col):
    return 0 <= row < 8 and 0 <= col < 8


class Knight(Figure):
    def char(self):
        return 'N'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        return (abs(self.row - row) == 2 and abs(self.col - col) == 1) or \
               (abs(self.row - row) == 1 and abs(self.col - col) == 2)


class Bishop(Figure):
    def char(self):
        return 'B'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        return abs(self.row - row) == abs(self.col - col)


class Queen(Figure):
    def char(self):
        return 'Q'

    def can_move(self, row, col):
        if not correct_coords(row, col):
            return False
        return not (abs(self.row - row) != abs(self.col - col) and
                    self.row != row and self.col != col)


class Rook(Figure):
    def char(self):
        return 'R'

    def can_move(self, row, col):
        if self.row != row and self.col != col:
            return False
        return True


WHITE = 1
BLACK = 2


def opponent(color):
    if color == WHITE:
        return BLACK
    else:
        return WHITE


class Board:
    def __init__(self):
        self.color = WHITE
        self.field = []
        for row in range(8):
            self.field.append([None] * 8)

    def current_player_color(self):
        return self.color

    def cell(self, row, col):
        piece = self.field[row][col]
        if piece is None:
            return '  '
        color = piece.get_color()
        c = 'w' if color == WHITE else 'b'
        return c + piece.char()

    def move_piece(self, row, col, row1, col1):
        if not correct_coords(row, col) or \
                not correct_coords(row1, col1) \
                or (row == row1 and col == col1):
            return False

        piece = self.field[row][col]

        if piece is None or \
                piece.get_color() != self.color or \
                not piece.can_move(row1, col1):
            return False

        self.field[row][col] = None
        self.field[row1][col1] = piece
        piece.set_position(row1, col1)
        self.color = opponent(self.color)
        return True

    def is_under_attack(self, row, col, color):
        for i in range(8):
            for j in range(8):
                if self.field[i][j] and \
                        self.field[i][j].get_color() == color and \
                        self.field[i][j].can_move(row, col):
                    return True

        return False