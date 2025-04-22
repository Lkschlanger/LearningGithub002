# The following will have the user write comments and GitHub Co-pilot write code based on the comments

# function that computes the average of a list of numbers
def average(numbers):
    # check if the list is empty
    if not numbers:
        return 0
    # calculate the sum of the numbers
    total = sum(numbers)
    # calculate the average
    avg = total / len(numbers)
    return avg

#What does the len() function do?
# The len() function returns the number of items in an object. For example, if you have a list of numbers, len(numbers) will return the number of elements in that list. (co-pilot's response to the question)

#implement the function using a splitted list from the input of user
def main():
    # get user input
    user_input = input("Enter numbers separated by spaces: ")
    # split the input into a list of strings
    numbers_str = user_input.split()
    # convert the list of strings to a list of floats
    numbers = [float(num) for num in numbers_str]
    # calculate the average
    avg = average(numbers)
    # print the average
    print(f"The average is: {avg}")

    # call the main function
if __name__ == "__main__":
    main()
# The above code defines a function that computes the average of a list of numbers. It also includes a main function that takes user input, splits it into a list of numbers, and calculates the average using the defined function. The result is then printed to the console.