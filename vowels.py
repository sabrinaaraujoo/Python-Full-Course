word = input("Enter a random word: ")
wordLength = len(word)

vowels = ["a", "e", "i", "o", "u"]
numVowels = 0

for x in range(0, wordLength, 1):
    for i in range(0, len(vowels), 1):
        
        if vowels[i] == word[x]:
            numVowels += 1
            vowels.remove(vowels[i])
            break
    pass

print(f"The word {word} has {numVowels} unique vowel(s)")
