# print('Enter your name')
# x = input()
# print('Hello', x)
# ---------------------------------
# x = int (input('Enter your x :'))
# y = int (input('Enter your y :'))
# z = x + y
# print('sum is :', z)
# ---------------------------------
# my_list = ['sach',100,True]
# print(my_list)
# print(my_list[0]) 
# print(my_list[-3])
# both print values give same output = sach
# ---------------------------------
# you can extend list using append() , list is mutable
# my_list = ['sach',100,True]
# my_list.append(20.3) 
# print(my_list)
# -----------------------------------
# you cannot extend tuple using append() because it is immutable ,but through casting you can
# my_tuple = ('sach',100,True)
# my_list = list(my_tuple)
# my_list.append(20.3) 
# print(my_list )
# -----------------------------------
# a = 130
# b = 17
# if a > b :
#   print("a is greater")
# -----------------------------------
# a = 130
# b = 17
# if a > b :
#   print("a is greater")
# elif a < b :
#   print("a is less")
# else :
#   print("invalid")
# -----------------------------------
# x = 1
# while(x < 5):
#    print(x)
#    x = x + 1 
# x++ is not possible with python, output : print 1-4
#-----------------------------------
# for i in range(10):
#   print(i)
# for loop runs until it finds the element, but will print only 0-9
# -----------------------------------
# x = ['SL','UK','AUS','USA']
# i = 0
# while i < len(x):
#   print(x[i])
#   i = i + 1
# -----------------------------------
# for i in range(5,10):
#   print(i)
# 5-10 will print
# -----------------------------------
# for i in range(99):
#   if i % 5 == 0:
#     print(i,"can be divided by 5")
# -----------------------------------
# for i in range(1,10,2):
#   print('attempt :',i,i*'.')
# 3rd arguement in the range will skip one number, output : 1,3,5,7,9
# -----------------------------------
# success = True
# for i in range(3):
#   if success:
#     print("suceesful")
#     break
# if successful then break, do not loop through
# -----------------------------------
# for x in range(5):
#   for y in range(7):
#     print("({0},{1})".format(x,y))
# print x,y coordinates
# ------------------------------------
# for x in [1,2,3,4]:
#   print(x)
#printing list using for loop
# ------------------------------------
# count = 0
# for i in range(1,1000):
#   if i%7 == 0:
#     count = count + 1
#     print(i)
# print('we have {0} number which divded by 7'.format(count))
# ------------------------------------
# def add(x,y):
#   z = x + y
#   print(z)
# add(3,5)  
# ------------------------------------