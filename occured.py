word = "Hello"
letter_count = {letter: word.count(letter) for letter in set(word)}
print(letter_count)
