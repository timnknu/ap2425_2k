import doctest

def Hamming_dist(s1, s2):
    """
    Відстанню Хемінга між s1 та s2 називають кількість позицій, у
    яких s1[i] != s2[i]
    >>> Hamming_dist('hello', 'world')
    4

    >>> Hamming_dist('hello', 'w orld')
    6

    >>> Hamming_dist('hello', 'world123')
    7

    >>> Hamming_dist('world123', 'hello')
    7

    >>> Hamming_dist('', 'hello')
    5

    >>> Hamming_dist('', '')
    0

    """
    num_different = 0
    for c1, c2 in zip(s1, s2):
        if c1!=c2:
            num_different += 1
    num_different += abs(len(s1) - len(s2))
    return num_different

if __name__=="__main__":
    doctest.testmod(verbose=2)
