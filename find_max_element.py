def find_max_element(lst):
    if not lst:
        return None
    max_element = lst[0]
    for num in lst:
        if num > max_element:
            max_element = num
    return max_element

# Prompt the user to enter a list of numbers
input_list = input("Enter a list of numbers separated by spaces: ")
numbers = input_list.split()

# Convert the input list to integers
numbers = [int(num) for num in numbers]

# Find the maximum element
max_num = find_max_element(numbers)

# Display the result
print(f"The maximum element in the list is: {max_num}")
