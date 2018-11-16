"""
7 128   ****    ******    **      **
6 64  **    **  **    **  **    **
5 32  **    **  **    **  **  **
4 16  ********  ******    ****
3 8   **    **  **    **  **  **
2 4   **    **  **    **  **    **
1 2   **    **  ******    **      **
0 1

A - 126,144,144,126
B - 254,146,146,108
K - 254,16,40,68,130
"""

class CharPattern:

    characters = {
        "A": [126,144,144,126],
        "B": [254, 146, 146, 108],
        "K": [254, 16, 40, 68, 130],
        "I": [254]

    }

    def __init__(self):
        self.data = []

    def get_char_array(self, ch):
        return CharPattern.characters[ch]


    def show_string(self, string):
        for ch in string:
            self.data.extend(self.get_char_array(ch))
            self.data.append(0)
        print(self.data)
        self.display()

    def display(self):
        ""

        for d in range(8, 0, -1):
            for c in self.data:
                if (c >> d) % 2 == 1:
                    print("**", end="")
                else:
                    print("  ", end="")
            print()


def main():
    p = CharPattern()
    p.show_string("ABIK")


if __name__ == '__main__':
    main()