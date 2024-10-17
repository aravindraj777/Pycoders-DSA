arr = [7, 3, 8, 36, 7, 35, 8, 4, 5]


def insertion_sort(array):
    n = len(array)
    for current_index in range(1, n):
        current_element = array[current_index]
        previous_index = current_index - 1

        while previous_index >= 0 and current_element < array[previous_index]:
            array[previous_index + 1] = array[previous_index]
            previous_index -= 1

        array[previous_index + 1] = current_element

    print(array)


insertion_sort(arr)
