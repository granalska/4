def caching_fibonacci():
    cache = {}  #створюємо порожній словник 

    def fibonacci(n):
        #базa
        if n <= 0:
            return 0
        elif n == 1:
            return 1

        if n in cache:
            return cache[n]

        cache[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cache[n]

    # повертаємо внутрішню функцію fibonacci
    return fibonacci