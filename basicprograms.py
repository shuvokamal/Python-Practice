# add two numbers
import math


def addnumbers(number1, number2):
    result = number1 + number2
    print("the summation of {0} and {1} = {2}".format(number1, number2, result))


# addnumbers(number1=int(input('Enter the first number')), number2=int(input('Enter the second number')))

# Find Factorial of a number

def factorial(num):
    if num == 1 or num == 0:
        return 1
    else:
        return num * factorial(num - 1)


# n = int(input("What number's factorial u wanna know dude?"))

# print(factorial(n))

# calculate simple interest

def simpleinterest(p, n, r):
    return print('interest = ' + str((p * n * r) / 100))


simpleinterest(3000, 7, 1)


# calculate compound interest

def compoundinterest(p, r, t):
    return print('compound interest: ' + str(p * (pow((1 + r / 100), t))))


compoundinterest(1200, 5.5, 2)


# Accumulate through recursion

def accumulate(n):
    if n == 1:
        return 1
    else:
        return n + accumulate(n - 1)


print(accumulate(5))


# calculate power using recursion

def power(base, exp):
    if exp == 1:
        return base
    if exp != 1:
        return base * power(base, exp - 1)


calc = power(2, 3)
print(calc)


# sum the items of a list recursively:

def list_sum_recursive(input_list):
    if input_list == []:
        return 0
    else:
        head = input_list[0]
        rest_of_list = input_list[1:]
        return head + list_sum_recursive(rest_of_list)


list = list_sum_recursive([1, 2, 3, 4])
print(list)

# fibonacci series with recursion:
print("Fibonacci problems, finding nth fibonacci number: ")


def calculatefib(n):
    # print("Calculating F ", "(", n , ")", sep= "", end=", ")
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return calculatefib(n - 1) + calculatefib(n - 2)


print(calculatefib(8))


# fibonacci by dynamic programming:
def fibonacci(n):
    a = 0
    b = 1
    if n < 0:
        print("Incorrect Input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            c = a + b
            a = b
            b = c
        return c


print(fibonacci(8))


# check if a number is a fibonacci number:
# interesting fact about fibonacci is, the (5*n*n+4) or (5*n*n-4) one or both is perfect square for a fibonacci number
# So we need two functions here, one to check if a number is a perfect square. Another function judge the condition.
def is_perfect_square(x):
    s = int(math.sqrt(x))
    return s * s == x


def is_fibonacci(n):
    a = 5 * n * n + 4
    b = 5 * n * n - 4
    if is_perfect_square(a) == True or is_perfect_square(b) == True:
        return True
    else:
        False


print("Is fibonacci:")
print(is_fibonacci(13))


# function to calculate the digits of the provided number:

def order(x):
    n = 0
    while x != 0:
        n = n + 1
        x = x // 10
    return n


print("Number of digits: " + str(order(1567394)))


# Now, to calculate the armstrong number, we will use power() and order() function that we created before.
def isArmstrong(x):
    n = order(x)
    temp = x
    sum1 = 0
    while temp != 0:
        r = temp % 10
        sum1 += pow(r, n)
        temp = temp // 10
    return sum1 == x


# x = int(input("Enter a number: "))
# print(isArmstrong(x))

# find area of a circle


def find_area(r):
    area = math.pi * (pow(r, 2))
    print("area= " + str(area))


find_area(5)


# Find prime numbers in a given interval:

def find_prime():
    a = int(input('What is the lower interval?'))
    b = int(input('What is the upper interval?'))
    empty_list = []

    for val in range(a, b + 1):
        if val > 1:
            for n in range(2, val):
                if val % n == 0:
                    break
            else:
                empty_list.append(val)
    print(empty_list)


# print(find_prime())

# function to check if a number is a prime number
def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True


# print(is_prime(18))

# Program to print ASCII value of a character:
# find the ASCII value of G. We can find it using ord() function

c = 'g'
print("The ASCII value of " + c + " is ", ord(c))


# Find the sum of squares of first n natural numbers

def sum_natural_numbers(N):
    if N == 1:
        return 1
    else:
        return pow(N, 2) + (sum_natural_numbers(N - 1))


X = 5
print('sum:' + str(sum_natural_numbers(X)))

# some natural number with the while loop:

def sum_digits(n):
    sum = 0
    for i in range(1, n+1):
        sum = sum + (i*i)
    return sum

print(sum_digits(5))

# Find cube sum for n natural numbers:
def sum_natural_numbers(N):
    if N == 1:
        return 1
    else:
        return pow(N, 3) + (sum_natural_numbers(N - 1))


X = 3
print('sum:' + str(sum_natural_numbers(X)))

