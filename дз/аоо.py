# num = input()
# if len(num) == 12 and num[1] == "(" and num[5] == ")" and num[0].isdigit() and num[2:5].isdigit() and num[6:].isdigit(): 
#     print("усе вірно")
# else:
#     print("не вірно набраний номер")

# s = input()
# if len(s) >= 4:
#     print("Перші 4 симв:", s[:5])

# text= "gjhgjgju"
# print(text[1::2])

# city = "київ суми харків"
# b= city.replace(" ", ":")
# print(b)

# n = input()
# b = 0
# for i in n:
#     if i.islower():
#         b+=1
# print(b)


# n = "кукурудза у полі"
# result = "".join('а' if ch == 'у' else ch for ch in n)
# print(result)

# def acronym(text):
#     return "".join(word[0].upper() for word in text.split() if word)

# phrase = "Харківський національний медичний університет"
# result = acronym(phrase)
# print(result)   


# a = list("hello")
# print(a)

# b = ['cat', 'dog', ' monkey']
# print(b[1][2])

# for i in b:
#     print(i[1].upper())

# print(b + b)
# print(b*2)
# b[1]= "bird"
# print(b)
# del b[2]
# print(b)

# v = [ 2, 4.7, 8]
# print(sum(v), max(v), min(v), sorted(v, reverse= True), len(v))
# v.sort(reverse=True)
# print(v)
# v.append("fire")
# print(v)

# v.insert(10, True)
# print(v)

# v.extend([1,2,3])
# print(v)

# v.remove(2)
# print(v)

# r = v.pop(3)
# print(r)
# print(v.index(4.7))
# print(v.count(2))

# v.reverse()
# print(v)

# b=v.copy()
# print(b, v)
# b[0]= 5
# print(b, v )
# v.clear()
# print(type(v))

# b = [-1,0,5,3,2, 0,34]

# for i in range(len(b)):
#     b[i]+= 7.2
# print(b)

# c = []
# b = float(input())
# print("Введіть числа до 0")
# while b != 0:
#     c.append(b**2)
#     b = float(input())
    
# print(c)
