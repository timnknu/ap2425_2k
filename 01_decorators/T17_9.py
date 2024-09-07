max_N = 10

# option 1
# storage = []
# for i in range(max_N+1):
#     storage.append(None)

# option 2
storage = [None]*(max_N+1)

def original_func(n):
    res = n**2
    return res

def cached_func(n):
    #