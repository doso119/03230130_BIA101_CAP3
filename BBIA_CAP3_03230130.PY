def extract_and_sum(filename): # def extract_and_sum(filename):
    total_sum = 0
    with open(filename, 'r') as file:
        for line_number, line in enumerate(file, start=1):
            line = line.strip()
            first_digit = ''
            last_digit = ''

            # Find the first digit
            for char in line:
                if char.isdigit():
                    first_digit = char
                    break

            # Find the last digit
            for char in reversed(line):
                if char.isdigit():
                    last_digit = char
                    break

            if first_digit and last_digit:
                two_digit_number = int(first_digit + last_digit)
                total_sum += two_digit_number
                print(f"Line {line_number}: {line} | Two-digit number: {two_digit_number} | Running sum: {total_sum}")
            else:
                print(f"Line {line_number}: {line} | No two-digit number found")

    return total_sum

# Example usage
filename = '130.txt'
result = extract_and_sum(filename)
print(f"\nThe final sum of the two-digit numbers is: {result}")
    