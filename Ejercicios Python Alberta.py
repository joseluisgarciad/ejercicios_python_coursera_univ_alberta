from math import sin, radians
grados = int(input("Enter an angle in degrees >"))
radianes = radians(grados)
print("The sin of", grados, "degrees is", sin(radianes))


#  Write a Python program that asks the user to input two numbers and finds the max of those number
#  when they are raised to the power of each other.
#  Display three numbers in your answer, the first number raised to the power of the second, the second number
#  raised to the power of the first, and then the maximum of these two computed values, each on one line.

a=int(input('Enter an integer >'))
b=int(input('Enter an integer >'))
print(a, 'to the power of', b, 'is', a**b)
print(b, 'to the power of', a, 'is', b**a)
print('the max of', a**b, 'and', b**a, 'is', max(a**b,b**a))