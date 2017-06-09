def fibonacci(ran):
    a, b = 1, 1
    for i in range(1, ran+1):
        print(a)
        c = a+b
        a = b
        b = c


ran = int(input('Please enter the count of  fibonacci to generate: \n'))
fibonacci(ran)