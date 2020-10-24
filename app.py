import json
from difflib import get_close_matches

dict = json.load(open("words.json", "r"))


def getMeaning(word):
    word = word.lower()
    if word in dict:
        meaning= dict[word]
        
        if len(meaning) > 0:
           return "\n".join(meaning)
    elif len(get_close_matches(word, dict.keys())) > 0:
     
       word2= input(f"\n'{word}' cannot be found see close matches {get_close_matches(word, dict.keys())}: ")
       return getMeaning(word2)
    else:
        return f"\n'{word}' cannot be found "




while True:
    
        word_to_lookup = input('Enter the word: "\q" to quit program: ')
        if word_to_lookup.lower() != "\q":
            print()
            print(getMeaning(word_to_lookup))
            print()
        else:
            break
   
        
        
        
# word_to_lookup = input('Enter the word: ')


# while word_to_lookup.lower() != "quit()":
#         print()
#         print(getMeaning(word_to_lookup))
#         print()
      
#         word_to_lookup = input('Enter the word: "quit()" to quit program: ')
        