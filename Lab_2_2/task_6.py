def unique_elements(promblem_list, un_list):
    for item in promblem_list:
        if isinstance(item, list):
            unique_elements(item, un_list)
        else:
            if item not in un_list:
                un_list.append(item)
    return un_list


list_a = [1, 2, 3, [4, 3, 1], 5, [6, [7, [10], 8, [9, 2, 3]]]]
un_list = unique_elements(list_a, [])
print(un_list)
