class Odd_even:

    def input(self):
        print('Please enter a number: ')
        num = int(input())
        self.check(num)

    def check(self, num):
        if num == 0:
            print('zero is neither even nor odd')
        if num % 2 == 0:
            print('Number is even')
        else:
            print('Number is odd')

no = Odd_even()
no.input()