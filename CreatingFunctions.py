
# Creating Functions

# In this exercise, we will review functions, as they are key building blocks of object-oriented programs.



# Create a function average_numbers(), which takes a list num_list as input and then returns avg as output.
# Inside the function, create a variable, avg, that takes the average of all the numbers in the list.
# Call the average_numbers function on the list [1, 2, 3, 4, 5, 6] and assign the output to the variable my_avg.
# Print out my_avg.


# Create function that returns the average of an integer list
def average_numbers(num_list):
    avg = sum(num_list)/float(len(num_list))  # divide by length of list
    return avg

# Take the average of a list: my_avg
my_avg = average_numbers([1, 2, 3, 4, 5, 6])

# Print out my_avg
print(my_avg)
# 3.5


# Creating a complex data type
# In this exercise, we'll take a closer look at the flexibility of the list data type, by creating a list of lists.

# In Python, lists usually look like our list example below, and can be made up of either simple strings, integers,
# or a combination of both.

list = [1, 2]

# In creating a list of lists, we're building up to the concept of a NumPy array.


# Create a variable called matrix, and assign it the value of a list.
# Within the matrix list, include two additional lists: [1,2,3,4] and [5,6,7,8].
# Print the matrix list.

matrix = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(matrix)