def vowel_function(text):
    vowels = ("AEIOUaeiou") 
    lis = list()
    for letter in text:
        l = letter.lower()
        if ( l in vowels ) and (l not in lis ):
            lis.append(l)
    print(", ".join(lis))

vowel_function("Umuzi")