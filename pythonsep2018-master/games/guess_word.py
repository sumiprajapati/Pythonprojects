class GuessWord:

    def __init__(self):
        self.matrix = [list("ABCDE"),list("FGHIJ"),list("KLMNO"),list("PQRST"),list("UVWXY"),list("Z-@.1")]
        self.selected = []
        self.round = 1

    def __str__(self):
        if len(self.matrix) == 0:
            return "Empty matrix"
        header = []
        cols = 5 if self.round == 1 else 6
        for i in range(1, 1 + cols):
            header.append(str(i))
        lines = list()
        lines.append((5*" ").join(header))
        lines.append("-" * 5 * cols)
        for rows in self.matrix:
            lines.append((5*" ").join(rows))
        return "\n".join(lines)

    def validate(self, data):
        try:
            data = int(data)
        except ValueError:
            print("Invalid input")
            return
        if data < 1 or data > (5 if self.round == 1 else 6):
            print("Invalid number")
            return
        self.selected.append(data)

    def get_col(self, col):
        cols = []
        for i in range(len(self.matrix)):
            cols.append(self.matrix[i][col-1])
        return cols

    def update_matrix(self):
        mat = []
        for sel in self.selected:
            mat.append(self.get_col(sel))
        self.matrix = mat
        self.selected = []
        self.round = 2

    def get_word(self):
        word = []
        for index, sel in enumerate(self.selected):
            word.append(self.matrix[index][sel-1])
        print("You guessed the word", "".join(word))

    def play(self):
        print("Guess a word in your mind and tell me the group.")
        while True:
            print(self)
            data = input("Column for letter %d Enter (1-5) or 0 to terminate: " % (len(self.selected)+1))
            if data == "0":
                break
            self.validate(data)

        # input word done, now convert matrix
        self.update_matrix()

        # again ask for next round
        while len(self.selected) < len(self.matrix):
            print(self)
            data = input("Enter column for letter %d/%d (1-6): " % (len(self.selected) + 1, len(self.matrix)))
            self.validate(data)

        # we are finished
        self.get_word()


def main():
    again = "Y"
    while again.upper() == "Y":
        guess = GuessWord()
        guess.play()
        again = input("Play Again (Y/N)? : ")
    print("Bye Bye")

if __name__ == '__main__':
    main()
