max_N = 10

# option 1
# storage = []
# for i in range(max_N+1):
#     storage.append(None)

# option 2
storage = [None]*(max_N+1)

def original_func(n):
    print("Hi, I'm original function, with n =", n)
    res = n**2
    return res

def cacher(some_function):
    def cached_func(n):
        if storage[n] is None:
            res = some_function(n)
            storage[n] = res
            return res
        else:
            return storage[n]
    #
    return cached_func

smart_f = cacher(original_func) # !!!

print('--------')
print(smart_f(2))
print('--------')
print(smart_f(3))
print('--------')
print(smart_f(4))
print('--------')
print(smart_f(2))
print('--------')
print(smart_f(4))
print('--------')