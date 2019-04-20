class LeftParagraph:
    def __init__(self, lenght: int):
        self.len = lenght
        self.words = []

    def add_word(self, word: str):
        self.words += [word]

    def end(self):
        to_print = ''
        for i in range(len(self.words)):
            if len(to_print + self.words[i]) + 1 <= self.len:
                to_print += ' ' + self.words[i]
                to_print = to_print.strip()
            else:
                print(to_print.ljust(self.len, ' ')) if to_print else ...
                to_print = self.words[i]
        print(to_print.ljust(self.len, ' ')) if to_print else ...
        self.words = []


class RightParagraph:
    def __init__(self, lenght: int):
        self.len = lenght
        self.words = []

    def add_word(self, word: str):
        self.words += [word]

    def end(self):
        to_print = ''
        for i in range(len(self.words)):
            if len(to_print + self.words[i]) + 1 <= self.len:
                to_print += ' ' + self.words[i]
                to_print = to_print.strip()
            else:
                print(to_print.rjust(self.len, ' ')) if to_print else ...
                to_print = self.words[i]
        print(to_print.rjust(self.len, ' ')) if to_print else ...
        self.words = []
