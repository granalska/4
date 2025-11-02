import re

def generator_numbers(text):
    for num in re.findall(r'\b\d+(?:\.\d+)?\b', text):
        yield float(num)

def sum_profit(text, func):
    return sum(func(text))

text = "Загальний дохід працівника складається з 1000.01, 27.45 i 324.00 доларів."
print("Загальний дохід:", sum_profit(text, generator_numbers))
