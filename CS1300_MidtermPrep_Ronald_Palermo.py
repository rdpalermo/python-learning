# Problem 1: Temperature Converter

# Ask user for temperature
temp = float(input("Enter temperature: "))

# Ask for scale
scale = input("Enter scale (C/F): ")

# Convert scale to uppercase for case sensitivity
scale = scale.upper()

if scale == "C":
    fahrenheit = temp * 9/5 + 32
    print(f"{temp:.1f}°C = {fahrenheit:.1f}°F")

elif scale == "F":
    celsius = (temp - 32) * 5/9
    print(f"{temp:.1f}°F = {celsius:.1f}°C")

else:
    print("Invalid scale.")
    
###############################################################
# Problem 2: String Analyzer

sentence = input("Enter a sentence: ")

total_chars = len(sentence)
uppercase = 0
lowercase = 0
digits = 0
spaces = 0

# Loop through each character
for ch in sentence:
    if ch.isupper():
        uppercase += 1
    elif ch.islower():
        lowercase += 1
    elif ch.isdigit():
        digits += 1
    elif ch == " ":
        spaces += 1

# Print results
print(f"Total characters: {total_chars}")
print(f"Uppercase letters: {uppercase}")
print(f"Lowercase letters: {lowercase}")
print(f"Digits: {digits}")
print(f"Spaces: {spaces}")
print(f"Reversed: {sentence[::-1]}")