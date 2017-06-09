def find_divisor(num):
    div_list= []
    for a in range(2, num):
        if num % a == 0:
            div_list.append(a)
    if div_list == []:
        print('the number is prime')
    else:
        print(div_list)

num = int(input('Please provide a number: \n'))
find_divisor(num)