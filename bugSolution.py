def calculate_average(numbers):
    numeric_numbers = [num for num in numbers if isinstance(num, (int, float))]
    if not numeric_numbers:
        return 0
    return sum(numeric_numbers) / len(numeric_numbers)
    #Alternative using a try-except block:
    #try:
        #return sum(numbers) / len(numbers)
    #except TypeError:
        #return 0  #or raise a more descriptive exception