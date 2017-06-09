def find_small(a):
    num_list = []
    for num in a:
        if num <= 5:
            num_list.append(num)
    print(num_list)


list1 = [1, 3, 5, 7, 1, 3, 4, 8, 0, 87, 45, 34, 2, 43, 5, 78, 2]
print(list1)
find_small(list1)
