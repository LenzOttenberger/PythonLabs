def merge_sorted_list(list1, list2):
    i = 0
    j = 0
    merged_list = []
    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        elif list1[i] >= list2[j]:
            merged_list.append(list2[j])
            j += 1

    while i < len(list1):
        merged_list.append(list1[i])
        i += 1

    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
    return merged_list


print(merge_sorted_list([1, 2, 5, 6, 9], [3, 4, 10, 11]))
