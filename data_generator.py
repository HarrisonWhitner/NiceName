import csv, random
import utilities as utl

def obfuscate(string):
    print("Hello")

def adjective_noun_generator(num_to_generate):

    adjectives = utl.file_to_array('./data/adjectives.txt')
    nouns = utl.file_to_array('./data/nouns.txt')

    with open("./data/good_adjective_noun.txt", 'w') as outputFile:
        for i in range(num_to_generate):
            ran_adj = random.choice(adjectives)
            ran_noun = random.choice(nouns)
            username = ran_adj + ran_noun
            outputFile.write(utl.print_name_data("G", username))

def name_noun_generator():
    print("Hello")


if __name__ == "__main__":
    adjective_noun_generator(25)