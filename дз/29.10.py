# x = 50
# y = 8


# if x < y:
#     print("x меньше y")

# elif y < x:
#     print("y меньше x")

# a = -20

# if a <= -1:
#     a = - a 
#     print(a)
    
# b = 5

# if b > 0:
#     print(1)
# elif b == 0:
#     print(0)
# elif b < 0:
#     print(-1)

# f = 6.5
# c = 7.2

# if c > f:
#     f,c = c,f 
# print(f,c)

# z = 2

# if z > -4 and z < 10:
#     print(" знаходиться в діапазоні")
# else:
#     print(" не знаходиться в діапазоні")
    
# q = 408

# if q % 4 == 0 and q % 100 != 0 or q % 400 == 0:
#     print(" Yes")

# else:
#     print("Not")

# p = 25.2
# v = 33.9
# s = 15

# if s < (p + v):
#     print("Недостатньо коштів:", s - (p + v))

# a = 7
# b = 7

# if a % b == 0:
#     print("Результат:", a // b)

# else:
#     print(" Числа не діляться")

class Animal:
    age = 0
    name = ""

    def jump(self):
        print("jump")

cat = Animal()
cat.age = 2
cat.name = "alex"

dog = Animal()
dog.age = 5
dog.name = " barni"
print( cat.age, cat.name, dog.age, dog.name )
cat.jump()
