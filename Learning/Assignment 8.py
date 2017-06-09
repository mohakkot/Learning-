def game(inp1, inp2):
    rules = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
    if inp1 not in rules or inp2 not in rules:
        print('invalid choice: ')
        return
    if inp1 == inp2:
        print('Its a tie')
    elif rules[inp1] == inp2:
        print('Player 1 wins')
    else:
        print('Player 2 wins')

while True:
    a = str(input('Please enter "rock, paper or scissors" :'))
    b = str(input('Please enter "rock, paper or scissors" :'))
    game(a, b)
    opt=str(input('want to play again (y/n): '))
    if opt != 'y':
       break
