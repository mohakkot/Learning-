def palindrome(phrase):
    rev_phrase = rev_string(phrase)
    if len(phrase) != len(rev_phrase):
        print('Not a palindrome')
        pass
    if phrase == rev_phrase:
            print(' String is a palindrome')
    else:
        print('String is not a palindrome')


def rev_string(string):
    return string[::-1]


a = str(input('Please enter a string :\n'))
palindrome(a)