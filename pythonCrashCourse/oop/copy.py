def makeCopy(list):
    new_list = []
    _makeCopy(list, new_list, 0)
    return new_list


def _makeCopy(original_list, new_list, current_index):
    if current_index == len(original_list):
        return
    # adding element at index current_index to new list
    new_list.append(original_list[current_index])

    # moving current index to next element in original list
    _makeCopy(original_list, new_list, current_index + 1)


lst = [1, 2, 3]
copy = makeCopy(lst)
print(copy is lst)
print(copy == lst)
