print('Hello, world')
print('Phython3 cool')

 #FizzBuzz method 1 
 # -----------------#
# for num in range(1,21):
#         string = ""
#         if num % 3 == 0:
#             string = string + "Fizz"
#         if num % 5 == 0:
#             string = string + "Buzz"
#         if num % 5 != 0 and num & 3 != 0:
#             string = string + str(num)
#         print(string)

# FizzBuzz method 2 
#-------------------
# for num in range(1,21):
#     if num % 3 == 0 and num % 5 == 0:
#         print('FizzBuzz')
#     elif num % 3 == 0:
#         print('Fizz')
#     elif num % 5 == 0:
#         print('Buzz')
#     else:
#         print(num)


# Playing with variable decelerations 
#------------------------------------
# a = 'my'
# b = 'name'
# c = 'is' 
# d = 'matt'

# a,b,c,d = 'my' , 'name' , 'is' , 'glen'
# print(a,b,c,d)


# Reverse a string 
#----------------- 
txt = "this is so cool! I can't believe I can reverse the string this easily"[::-1]
print(txt)