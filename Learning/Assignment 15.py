import random
import string
def password_gen(count):
    while True:
        if count < 8:
            print('Password should be atleast 8 characters long')
            opt = input('want to try again (y/n) : \n')
            if opt != 'y':
                break
        else:
            break
    word = []
    password = []
    for i in range(1, count+1):
        word = [random.choice(string.ascii_lowercase), random.choice(string.ascii_uppercase), random.choice(string.digits)]
        password.append(random.choice(word))
    print("".join(password[::]))



count = int(input('length of the password you want : \n'))
password_gen(count)