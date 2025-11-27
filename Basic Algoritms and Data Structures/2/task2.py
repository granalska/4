from collections import deque

def is_palindrome(text):
    #привести до нижнього регістру і прибрати пробіли
    cleaned = "".join(char.lower() for char in text if char.isalnum())

    #додати символи до deque
    d = deque(cleaned)

    #pорівняти символи з обох сторін
    while len(d) > 1:
        if d.popleft() != d.pop():
            return False
    return True


#перевірка
user_input = input("Введіть рядок: ")

if is_palindrome(user_input):
    print("Це паліндром")
else:
    print("Це не паліндром")