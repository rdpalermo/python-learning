# Problem 1 ###################################
# Get user input
principal = float(input("Principal: "))
rate = float(input("Rate (%): "))
years = int(input("Years: "))

# Start with the initial balance
balance = principal

# Loop through each year
for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)
    print(f"Year {year}: ${balance:.2f}")

# Calculate total interest earned
interest = balance - principal

# Print total interest
print(f"Total interest earned: ${interest:.2f}")
# Problem 2 #####################################
def caesar_encode(text, shift):
    result = ""

    for ch in text:
        if ch.islower():
            # Shift lowercase letters
            new_char = chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
            result += new_char
        elif ch.isupper():
            # Shift uppercase letters
            new_char = chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
            result += new_char
        else:
            # Keep non-letters the same
            result += ch

    return result


# Tests
print(caesar_encode("Hello, World!", 3))
print(caesar_encode("abc xyz", 2))
print(caesar_encode("Python 3", 5))

# Problem 3 #####################################
def transpose(matrix):
    result = []
    
    # Loop through columns of original matrix
    for col in range(len(matrix[0])):
        new_row = []
        
        # Loop through rows of original matrix
        for row in range(len(matrix)):
            new_row.append(matrix[row][col])
        
        result.append(new_row)
    
    return result
# Tests
m1 = [[1, 2, 3],
      [4, 5, 6]]
print(transpose(m1))
m2 = [[1, 2],
      [3, 4],
      [5, 6]]
print(transpose(m2))
