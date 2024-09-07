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

def cached_func(n):
    if storage[n] is None:
        res = original_func(n)
        storage[n] = res
        return res
    else:
        return storage[n]

print('--------')
print(cached_func(2))
print('--------')
print(cached_func(3))
print('--------')
print(cached_func(4))
print('--------')
print(cached_func(2))
print('--------')
print(cached_func(4))
print('--------')