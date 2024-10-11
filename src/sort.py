arr = [40, 4, 20, 10, 30, 6, 10]

# insertion sort with logging:
for i in range(1, len(arr)):
    a_i = arr[i]
    j = i - 1
    # Логирование сравнения элементов, как это было в selection sort
    while j >= 0:
        print("comparing {} and {}".format(arr[j], a_i))
        if arr[j] > a_i:
            arr[j + 1] = arr[j]
        else:
            break
        j -= 1
    arr[j + 1] = a_i

print(arr)
