# Importing dictogram class. 
from dictogram import Dictogram
# Importing a function that outputs a weighted random word based on a given histogram. 
from weighted_sample import output_random_word 
# Returns parsed corpus into list form.
from get_text_from_corpus import read_file
import random

# We are keeping track of dictionaries, not words
# file_path = "./texts/beekeeper.txt"
# word_list = read_file(file_path)

class Markov(dict):
    def __init__(self, word_list=None):
        super(Markov, self).__init__() # Initialise empty dictionary
        self.types = 0
        self.tokens = 0
         
        if word_list is not None:
            self.create_dict_of_dict(word_list)

    def create_dict_of_dict(self, word_list):
        list_length = len(word_list)
        for i in range(0, list_length-1):
            if i + 1 < list_length:
                current_type = word_list[i]
                next_word = word_list[i + 1]
                self.add_word_to_dict_of_dict(current_type, next_word)
            else:
                current_type = word_list[i]
                next_word = 'END'
                self.add_word_to_dict_of_dict(current_type, next_word)

    def add_word_to_dict_of_dict(self, current_type, next_word):  
        if current_type in self:
            dictogram = self[current_type]
            # Dictogram class incrementing frequency if current_type is found 
            # in initialised dictionary.
            dictogram.add_count(next_word)
        else:
            # New {current_type: {next_word: 1}} pair being added if current_type
            # is not found. Dictogram used to make histogram. 
            self[current_type] = Dictogram([next_word])
            self.types += 1
            self.tokens += 1
            
    
    def generate_random_sentence(self, word_list, sentence_length=8):
        random_sentence_output = list()
        # I will use a completely random word as my first word.
        # TODO: I will try and pick the most frequently used word as my first "random" word. 
        random_index = random.randint(0, len(self.keys())-1)
        random_word = list(self.keys())[random_index]
        random_sentence_output.append(random_word)
        
        output_count = 0
        # * Now using markov chains to append the most likely "next" word
        while output_count < sentence_length:
            random_word = output_random_word(self[random_word])
            if not random_word == 'END':
                random_sentence_output.append(random_word)
                output_count += 1
            # 'END' will be used to check if the random word picked is not at the
            # end of the given words_list. If it is, there can be no "next_word". 
            else:
                new_index = random.randint(0, len(self.keys()) - 1)
                random_word = list(self.keys())[new_index]

        return random_sentence_output


