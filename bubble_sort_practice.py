def bubble_sort(input_list):
    swapped = True
    while swapped is True:
        last_index = len(input_list) - 1
        swapped = False
        for i in range(last_index):
            if input_list[i] > input_list[i + 1]:
                input_list[i], input_list[i + 1] = input_list[i + 1], input_list[i]
                swapped = True
        last_index -= 1
    return input_list


test_data = [6, 5, 3, 1, 8, 7, 2, 4]
print(bubble_sort(test_data))
