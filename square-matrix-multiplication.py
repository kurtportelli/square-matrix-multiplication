def matrix_mult(a, b):
    size = len(a)
    c = [[0 for i in range(size)] for j in range(size)]
    for i in range(size):
        for j in range(size):
            total = 0
            for index in range(size):
                total += a[i][index] * b[index][j]
            c[i][j] = total
    return c
