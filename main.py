word = "pizza"
guesses = []
print ("Welcome to Hangman")
lives = 6
while True:
    hidden_word=""
    for x in word:
        if x in guesses:
            hidden_word += x
        else:
            hidden_word += "_"
        hidden_word +=" "
    print ("You have " + str(lives) + " lives left")
    print (hidden_word)
    if "_" not in hidden_word:
        print ("YOU WIN")
        break
    guess = input("Guess a Letter ")
    guesses.append(guess)
    if guess not in word:
        lives -=1
    if lives == 0:
        print ("GAME OVER. The word was pizza")
        break
