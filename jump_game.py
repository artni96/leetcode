test_data_1 = [2, 3, 1, 2, 4]
test_data_2 = [1, 1, 1, 2, 1]


def jump_game(input_data):
    current_index = 0
    while current_index <= len(input_data) - 1:
        input_data[current_index]
        current_index += input_data[current_index]
        if current_index == len(input_data) - 1:
            return True
    return False


print(jump_game(test_data_2))
