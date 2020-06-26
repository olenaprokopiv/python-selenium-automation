#Sum of 3 modifiedhttp://mp3tales.info/
#Homework: Rewrite a program with any number of digits.
#Instead of  3 digits, you should sum digits up from n digits number,
#Where  User enters n manually. n > 0

# numstr = input('Input more then three digits: ')
# sum = 0
# for c in numstr:
#     sum += int(c)
# print(sum)


#Find max number from 3 values, entered manually from a keyboard

# val_1 = int(input('Enter value 1: '))
# val_2 = int(input('Enter value 2: '))
# val_3 = int(input('Enter value 3: '))
# max = val_1
# if val_2 > max:
#     max = val_2
# if val_3 > max:
#     max = val_3
# print(max)

#Count odd and even numbers.  Count odd and even digits of the whole number. E.g,
# if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5)

# num = input('Enter number: ')
# even = 0
# odd = 0
# for c in num:
#     if int(c) % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(f'even', even,  '\nodd', odd)

#Algoritm 2

#Zeros not for Heros
# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

# def ending_zeros(Num):
#     while Num % 10 == 0:
#            Num = int(Num) /10
#     return int(Num)
#
# n = 1050
# N = ending_zeros(n)
# print(N)

#Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

# def sum_of_digits(n):
#     sum = 0
#     while n > 0:
#         d = int(n) % 10
#         sum += d
#         n = n/10
#     if sum < 10:
#         return sum
#     else:
#         return sum_of_digits(sum)
#
# s = 493193
# S = sum_of_digits(s)
# print(S)




