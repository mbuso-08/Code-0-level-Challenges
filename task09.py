def vowel_function(text):
    vowels = "AEIOUaeiou" 
    lis = [letter for letter in text if letter in vowels]
    print(", ".join(lis))

vowel_function("Umuzi")