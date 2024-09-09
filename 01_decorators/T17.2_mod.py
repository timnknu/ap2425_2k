# 17.2 (модифікована)
# Побудувати декоратор, який перевіряє результат функції (яка повертає число), так, щоб цей результат y був у межах заданих границь a, b (a⩽y⩽b), і створює виключення, якщо результат не лежить у вказаних межах.
# Виконати перевірку роботи декоратора для деякої функції f.

def res_checker(a, b):
    def checker(some_function):
        def checkable_func(*arg, **kwargs):
            res = some_function(*arg, **kwargs)
            if res <= b and res >=a:
                return res
            else:
                raise Exception("wrong range")
        #
        return checkable_func
    #
    return checker

@res_checker(0, 5)
def func(x):
    return x - 10

print(func(14)) # працює
print(func(0))  # ініціює виключення