def binary_search(nums: list, target: int) -> int:
    left, right = 0, len(nums)
    while left < right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


def bubble_sort(unsorted_list: list) -> list:
    swapped = True
    last_index = len(unsorted_list) - 1
    while swapped:
        swapped = False
        for i in range(last_index):
            if unsorted_list[i] > unsorted_list[i + 1]:
                unsorted_list[i], unsorted_list[i + 1] = unsorted_list[i + 1], unsorted_list[i]
                swapped = True
        last_index -= 1
    return unsorted_list


def list_superset(list_1, list_2):
    counter = 0
    for outer_i in list_1:
        for inner_i in list_2:
            if outer_i == inner_i:
                counter += 1
    if counter == (len(list_2)) == len(list_1):
        return "Наборы равны"
    elif counter == (len(list_1)):
        return f"Набор {list_2} супермножество."
    elif counter == (len(list_2)):
        return f"Набор {list_1} супермножество."

    return "Супермножество не обнаружено."


list_set_1 = [1, 3, 5, 7]
list_set_2 = [3, 5]
list_set_3 = [5, 3, 7, 1]
list_set_4 = [5, 6]

print(list_superset(list_set_1, list_set_2))
print(list_superset(list_set_2, list_set_3))
print(list_superset(list_set_1, list_set_3))
print(list_superset(list_set_2, list_set_4))