# Importing dictogram class. 
from dictogram import Dictogram
# Importing a function that outputs a weighted random word based on a given histogram. 
from weighted_sample import random_word
# Returns parsed corpus into list form.
from get_text_from_corpus import read_file

# We are keeping track of dictionaries, not words
file_path = "./texts/beekeeper.txt"
word_list = read_file(file_path)

class Markov(dict):
    def __init__(self, word_list=None):
        super(Markov, self).__init__() # Initialise empty dictionary
        self.types = 0
        self.tokens = 0
        if word_list is not None:
            self.create_sub_dictionary(word_list)

    def create_sub_dictionary(self, word_list):
        list_length = len(word_list)
        for i in range(0, list_length):
            if i + 1 < list_length:
                current_type = word_list[i]
                next_word = word_list[i + 1]
                self.add_word(current_type, next_word)

    def add_word_to_sub_dictionary(self, current_type, next_word):  
        if current_type in self:
            for word in self:
                if next_word in self[current_type]:
                    self[current_type][next_word] += 1
                    self.tokens += 1
            self[current_type] = {next_word: 1} 
            self.types += 1
            self.tokens += 1
    
    def generate_random_sentence()
        random_sentence_output = list()
        

        # for word in file_data:
        #     for i in range(len(word_list)):
        #         j = i + 1
        #         current_word = word_list[i]
        #         next_word =  word_list[j]
        #         if current_word in self:
        #             if self[current_word[i]] == next_word:
        #                 self[current_word[j]] += 1
        #         self[current_word] = {next_word: 1}

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


                    