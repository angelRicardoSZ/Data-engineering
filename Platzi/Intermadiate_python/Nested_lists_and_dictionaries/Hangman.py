import random
import os

### STEP 1 ###

## Function that read the file with the list of words to guess

# 1.- Read a txt file with the secret words to guess
# 2.- Returns a dictionary with information

def read_words():
    
    with open("./files/data.txt", "r", encoding="UTF-8") as f:
        
        # Use of list comprehensions and strip to remove line break
        
        secret_words = [line.strip("\n") for line in f]
        
        
        #
        #print(secret_words)
        
        #print(list(enumerate(secret_words)))
        
        dict_secret_words = {key:value for key, value in enumerate(secret_words)}
        
        #print(dict_secret_words)
        return dict_secret_words
    
    
    
### STEP 2 ###    
    
## Function that transforms the information for its correct use
#  1.- Take the output from read_words()
#  2.- Clean the data removing accents and capital letters
#  3.- Return a dictionary with clean information

def clean_words(word_original):
    characters =  (
            ("á", "a"),
            ("é", "e"),
            ("í", "i"),
            ("ó", "o"),
            ("ú", "u"),
        )
    for x,y in characters:
        
        word_clean = word_original.replace(x, y).replace(x.upper(), y.upper())
        
        
    return word_clean



## Game

def run():
    
    ## Constants
        
    ### STEP 1 ###
        
    dict_secret_words = read_words()
        
    ### STEP 2 ###
        
    # Word to guess 
    total_secret_words = len(dict_secret_words)
        
    random_value = random.randint(0,total_secret_words-1)
        
    word_to_guess = clean_words(dict_secret_words.get(random_value))
        
        
    length_word_to_guess = len(word_to_guess)

    secret_word = length_word_to_guess*"_"
    print(word_to_guess)
        
    print("Welcome to hangman´s game, guess the next word: ")
        
            
        ## Variables
        
        # Secret word "- - - -" = SW
    lives = int(length_word_to_guess/2)
        
        # While SW be different of WG OR liVes > 0:
        
    while word_to_guess != secret_word and lives > 0: 
            
        print(secret_word)
        secret_word = list(secret_word)

            # input (User´s handwriting = UH)
            
        user_word = input("Enter a letter, remember that you have " + str(lives) + " lives. ")
            
        
            
        if user_word in word_to_guess:
                
                    # get the index in which it is     
            for index, value in enumerate(word_to_guess): 
                if value == user_word:
                            # change blank space for UH: "_" -> "UH" 
                    secret_word[index] = user_word
                    
        else:
            print("You have lost a life :( ")
            lives = lives -1
        secret_word = "".join(secret_word)    
        os.system("cls")
                
        
                
    if secret_word == word_to_guess and lives > 0:
        print("You Won, congratulations.")
        status = input("Would you like to play again? (yes/no) ")  
    else: 
        print("you've lost, good luck for the next one")
        status = input("Would you like to play again? (yes/no) ")  
    return status
    





if __name__ == "__main__":
    status = run()
    if status == "yes":
        run()
    else: 
        print("Thank you for play.")
    