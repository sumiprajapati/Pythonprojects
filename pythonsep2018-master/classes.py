
class User:
    """
    This class defines the vehicle object
    """
    # attributes or properties or data type
    # methods or function

    # encapsulation
    # __var_name__ = private variable
    # _var = protected varible
    # var_name = public

    def __init__(self, name="John", age=35, height=6.5): # constructor method, inbuild method
        self.__name = name # attributre
        # self._name = name # attributre
        # self.name = name # attributre
        self.__height = height
        self.__age = age

    def __str__(self):
        return "name = {} with  age ={} and height = {}".format(self.__name,self.__age, self.__height)

    def __eq__(self, other):
        return self.__name == other.__name

    def show_name(self):  # custom method
        print(self.__name)

    def set_name(s, name):
        s.__name = name


class Student(User): # inheritance
    """This is student class"""

    def __init__(self, name="Student class", age=0, height=0.0, roll=100):
        self.__roll = roll
        self.__name1 = name
        super(Student, self).__init__(name, age, height)
        # User.__init__(self, name, age, height)

    def set_name(s, name):
        ""

    def set_roll(self, roll):
        self.__roll = roll

    def show_roll(self):
        print(self.__roll)



s = Student("St", 12, 23.4, 34)
print(s)
s2 = Student("St", 3453,3456,43)
print(s is s2)
print( s == s2)

s.show_name()
s.set_name("Student 1")
s.show_name()
# s.set_roll(35)
s.show_roll()




# u = User("John", 22, 5.5) # create object
#
# u.name = "John"
# u.age = 18
# u.height = 5.5
#
# print(u.name)
# # print(u.__name)
# print(u.age)
# print(u.height)
#
# u.show_name()
# u.set_name("Santosh")
# u.show_name()


# print(())

