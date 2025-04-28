def t302_matrix_process(M):
    "Ця функція приймає M -- матрицю як список списків"
    sum_elements = 0
    min_elem = 0
    max_elem = 0
    for row in M:
        for el in row:
            sum_elements += el
            if el < min_elem:
                min_elem = el
            if el > max_elem:
                max_elem = el
    return sum_elements, min_elem, max_elem
