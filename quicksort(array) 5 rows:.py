def quicksort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
        left = [x for x in array[1:] if x < pivot]
        middle = [x for x in array[1:] if x == pivot]
        right = [x for x in array[1:] if x > pivot]

        return quicksort(left) + middle + quicksort(right)

# Пример использования функции
data = [[1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]]

result = quicksort(data)
print("Отсортированные данные:")
for row in result:
    print(row)
