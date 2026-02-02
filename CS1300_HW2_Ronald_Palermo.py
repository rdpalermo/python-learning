#1
first = input("Enter first name: ").title()
last = input("Enter last name: ").title()
birth_year = int(input("Enter birth year: "))
hobby = input("Enter favorite hobby: ").title()

age = 2026 - birth_year

print("=" * 36)
print("         USER PROFILE CARD")
print("=" * 36)
print(f"Name:    {first} {last}")
print(f"Age:     {age}")
print(f"Hobby:   {hobby}")
print("-" * 36)
print("Thank you for creating your profile!")
print("=" * 36)

#2
sentence = input("Enter a sentence: ")

vowels = "aeiouAEIOU"
vowel_count = sum(1 for i in sentence if i in vowels)

print("\n--- Analysis Results ---")
print(f"Total characters (with spaces):    {len(sentence)}")
print(f"Total characters (without spaces): {len(sentence.replace(' ', ''))}")
print(f"Number of words:                   {len(sentence.split())}")
print(f"Number of vowels:                  {vowel_count}")
print(f"Uppercase version:                 {sentence.upper()}")
print(f"Lowercase version:                 {sentence.lower()}")
print(f"Reversed:                          {sentence[::-1]}")
print(f"Starts with capital:               {sentence[0].isupper()}")
print(f"Ends with punctuation:             {sentence[-1] in '.!?'}")

 #Bonus
text = input("Enter a word or phrase: ").lower().replace(" ", "")

if text == text[::-1]:
        print("Palindrome")
else:
    print("Not a palindrome")
