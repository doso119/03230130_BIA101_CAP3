# https://github.com/doso119/03230130_BIA101_CAP3
# Kinley Tshering
# 03230130
# BBI'A'

# calculating line wise
def extract_and_sum(filename): # def extract_and_sum(filename):
    total_sum = 0
    with open(filename, 'r') as file: # read txt file 
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            first_digit = ''
            last_digit = ''

            # Finding the first digit
            for char in line:
                if char.isdigit():
                    first_digit = char # Store the first digit found
                    break

            # Finding the last digit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char # Store the last digit found
                    break

            if first_digit and last_digit: # If both first and last digits are found, combine them into a two-digit number and add to total_sum
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
                # when two digits are found
                print(f"Line {line_number}: {line} | Two-digit number: {two_digit_number} | Running sum: {total_sum}")
            else:# Print information about the line when no two-digit number is found
                print(f"Line {line_number}: {line} | No two-digit number found")

    return total_sum # The total sum of two-digit numbers found in the file.

# Example usage
filename = '130.txt'
result = extract_and_sum(filename) # Call the function to extract and sum two-digit numbers
print(f"\nThe final sum of the two-digit numbers is: {result}")
    
    
