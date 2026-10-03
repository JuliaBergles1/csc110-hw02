# Julia Bergles
# Task 1.1:
#  Complete the function "read_two_ints" below:
def read_two_ints():
    """Read two integers from the user and return them."""
    # Get the first number and convert it to an integer
    x = input("give me x: ")
    x = int(x)
    # Get the second number from the user
    y = input("give me y: ")
    y = int(y)
    return x,y
    
    

# Task 2.1:
#  Complete the function "compute_multadd" below:
def compute_multadd(a, b):
    """Calculate and print the multiplication and addition results."""
    mult_result = a * b     # Calculate the product of the two numbers
    print("mult result:", mult_result)
    add_result = a + b  # Calculate the sum of the two numbers
    print("add result:", add_result)
    # Return the multiplication result divided by the addition result
    return mult_result / add_result 
    

# Task 3.1:
#  Complete the function "print_fancy" below:
def print_fancy(a, b, ab_multadd):
    """Print the inputs and multadd result in a fancy format."""
    # Print the results in the required format
    print("****************")
    print("RESULTS:")
    print("first number:", a)
    print("second number:", b)
    print("multadd result:", ab_multadd)
    print("================")

def main ():
    """Run the main program."""
     # Task 1.2:
     # Read the two numbers from the user
    x, y = read_two_ints()
    
    # Task 2.2:
   # Calculate the multadd result using x and y
    xy_multadd = compute_multadd(x, y)

    # Task 3.2:
 # Display the results in the right format
    print_fancy(x, y, xy_multadd)
    
    # Do not modify this final print statement
    print("The End")

# Do not modify these two lines
if __name__ == "__main__":
    main()
