#Write a Python function called sum_even_odd that takes a list of integers
#as input and returns a tuple containing the sum of even numbers and the 
#sum of odd numbers in the list.

sum_even_odd = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_sum = sum(number for number in sum_even_odd if number % 2 == 0)
odd_sum = sum(number for number in sum_even_odd if number % 2 != 0)

solution = (even_sum, odd_sum)

print(solution)

