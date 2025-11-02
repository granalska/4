import numpy as np
import time

from functools import lru_cache
def fibonacci(n_terms):
    sqrt_5 = np.sqrt(5)
    alpha = (1 + sqrt_5) / 2
    beta = (1 - sqrt_5) / 2
    n_values = np.arange(n_terms) 
    fib_numbers = (alpha**n_values - beta**n_values) / sqrt_5
    
    return np.round(fib_numbers).astype(int)

@lru_cache(maxsize=128)
def caching_fibonacci(n):
    return fibonacci(n)
    
start_time = time.time()
a=caching_fibonacci(10)
end_time = time.time()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд",a)

start_time = time.time()
a=caching_fibonacci(15)
end_time = time.time()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд",a)

start_time = time.time()
a=caching_fibonacci(10)
end_time = time.time()

execution_time = end_time - start_time
print(f"Час виконання: {execution_time} секунд",a)