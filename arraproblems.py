# Given array of elements, find the sum of them
from audioop import reverse


def sum_array(array1):
    sum = 0
    for i in range(0, len(array1)):
        sum = sum + array1[i]
    print(sum)


arr1 = [12, 3, 4, 15]

sum_array(arr1)


# sum in another method:

def summing(arr):
    return sum(arr)


# ans = summing(arr)
# print(" Sum of the array is: ", ans)

# inbuilt function
# print('Sum of the array is: ', sum(arr))


# Python program to find the largest element in the array:

def largest_element(array2):
    for i in range(0, len(array2)):
        return max(array2)


# print('The largest element is: ' + str(largest_element(arr)))


# another method:
def largest(array2):
    big = array2[0]
    for i in range(0, len(array2)):
        if big < array2[i]:
            big = array2[i]
    return print('The largest number: ', big)


# largest(arr)


# Array rotation. Write a function rotate (ar[], d, n) that rotates arr[] of size n by d elements.
# array of [1,2,3,4,5,6,7] will be [3,4,5,6,7,1,2]; d = 2, n = 7
# Pseudo code: > store d elements in a temp array, shift rest of the array, store back d elements


def arr_rot_mannual(array5):
    temp = []
    for i in range(0, 2):
        temp.append(array5[i])
    temp

    temp1 = []

    for i in range(2, len(array5)):
        temp1.append(array5[i])
    temp1

    rotated_list = []
    for i in range(0, len(temp1)):
        rotated_list.append(temp1[i])
    for i in range(0, len(temp)):
        rotated_list.append(temp[i])

    return print('Rotated list ', rotated_list)


arr_rotation = [1, 2, 3, 4, 5, 6, 7]
print('The original array: ', arr_rotation)
arr_rot_mannual(arr_rotation)
arr_rotation.reverse()
# That means function reverse doesn't return anything.
print("print arr_rotation: ", arr_rotation)


# Method 2: Rotate one by one.


def leftRotateByOne(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


# print("arr before rotation", arr)

def left_rotate(arr, n, d):
    for i in range(d):
        leftRotateByOne(arr, n)


def PrintArray(arr):
    print("Print arr", arr)


left_rotate(arr_rotation, 7, 2)
PrintArray(arr_rotation)
print("arr_rotation Before applying following codes", arr_rotation)

"""find summation of two elements of a list whether they match a given number!"""


def findNumber(target_num):
    arr_rotation = [1, 2, 3, 4, 5, 6, 7]

    for i in range(0, len(arr_rotation)):

        for j in range(i, len(arr_rotation)):

            if arr_rotation[i] + arr_rotation[j] == target_num:
                print(arr_rotation[i], arr_rotation[j])

        """else:
                print("No match found") """


findNumber(8)
print('End of find numbers')
# Array reversal another way:
# Function to reverse array from index start to end
arr_rotation = [1, 2, 3, 4, 5, 6, 7, 8]
print("beginning of new arr_rotation:", arr_rotation)


def reverseArray(arr, start, end):
    print(len(arr))
    while (start < end):
        print(start, end)
        print('Beginning of the while loop')
        temp = arr[start]
        arr[start] = arr[end]
        arr[end] = temp
        start = start + 1
        end = end - 1
        print(start, end)
        print(arr_rotation)


reverseArray(arr_rotation, 0, 7)
