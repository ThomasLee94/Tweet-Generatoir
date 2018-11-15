# Importing dictogram class. 
from dictogram import Dictogram
# Importing a function that outputs a weighted random word based on a given histogram. 
from weighted_sample import random_word
# Returns parsed corpus into list form.
from get_text_from_corpus import read_file

# We are keeping track of dictionaries, not words
file_path = "./texts/beekeeper.txt"
file_data = read_file(file_path)

class Markov(dict):
    def __init__(self):
        super(Markov, self).__init__() # Initialise empty dictionary
        self.add_word()

    def add_word(self, word):  
        for word in file_data:
            for i in range(len(word_list)):
                j = i + 1
                current_word = word_list[i]
                next_word =  word_list[j]
                if current_word in self:
                    if self[current_word[i]] == next_word:
                        self[current_word[j]] += 1
                self[current_word] = {next_word: 1}

    def generate_random_sentence(self):
        random_sentence = list()
        for i in range(0,10):
            random_sentence.append(random_word(self))
        return random_sentence


def main():
    word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    list_len = len(word_list)
    markov = Markov()

    for i in range(0, list_len):
        if i + 1 < list_len:
            current_type = word_list[i]
            next_type = word_list[i + 1]
            markov.add_word(current_type, next_type)

    sentence = markov.generate_sentence()
    print("".join(sentencejjh))

if __name__ == '__main__':
    main()


                    