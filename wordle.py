from config import ALPHABET, GREY, GREEN, YELLOW

def load_dict(file_name):
    with open(file_name) as file:
        words = file.readlines()
    return [word.strip().upper() for word in words]

def determine_unguessed_letters(guesses):
    guessed_letters = "".join(guesses)
    return "".join(letter for letter in ALPHABET if letter not in guessed_letters)

def determine_color(guess, j, answer):
    letter = guess[j]
    if letter == answer[j]:
        return GREEN
    elif letter in answer:
        n_target = answer.count(letter)
        n_correct = sum(1 for i in range(5) if guess[i] == letter and letter == answer[i])
        n_occurance = sum(1 for i in range(j + 1) if guess[i] == letter)
        if n_target - n_correct - n_occurance >= 0:
            return YELLOW
    return GREY
