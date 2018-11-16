
def string_format():
    name = "John Doe"
    age = 45
    height = 65.5

    str1 = "name is " + name + " age is " + str(age) + " height is " + str(height)
    print(str1)

    str2 = "name is %s age is %d height is %f" % (name, age, height)
    print(str2)

    str3 = "name is {} age is {} height is {}".format(name, age, height)
    print(str3)

    str4 = "name is {name} age is {age} height is {height}".format(height=height, name=name, age=age)
    print(str4)

if __name__ == '__main__':
    string_format()