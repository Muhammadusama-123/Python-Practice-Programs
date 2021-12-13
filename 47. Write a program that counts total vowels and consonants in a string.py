'''
Casefold is basically method that turns the string into lower case format.
'''

text = input('Enter string: ').casefold()
vowel = 0
consonant = 0
for i in range(0, len(text)):
    if text[i] != '':
        if text[i] == 'a' or text[i] == 'e' or text[i] == 'i' or text[i] == 'o' or text[i] == 'u':
            vowel += 1
        else:
            consonant += 1
print('Total Vowels =', vowel)
print('Total Consonant\'s =', consonant)
