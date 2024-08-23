def amount_of_options(steps):
    if steps == 1:
        return 1
    if steps == 2:
        return 2
    if steps > 2:
        result = [1, 2]
        for i in range(3, steps):
            new_result = int(result[-1] + result[-2])
            result[-2] = result[-1]
            result[-1] = new_result
            i += 1
        return int(result[-1] + result[-2])


print(amount_of_options(8))
# print(amount_of_options(8))
