def Ncacher(max_N = 10):
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
    #
    return cacher

@Ncacher(20)  # діє як original_func = cacher(original_func),
# де cacher = Ncacher(10)
def original_func(n):
    print("Hi, I'm original function, with n =", n)
    res = n**2
    return res


print('--------')
print(original_func(2))
print('--------')
print(original_func(3))
print('--------')
print(original_func(3))
print('--------')
