class TicTacToeBoard:
    def __init__(self):
        self.who_doing = '0'
        self.new_game()
        self.winner = None

    def new_game(self):
        self.field = [['-' for _ in range(3)] for _ in range(3)]
        self.who_doing = 'X' if self.who_doing == '0' else '0'

    def get_field(self):
        return self.field

    def check_field(self):
        winner = []
        for i in self.field:
            for j in range(len(i) - 2):
                if i[j] == i[j + 1] == i[j + 2] == 'X' and not winner:
                    winner += 'X'
                    break
                if i[j] == i[j + 1] == i[j + 2] == '0'and not winner:
                    winner += '0'
                    break

        for i in range(3):
            if self.field[i][0] == self.field[i][1] == self.field[i][2] == 'X':
                winner += 'X'
            if self.field[0][i] == self.field[1][i] == self.field[2][i] == 'X':
                winner += 'X'
            if self.field[0][0] == self.field[1][1] == self.field[2][2] == 'X':
                winner += 'X'
            if self.field[0][2] == self.field[1][1] == self.field[2][0] == 'X':
                winner += 'X'

            if self.field[i][0] == self.field[i][1] == self.field[i][2] == '0':
                winner += '0'
            if self.field[0][i] == self.field[1][i] == self.field[2][i] == '0':
                winner += '0'
            if self.field[0][0] == self.field[1][1] == self.field[2][2] == '0':
                winner += '0'
            if self.field[0][2] == self.field[1][1] == self.field[2][0] == '0':
                winner += '0'

        if len(winner) == 0:
            return self.winner
        if winner and all(map(lambda x: x == 'X', winner)) or all(map(lambda x: x == '0', winner)):
            self.winner = winner[0]
        if len(winner) > 2 and not (all(map(lambda x: x == 'X', winner)) or all(map(lambda x: x == '0', winner))):
            self.winner = 'D'
        return self.winner

    def make_move(self, cow, col):
        if self.winner:
            return "Игра уже завершена"

        if self.field[cow - 1][col - 1] == '-':
            self.field[cow - 1][col - 1] = self.who_doing
            self.who_doing = 'X' if self.who_doing == '0' else '0'
        else:
            return f"Клетка {cow}, {col} уже занята"

        if not self.check_field():
            return "Продолжаем играть"
        if self.winner == 'D':
            return "Ничья"
        return f"Победил игрок {self.check_field()}"
