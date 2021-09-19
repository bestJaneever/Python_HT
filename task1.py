# Random list creation
import random  # function to generate random numbers

random_numbers = random.sample(range(0, 1000), 100)  # generate 100 random numbers between 0 and 1000
print(random_numbers)  # print in console

# Sorting
for i in range(len(random_numbers) - 1):  # body. in range, we set the amount of times for execution
    for j in range(len(random_numbers) - 1):  # iteration. we take elements from the list and and compare values at positions in range with the neighboring element
        # we use -1 to avoid the error of exceeding the length of the list
        if random_numbers[j] > random_numbers[j + 1]:  # in case j > j+1
            random_numbers[j], random_numbers[j + 1] = random_numbers[j + 1], random_numbers[j]  # numbers must be swapped
print(random_numbers)  # print in console

# Calculate average for even and odd numbers
even_list = []  # create list for even
odd_list = []  # create list for odd
for i in random_numbers:  # i - value from the list
    if i % 2 == 0:  # if the number is divisible by 2 without remainder it go to the even_list
        even_list.append(i)
    else:
        odd_list.append(i)  # if not - to the odd_list
average_even_list = sum(even_list) / len(even_list)  # to find average - divide the amount from the list by the number
average_odd_list = sum(odd_list) / len(odd_list)

print(average_even_list, average_odd_list)  # print in console
