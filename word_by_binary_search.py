def find_element(sorted_list, elem):
    left = 0
    right = len(sorted_list)
    while left < right:
        mid = (left + right) // 2
        if elem == sorted_list[mid]:
            return mid
        if elem > sorted_list[mid]:
            left = mid + 1
        else:
            right = mid


input_data = [
    'алгоритмы', 'будут', 'главным',
    'доводом', 'профессионального', 'разработчика']
print(find_element(input_data, 'будут'))
