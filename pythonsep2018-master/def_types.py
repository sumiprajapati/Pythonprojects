# # lambda function
#
#
# print((lambda a, b, c: a+b+c)(5, 30, 10))
#
# def sq(x):
#     return x*x
#
# t = (1,2,3,4)
# x = map(sq, t)
# print(tuple(x))
#
# print(list(map(lambda x:2*x, (5,34,346343534,"hi"))))
from functools import reduce

names = [
    {"name":"Ram", "address":"ktm", "height":65},
    {"name":"Ram1", "address":"pkr", "height":65},
    {"name":"Ram3", "address":"but", "height":65},
    {"name":"Ram4", "address":"ktm", "height":65},
    {"name":"Ram5", "address":"ktm", "height":65},
    {"name":"Ram6", "address":"pkr", "height":65},
 ]

#map - generate name only list
name_list = list(map(lambda x:x["name"], names))
print(name_list)

#filter - filter user from ktm only
def fil(x):
    if x["address"]=="ktm":
        return True
    else:
        return False

# ktm_list = list(filter(fil, names))
ktm_list = list(filter(lambda x:x["address"]=="ktm", names))

print(ktm_list)

li = [345,34,534,34,4,3,4,43,4,3,43]

def red(a,b):
    return a * b
r = reduce(red, li)
print(r)