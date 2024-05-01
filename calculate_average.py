def calculate_average(number_list: list):
    if len(number_list) == 0:
        return "Empty list."
    else:
        return sum(number_list) / len(number_list)
    
my_list = [1, 2, 3, 4, 5]

print(calculate_average(my_list))


