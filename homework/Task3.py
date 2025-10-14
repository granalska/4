import re

#база даних
phone_numbers = [
     "    +38(050)123-32-34",
   "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

#прибираємо зайве
cleaned = [
    "+38" + r if r.startswith("0") else "+" + r
    for r in (re.sub(r"[^\d]", "", p) for p in phone_numbers)
]
unique = dict.fromkeys(cleaned)

#виведення
for n in unique:
    if re.match(r"^\+380\d{9}$", n):
       print(n)