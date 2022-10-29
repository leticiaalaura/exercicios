def run(array):
    sums = []
    for idx, n1 in enumerate(array):
        if n1 % 1 > 0:
            raise Exception('A lista deve conter somente numeros inteiros')
        for n2 in array[idx+1:]:
            result = n1 + n2
            if result in array:
                sums.append(result)
    return list(set(sums))

run(array= [1, 2, 3, 4, 5, 5.1])