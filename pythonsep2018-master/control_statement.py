
# condition = False
# if condition:
#     print("This is true condition")
# else:
#     print("This executes when condition is false")
#
# print("This line executes on both condition")


# num = int(input("Enter a number : "))
# print(type(num))
# if num == 5:
#     print("Number is 5")
# else:
#     if num == 6:
#         print("Number is 6")
#     else:
#         if num == 7:
#             print("Number is 7")
#         else:
#             print("Number is not 5 nor 6, nor 7")


# num = int(input("Enter a number : "))
# print(type(num))
# if num == 5:
#     print("Number is 5")
# elif num == 6:
#     print("Number is 6")
#     print("This is addition statement for 6")
# elif num == 7:
#     print("Number is 7")
# else:
#     print("Number", num, "is not 5 nor 6, nor 7")

# raining = True
# while raining:
#     print("It is raining")
#     x = input("Is it still raining ? (y/n) : ")
#     if x == "y":
#         raining = True
#         continue
#     elif x == "n":
#         raining = False
#         break
#     else:
#         print("Write only y or n next time")
#     print("Last line of loop")
#     raining = True
#
# print("Now its not raining")


# a =  input("Enter a and b")
# b = a.split(" ")
# print(type(a))
# print(type(b))
# print(a, b)

# iterator = ["4534",34634,"dsfhd","4534",(43634,4,6),435,"453",45,"a", "45"]
#
# for i in range(0, len(iterator)):
#     print("Index is",i,"value is",iterator[i])
#
# for indexdfsa in iterator:
#     print("value is", indexdfsa)
#
# i = 45
# if i in iterator:
#     print("Yes", i,"is member of iterator")
#
# iterator = {"4534":34634,"dsfhd":"4534","t":(43634,4,6),"n":435,"453":45,"a":"45"}
# for i in iterator:
#     print("key is", i, "Value is", iterator[i])
#
def five_things():
    things = []

    print("Enter 5 things: ")
    while len(things) < 5:
        thing = input("> ")
        things.append(thing)

    print("You entered these things:")
    for thing in things:
        print(thing)

def qa():
    questions_and_answers = [
            # [question, answer], ...
            ["What is 2+4? ", "6"],
            ["What is 2-4? ", "-2"],
            ["What is 2*4? ", "8"],
            ["What is 2/4? ", "0.5"],
            # You could add more questions, but the code that asks them
            # wouldn't need to be changed in any way.
        ]

    for qa in questions_and_answers:
            while True:
                if input(qa[0]) == qa[1]:
                    print("Correct!")
                    break
                else:
                    print("That's not what I was thinking of... Try again.")


def name_list():
    namelist = []

    print("Options:")
    print("  0      Quit")
    print("  1      Check if I know you")
    print("  2      Introduce yourself to me")
    print("  3      Make me forget you")
    print("  4      Print a list of people I know")
    print()     # print an empty line

    while True:
        option = input("Choose an option: ")

        # Things like option == 0 don't work because option is a string
        # and it needs to be compared with a string:
        #   >>> 0 == 0
        #   True
        #   >>> '0' == '0'
        #   True
        #   >>> 0 == '0'
        #   False
        if option == '0':
            print("Bye!")
            break

        elif option == '1':
            name = input("Enter your name: ")
            if name in namelist:
                print("I know you! :D")
            else:
                print("I don't know you :/")

        elif option == '2':
            name = input("Enter your name: ")
            if name in namelist:
                print("I knew you already.")
            else:
                namelist.append(name)
                print("Now I know you!")

        elif option == '3':
            name = input("Enter your name: ")
            if name in namelist:
                namelist.remove(name)
                print("Now I don't know you.")
            else:
                print("I didn't know you to begin with.")

        elif option == '4':
            if namelist == []:
                print("I don't know anybody yet.")
            else:
                for name in namelist:
                    print("I know %s!" % name)

        else:
            print("I don't understand :(")

        print()

if __name__ == '__main__':
    five_things()