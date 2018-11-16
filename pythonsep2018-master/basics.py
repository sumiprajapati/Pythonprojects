"""
This is basic module docString

"""
import math


def calculate_area():
    """
    Takes input
    processes input and generate result
    display result
    """
    radius = float(input("Enter radius of circle : "))
    pi = math.pi
    # area = pi * math.pow(radius, 2)
    area = pi * power(radius, 2)
    print("Area of circle is", area)


def power(base, exponent):
    "calculates power of base to exponent term"
    result = 1
    for i in range(exponent):
        result *= base
    return result


def pattern(number):
    """
*
**
***
****
*****
     n=5    i   sp  st
    *       0   4   1
   **       1   3   2
  ***       2   2   3
 ****       3   1   4
*****       4   0   5

    *       0   4   1
   ***      1   3   3
  *****     2   2   5
 *******    3   1   7
*********   4   0   9
 *******    0   1   7
  *****     1   2   5
   ***      2   3   3
    *       3   4   1


    :return:
    """
    # number = input("Enter number : ")

    # c style
    # for i in range(1, number+1):
    #     for j in range(i):
    #         print(j+1, end="")
    #     print()

    for i in range(number):
        spaces = number - 1 - i
        stars = 2 * i + 1
        print("  " * spaces, "* " * stars, sep="")

    for i in range(number-1):
        spaces = i + 1
        stars = (number - i) * 2 - 3
        print("  " * spaces, "* " * stars, sep="")


def char_pattern():
    """

********      0     4   0   4
**    **      1     2   4   2
**    **      2     2   4   2
********      3     4   0   4
**    **      4     2   4   2
**    **      5     2   4   2
**    **      6     2   4   2

**      **      0     2   6   2
**    **        1     2   4   2
**  **          2     2   2   2
****            3     2   0   2
**  **          4     2   2   2
**    **        5     2   4   2
**      **      6     2   6   2



    :return:
    """
    for i in range(7):
        st1 = 2
        st2 = 2
        sp = 0
        if i == 0 or i == 6:
            sp = 6
        elif i == 1 or i == 5:
            sp = 4
        elif i == 2 or i == 4:
            sp = 2

        # if i < 3:
        #     sp = 6 - 2*i
        # else:
        #     sp = 2*(i-3)

        print("*" * st1, " " * sp, "*" * st2, sep="")


def input_to_tuples():  # 2,3,4,5,6
    ip = input("Enter comma ceperated values : ")
    li = ip.split(",")
    tu = tuple(li)
    print("Splitted value in list", li)
    print("Splitted value in tuple", tu)

def main():
    # calculate_area()
    # print(help(power))
    # print(power(4, 3))  # 64
    # print(power(5, 2))  # 25
    # print(power(2, 8))  # 256

    # input_to_tuples()
    pattern(10)
    # char_pattern()


if __name__ == '__main__':
    main()