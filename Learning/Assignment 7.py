def list_even(list):
    new_list = [b for b in list if b % 2 == 0]
    print(new_list)


a = [1, 4, 9, 16, 25,36, 49,64, 81, 100]
list_even(a)