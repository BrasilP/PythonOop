
# Creating Functions

# In this exercise, we will review functions, as they are key building blocks of object-oriented programs.



# Create a function average_numbers(), which takes a list num_list as input and then returns avg as output.
# Inside the function, create a variable, avg, that takes the average of all the numbers in the list.
# Call the average_numbers function on the list [1, 2, 3, 4, 5, 6] and assign the output to the variable my_avg.
# Print out my_avg.


# Create function that returns the average of an integer list
def average_numbers(num_list):
    avg = sum(num_list)/float(len(num_list)) # divide by length of list
    return avg

# Take the average of a list: my_avg
my_avg = average_numbers([1, 2, 3, 4, 5, 6])

# Print out my_avg
print(my_avg)
# 3.5



