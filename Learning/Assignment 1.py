class Character_input:


    def input(self):
        print('Please enter your name: ')
        name= input()
        while True:
            try:
                print('Please enter your age: ')
                age = int(input())
                break
            except:
                print('Please enter integer Number: ')
        self.age_calculate(age, name)


    def  age_calculate(self, age, name):
        newage = (2016 - age) + 100
        data = 'Dear ' + str(name) + ' your age will be 100 years in the year: ' + str(newage)
        print(data)
        self.print_multi(data)


    def print_multi(self, data):
        num = int(input('Please enter any number'))
        for i in range(0, num):
            print(data + '\n')

ch = Character_input()
ch.input()