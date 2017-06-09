def prime(num):
    if num == 2 or num == 3:
        print ('The number is prime')
        return
    for i in range(2, (int((num/2))+1)):
        if num % i == 0:
            print('The number is not prime')
            return
    print('The number is prime')

num =int(input('Please enter a number: \n'))
prime(num)