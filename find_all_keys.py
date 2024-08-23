test_rooms_1 = [[2, 2], [3, 3], [1, 2], [0]]
test_rooms_2 = [[1, 3], [3, 0, 1], [2], [0]]


def find_keys(rooms):
    current_point = rooms[0][0]
    rooms[0].pop(0)
    visited_rooms = [0, ]
    while isinstance(current_point, int) is True:
        try:
            previous_point = current_point
            current_point = rooms[current_point][0]
            visited_rooms.append(previous_point)
            rooms[previous_point].pop(0)
        except Exception:
            if len(set(visited_rooms)) == len(rooms):
                return True
            return False


print(find_keys(test_rooms_1))
print(find_keys(test_rooms_2))
