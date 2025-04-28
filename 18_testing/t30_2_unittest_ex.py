def t302_matrix_process(M):
    "Ця функція приймає M -- матрицю як список списків"
    sum_elements = 0
    min_elem = None
    max_elem = None
    for row in M:
        for el in row:
            sum_elements += el
            if min_elem is None or el < min_elem:
                min_elem = el
            if max_elem is None or el > max_elem:
                max_elem = el
    return sum_elements, min_elem, max_elem
