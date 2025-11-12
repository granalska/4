# n = 0
# v = 6
# while v == 0:
#      break
# n += 1 ?
# print(v)


# n = 0
# v = 6
# while v == 0:
#       break
# n += 6
# print(n)

def outer(x):

    def inner(y):
     return x + y
     return inner

add_five = outer(5)
print(add_five 3 )
print(add_five(10))

 