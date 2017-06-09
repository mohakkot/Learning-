from random import randrange

def guess(num, chance):
    value = randrange(1, 9)
    if num > value:
        chance += 1
        if num - value > 3:
            print(' your guess was too high')
        elif num - value == 0:
            print(' you guessed it right')
            print('You took only ', chance, ' tries')
        else:
            print('you were close')
    else:
        chance += 1
        if value -  num > 3:
            print(' your guess was too low')
        elif num - value == 0:
            print (' you guessed it right')
            print('You took only ', chance, ' tries')
        else:
            print('you were close')
    print('the number was: ', value)
    return(chance)

chance = 0
while True:
    num = int(input('please enter a number:\n'))
    chance = guess(num, chance)
    opt = str(input('Want to continue ? (y/n): \n'))
    if opt!= 'y':
        break