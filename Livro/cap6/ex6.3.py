def count(word, your_letter):
    letter_count = 0
    for letter in word:
        if letter == your_letter:
            letter_count = letter_count + 1        
    print letter_count
    return count

while True:

    word = raw_input("Escolha uma palavra: ")
    your_letter = raw_input("Escolha uma letra dessa palavra para contar: ")

    if word == "done" or your_letter == "done": break

    count(word, your_letter)
    continue