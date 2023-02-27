max_digits = int(input("Enter the maximum number of digits to consider: "))
if max_digits < 2:
    print("The number should have at least two digits.")
else:
    
# variable to keep track of valid numbers
 count = 0

# iterate through all possible two or more digit numbers
 for num in range(10, 10 ** max_digits):
     digits = [int(d) for d in str(num)] # convert number to list of digits
     if digits == sorted(digits): # check if digits are sorted in ascending order
        count += 1

 # print the number of valid numbers found
 
 print("The number of valid numbers found is:", count)
