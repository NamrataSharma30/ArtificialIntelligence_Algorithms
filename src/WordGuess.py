import random


def main():
    secret_word = get_word()
    length = len(secret_word)
    play_game(secret_word, length)


def play_game(secret_word, length):
    st = ""
    initial_guesses = 8
    for i in range(length):
        st += "- "
    while initial_guesses > 0:
        print("The word now looks like this: " + str(st))
        print("You have " + str(initial_guesses) + " guesses left")
        s = input("Type a single letter here, then press enter: ")
        s_upper = s.upper()
        if s_upper.isalpha() and len(s_upper) == 1:
            for ch in secret_word:
                if ch == s_upper:
                    temp = secret_word
                    ch_index = temp.find(ch)
                    temp = temp.replace(temp[ch_index], ' ')
                    print("You got it right!")
                    st = str(st[:ch_index]) + s_upper + str(st[ch_index + 1:])
                    st = st[:-1]
            initial_guesses -= 1
            if st == secret_word:
                print("You guessed the word! It is - ", st)
                break
        else:
            print("Guess should only be a single character.")
    else:
        print("Oh no!! Better luck next time!")
        initial_guesses -= 1


def get_word():
    words = ['DAYLIGHT', 'DOG', 'SAD', 'CLOTHING']
    return random.choice(words)


if __name__ == '__main__':
    main()
