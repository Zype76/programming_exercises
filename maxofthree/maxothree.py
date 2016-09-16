#!/usr/bin/python3.4
# Select the max of three numbers

#Prompt the user for three numbers

first_number = input("Please enter a number: ")
second_number = input("Please enter a number: ")
third_number = input("Please enter a number: ")


#Function for sorting and printing the largest number
def maxx(first, second, third):
    three_numbers = [first, second, third]
    maxothree = (sorted(three_numbers))
    print('The largest number is: ', maxothree[-1])
    return maxothree

maxx(first_number, second_number, third_number)
