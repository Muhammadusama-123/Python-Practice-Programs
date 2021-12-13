# 1st Method:

# text = input('Enter String to find its reverse: ').casefold()
# print('The reverse of a string is',text[-1::-1])

# 2nd method:

# text = 'ram' # 2 se start lega or -1 tak jaiga matlb -1 se ek ziyada matlb 0 tak jaiga
# # or har dafa ek ka decrement hoga.
# for i in range((len(text)-1), -1, -1):
#     print(text[i], end='')

# 3rd method:

text = 'ram'
print(text[-1:-4:-1])