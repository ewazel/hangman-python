
### import random country from txt file

def word_files(countries, capitals):
    temp_capitals = []

    file = open("countries-and-capitals.txt", "r")

    for line in file:
        countries.append(line.split(' | ')[0])
        temp_capitals.append(line.split(' | ')[1])

    for x in temp_capitals:
        capitals.append(x.replace("\n", ""))

    return countries, capitals

def word_pool(countries, capitals):

    user_input = int(input("Choose a word-pool: 1 = countries, 2 = capitals "))
    if user_input == 1:
        return random_word(countries)
    elif user_input == 2:
        return random_word(capitals)
    # elif user_input == 3:
    #     return random_word(both)
    else:
        print("Please, write 1 or 2.")
        return word_pool(countries, capitals)

def random_word(pool):

    import random
    word_upper = random.choice(pool)
    print(word_upper)
    return word_upper


### play

def play(word_upper, lives, score):
    word = word_upper.lower()
    # print(word)
    password = "_" * len(word)
    print(password)

    set_correct = set()
    set_wrong = set()

    while lives != 0:
        letter = (input("\nGuess a letter or write 'quit' ")).lower()

        # quit
        if letter == "quit":
            break
        # repetitions
        elif letter in set_correct or letter in set_wrong:
                print("You repeated a letter. Try again.")
                continue
        else:
            # correct or wrong
            if letter in word:
                for index in range(0, len(word)):
                    if letter == word[index]:
                        score += 1
                        set_correct.add(letter)
                        if word_upper[index].isupper():
                            password = password[:index] + letter.upper() + password[index+1:]
                        else:
                            password = password[:index] + letter + password[index+1:]
                print(password)

                if "_" not in password:
                    print(f"You won! Your score is: {score}\n\n\n")
                    break

            else:
                lives -= 1
                set_wrong.add(letter)
                print(f"You missed a letter. This is the list of missing letters: {set_wrong}")

                if lives > 0:
                    print(f"You' ve got {lives} chance(s) left.")
                else:
                    print(f"Game over. The word was {word_upper}.")
                    print(f"Thank you for playing! Your final score is {score}.\n\n\n")

    return score, lives

### menu

def main():
    countries = []
    capitals = []
    new_lists = word_files(countries, capitals)

    print("Hello. Let's play! Let's set the rules first.")
    lives = int(input("How many lives do you want to have? "))
    score = 0
    lista = [score, lives]

    user_input = "Yes"

    while user_input == "yes" or user_input == "Yes" or user_input == "y":
        word_upper = word_pool(countries, capitals)
        lista = play(word_upper, lives, score)
        score = lista[0]
        lives = lista[1]
        user_input = input("Do you want to play again? Yes/ No ")

    print("Bye bye")

main()



    