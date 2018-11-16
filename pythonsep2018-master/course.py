
import random
from functions import find_min_max as m, counter_test
from string_format import string_format

def main():
    a =  m([13241,234,54,356,4,6])
    print(a)

    counter_test()

def exercise():
    before = [[1, 2], [3, 4], [5, 6]]
    after = []
    for number in before:
        # after.append(number[0])
        after.extend(number)
    print(after)

if __name__ == '__main__':
    main()