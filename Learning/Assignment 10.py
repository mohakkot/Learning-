def list_compare(list1,list2):
    new_list = []
    for i in list1:
        if i in list2 and i not in new_list:
                new_list.append(i)
                continue
    print(new_list)


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
list_compare(a, b)
result = [i for i in set(a) if i in b]
print(result)
