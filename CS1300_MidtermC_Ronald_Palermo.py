# 03/05/2026
# 9:30 - 11:30
# Zollner 116 -- Computer Science Lab
#######################################################
# Problem 1: Distance Calculator

distance = float(input("Enter distance: "))
unit = input("Enter unit (km/mi): ").lower()

if unit == "km":
    miles = distance * 0.621371
    print(f"{distance:.2f} km = {miles:.2f} mi")

elif unit == "mi":
    km = distance * 1.60934
    print(f"{distance:.2f} mi = {km:.2f} km")

else:
    print("Invalid unit.")
    
#######################################################
#Problem 2: Text Statistics Tool

# Text Statistics Tool

sentence = input("Enter a sentence: ")

total_characters = len(sentence)

words = sentence.split()
total_words = len(words)

vowels = "aeiou"
vowel_count = 0
consonant_count = 0

for i in sentence.lower():
    if i.isalpha():
        if i in vowels:
            vowel_count += 1
        else:
            consonant_count += 1

non_space_characters = len(sentence.replace(" ", ""))
average_word_length = non_space_characters / total_words

longest_word = ""
for word in words:
    if len(word) > len(longest_word):
        longest_word = word

print("Total characters:", total_characters)
print("Total words:", total_words)
print("Vowels:", vowel_count)
print("Consonants:", consonant_count)
print(f"Average word length: {average_word_length:.2f}")
print("Longest word:", longest_word)
