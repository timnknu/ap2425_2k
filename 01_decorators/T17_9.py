# Модифікації (на вибір):
# 1. Зберігати позначку про зроблений раніше виклик
#    оригінальної функції окремо від результату, який вона повертала
# 2. Реалізувати механізм кешування для функції, аргумент
#    якої - ціле число в межах -max_N ... +max_N
# 3. Замість списку використати словник як "сховище" для
#    зберігання результатів

max_N = 10
def cacher(some_function):
    storage = [None] * (max_N + 1)
    def cached_func(n):
        if storage[n] is None:
            res = some_function(n)
            storage[n] = res
            return res
        else:
            return storage[n]
    #
    return cached_func


@cacher  # original_func = cacher(original_func)
def original_func(n):
    print("Hi, I'm original function, with n =", n)
    res = n**2
    return res

@cacher  # alternative_func = cacher(alternative_func)
def alternative_func(n):
    print("Hi, I'm alternative function, with n =", n)
    res = -n
    return res


print('--------')
print(original_func(2))
print('--------')
print(original_func(3))
print('--------')
print(alternative_func(3))
print('--------')
