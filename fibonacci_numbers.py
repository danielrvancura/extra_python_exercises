# Fibonacci numbers   0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

# Implment a program that will print a LIST of fibonacci numbers to a specified length.

# Example: fibonacci(10)
# input: number  (desired length of array)
# output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34] - the first 10 numbers of the fibonacci sequence

# Hint:
# You may start your array like this:
# list = [0, 1]


# *** your code here ***

number = 10

num1 = 0
num2 = 1
count = 0

if number == 1:
   print("Fibonacci sequence up to",number,":")
   print(num1)
else:
   print("Fibonacci sequence up to",number,":")
   while count < number:
       print(num1, end=' , ')
       num3 = n1 + n2
       num1 = num2
       num2 = num3
       count += 1
