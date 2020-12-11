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

def run_username_generator(outputFile, label, num_to_generate, obfuscation, list_1, list_2):
    with open(outputFile, 'w') as oFile:
        for i in range(num_to_generate):
            ran_1 = random.choice(list_1)
            ran_2 = random.choice(list_2)

            username = ran_1 + ran_2

            if random.randint(0, 1) == 1:
                username = ran_2 + ran_1

            if (obfuscation):
                username = obfuscate(username)

            oFile.write(utl.print_name_data(label, username))

def generate_usernames(num_generate):

    # GOOD USERNAMES
    run_username_generator("./data/generated/G_Adj_Name.txt", "G", num_generate, False, adjectives, names)
    run_username_generator("./data/generated/G_Adj_Name_Obfs.txt", "G", num_generate, True, adjectives, names)
    run_username_generator("./data/generated/G_Adj_Noun.txt", "G", num_generate, False, adjectives, nouns)
    run_username_generator("./data/generated/G_Adj_Noun_Obfs.txt", "G", num_generate, True, adjectives, nouns)
    run_username_generator("./data/generated/G_Name_Noun.txt", "G", num_generate, False, names, nouns)
    run_username_generator("./data/generated/G_Name_Noun_Obfs.txt", "G", num_generate, True, names, nouns)

    # BAD USERNAMES
    run_username_generator("./data/generated/B_CMU_Adj.txt", "B", num_generate, False, adjectives, bad_words)
    run_username_generator("./data/generated/B_CMU_Adj_Obfs.txt", "B", num_generate, True, adjectives, bad_words)
    run_username_generator("./data/generated/B_CMU_Name.txt", "B", num_generate, False, adjectives, bad_words)
    run_username_generator("./data/generated/B_CMU_Name_Obfs.txt", "B", num_generate, True, adjectives, bad_words)
    run_username_generator("./data/generated/B_CMU_Noun.txt", "B", num_generate, False, names, bad_words)
    run_username_generator("./data/generated/B_CMU_Noun_Obfs.txt", "B", num_generate, True, names, bad_words)


if __name__ == "__main__":
    generate_usernames(50)