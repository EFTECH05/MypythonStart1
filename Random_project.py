import random 
word_list = ["aardvark" , "baboon" , "camel"] 
choson_word = random.choice(word_list)
print(choson_word)

guess = input("guess a letter : ").lower()
print(guess)

 for letter in  choson_word :
     if letter == guess :
        print("right")
    else :
       print ()