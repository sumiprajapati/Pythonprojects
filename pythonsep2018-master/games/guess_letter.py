class GuessLetter:
    def __init__(self):
        self.letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ-")
        self.iteration = 0

    def __str__(self):
        line1 = "/------ 1 -------/------- 2 -------/------- 3 -------/\n"
        line2 = " ".join(self.letters)
        return line1 + line2

    def sort_group(self, group):
        try:
            group = int(group)
        except ValueError:
            print("Invalid input. Please enter (1/2/3)")
            return
        if group < 1 or group > 3:
            print("Invalid number. Please enter (1/2/3)")
            return

        # Put the selected group deck in the middle
        if group != 2:
            for i in range(9):
                if group == 1:
                    self.letters[i],self.letters[i+9] = self.letters[i+9],self.letters[i]
                elif group == 3:
                    self.letters[i+9],self.letters[i+18] = self.letters[i+18],self.letters[i+9]

        # Regroup the deck in 3 groups
        my_letters = []
        for i,l in enumerate(self.letters):
            if i % 3 == 0:
                my_letters.append(l)
        for i,l in enumerate(self.letters):
            if i % 3 == 1:
                my_letters.append(l)
        for i,l in enumerate(self.letters):
            if i % 3 == 2:
                my_letters.append(l)
        self.letters = my_letters
        self.iteration += 1

    def get_guess(self):
        return "You guessed the letter " + self.letters[13]

    def play(self):
        print("Guess a letter in your mind and tell me the group which it belongs.")
        while self.iteration < 3:
            print(self)
            self.sort_group(input("Enter Group (1/2/3) : "))
        print(self.get_guess())


def main():
    again = "Y"
    while again.upper() == "Y":
        guess = GuessLetter()
        guess.play()
        again = input("Play Again (Y/N)? : ")
    print("Bye Bye")

if __name__ == '__main__':
    main()
