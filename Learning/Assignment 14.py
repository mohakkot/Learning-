def reverse_string(phrase):
    print(phrase)
    str_split = phrase.split()
    print(str_split)
    result = str_split[::-1]
    return(' '.join(result))

def rev_str(phrase):
    return ' '.join(phrase.split()[::-1])

phrase = str(input('Please enter a string:\n'))
rev = reverse_string(phrase)
print(rev)
rev = rev_str(phrase)
print(rev)