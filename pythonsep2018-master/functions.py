# def say_hello():
#     print("Hello")
#
#
# say_hello()
#
#
# def show_text_twice(text):
#     print(text)
#     print(text)
#
#
# show_text_twice("there")

# def show_box(text, pattern="*"):
#     print(pattern*(len(text)+4))
#     print(pattern, text, pattern)
#     print(pattern*(len(text)+4))
#
# show_box("my texts", "$")
# show_box("hi")
# show_box("my texts my texts my texts my texts", "#")
# show_box("This is single parameter")
#
#
# def sum(a,b):
#     return a+b
#
# c = sum(4634,2354)
# print(c)
#
# print(sum("Hello", "World"))

counter = 0

def show_counter():
    print("Value of counter is", counter)


def increase_counter():
    global counter
    counter = 1
    counter = counter + 1

def counter_test():
    show_counter()
    increase_counter()
    show_counter()
    increase_counter()
    increase_counter()
    show_counter()


def find_min_max(mylist):
    # return min(mylist), max(mylist)

    if mylist:
        min = mylist[0] # 23 23 23 22 2 2
        max = mylist[0] # 23 45 234 234 234 454
        for item in mylist:
            if min > item:
                min = item
            if max < item:
                max = item
        return (min, max, 1, 3)
    else:
        print("Please provide some items")
        return None

def main():
    mi, mx, one, three = find_min_max([23,45,234,22,2,454])
    print("Min val is", mi, "Max value is", mx)
    print(find_min_max([]))
    a = find_min_max([2345,45456,24634,2442,442,454])
    print(a)

def character_counter(word):
    data = {}
    for ch in word:
        if ch not in data:
            data[ch] = 1
        else:
            data[ch] = data[ch] + 1
    return data


def parameter_passing(name, age, height):
    print("Name is", name)
    print("Age is", age)
    print("height is", height)

def print_all(*args):
    for arg in args:
        print(arg)


def sum_all(*num): # num is always tuple
    "this sums any number of input arguments"
    print(num)  # prints tuple
    print(*num)
    sum = 0
    for i in num:
        sum += i
    print(sum)
    return sum

def length(items):
    ""
    count = 0
    for c in items:
        count += 1
    return count

if __name__ == '__main__':
    s = "Hello there whats up"
    li = [34534,436,34,63,"34364","34534","efgfd"]
    print(len(s))
    print(length(s))
    print(len(li))
    print(length(li))

    # sum_all(24)
    # sum_all(45,64)
    # sum_all(35,3,5,4,46,4,4,45,4)

    # print_all(124)
    # print_all(1,34)
    # print_all("hello",  "there", 5 , "lines", "printing")
    # t = ("John1", 26, 65.51)
    # parameter_passing(*t)
    # parameter_passing("John", 25, 65.5)
    # # parameter_passing("John12", 25)
    # parameter_passing(age=25, name="Raj", height=75.6)
    # # parameter_passing(age=15, name="Ram")
    # # dic = character_counter("google.com")
    # # print(dic)



