import unittest


def fxyz(a):
    """
    >>> fxyz(1)
    2
    >>> fxyz(2)
    3
    """
    global b
    try:
        #print(b)
        a = b
    except:
        #print('b is not defined')
        pass
    #b = a
    return a + 1

if __name__ == "__main__":
    #import doctest
    #doctest.testmod()
    #print('OK')
    print(fxyz(1))