import random
MAX_GOLD_COUNT = 500

class SellAnApple:
    def __init__(self):
        self.apples = 0
        self.gold = 0
        self.total_apples = 0

    def show_choice(self):
        options = ["",
                   "1. Pick Apple",
                   "2. Sell Apple",
                   "Select option (1/2) : "]
        ask = input("\n".join(options))
        if ask == "1":
            return self.pick()
        else:
            return self.sell()

    def pick(self):
        self.apples += 1
        self.total_apples += 1
        print("You have", self.apples, "apples and", self.gold, "golds")

    def sell(self):
        if self.apples == 0:
            print("Pick more apples to get more than", MAX_GOLD_COUNT, "golds")
        else:
            price = random.randint(50, 250)
            print("Apple is sold at price", price)
            self.gold += price
            self.apples -= 1
        print("You have", self.apples, "apples and", self.gold, "golds")

    def play(self):
        print("************** WElCOME TO THE SELL AN APPLE GAME ********************")
        while self.gold <= MAX_GOLD_COUNT:
            self.show_choice()
        print("\nCongratulations you met the target with", self.gold, "golds")
        print("You sold ", self.total_apples - self.apples, "apples with", self.apples, "apples remaining")
        print("Your score is", 100//self.total_apples)

def main():
    choice = "Y"
    while choice.upper() == "Y":
        app = SellAnApple()
        app.play()
        choice = input("\nPlay Again? (y/n) : ")
    print("See you again")

if __name__ == '__main__':
    main()