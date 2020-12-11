import csv, random
import utilities as utl

adjectives = utl.file_to_array('./data/adjectives_clean.txt')
nouns = utl.file_to_array('./data/nouns_clean.txt')
names = utl.file_to_array('./data/names_clean.txt')
bad_words = utl.file_to_array('./data/bad_words_cmu.txt')
bad_words_obfs = utl.file_to_array('./data/bad_words_google.txt')

obfuscation_dictionary = {'A':'4','a':'4','E':'3','e':'3','I':'1','i':'1','O':'0','o':'0','L':'1','l':'1','S':'5','s':'5'}

def obfuscate(username):
    return_username = username
    for i, char in enumerate(username, 0):
        if char in obfuscation_dictionary and random.randint(0, 1) == 1:
            return_username = return_username[:i] + obfuscation_dictionary[char] + return_username[i+1:]
    return return_username

def adjective_noun_generator(num_to_generate, obfuscation):

    with open("./data/good_adjective_noun.txt", 'w') as outputFile:
        for i in range(num_to_generate):
            ran_adj = random.choice(adjectives)
            ran_noun = random.choice(nouns)
            username = ran_adj + ran_noun

            if (obfuscation):
                username = obfuscate(username)

            outputFile.write(utl.print_name_data("G", username))

def name_noun_generator(num_to_generate, obfuscation):

    with open("./data/good_name_noun.txt", 'w') as outputFile:
        for i in range(num_to_generate):
            ran_adj = random.choice(names)
            ran_noun = random.choice(nouns)
            username = ran_adj + ran_noun

            if (obfuscation):
                username = obfuscate(username)

            outputFile.write(utl.print_name_data("G", username))

def clean_words():
    for bad_word in bad_words:
        if bad_word in nouns:
            nouns.remove(bad_word)
        if bad_word in adjectives:
            adjectives.remove(bad_word)
        if bad_word in names:
            names.remove(bad_word)
    
    with open("./data/names_clean.txt", 'w') as names_file:
        for name in names:
            names_file.write(name + "\n")

    with open("./data/nouns_clean.txt", 'w') as nouns_file:
        for noun in nouns:
            nouns_file.write(noun + "\n")

    with open("./data/adjectives_clean.txt", 'w') as adjectives_file:
        for adjective in adjectives:
            adjectives_file.write(adjective + "\n")


if __name__ == "__main__":
    clean_words()