import math

def list_compare(list1,list2):
    new_list = []
    for i in list1:
        if i in list2:
                new_list.append(i)
                continue
    print(new_list)

a = range(1, 10)
b = range(5, 20)
list_compare(a, b)

