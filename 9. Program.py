"""
Write a program to accept marks of 5 subjects and find total marks and percentage assumimg full marks as
100 in each subject.
"""

markOfsubj1 = int(input('Enter marks of subject#1: '))
markOfsubj2 = int(input('Enter marks of subject#2: '))
markOfsubj3 = int(input('Enter marks of subject#3: '))
markOfsubj4 = int(input('Enter marks of subject#4: '))
markOfsubj5 = int(input('Enter marks of subject#5: '))

totalMarks = markOfsubj1 + markOfsubj2 + markOfsubj3 + markOfsubj4 + markOfsubj5
print('Total marks is', totalMarks)
