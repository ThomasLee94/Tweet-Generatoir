from dictogram import Dictogram
from weighted_sample import output_random_word 
from get_text_from_corpus import read_file
import random

class Markov_nth_order(dict):
    def __init__(self, word_list=None, order=2):
        super(Markov_nth_order, self).__init__() # Initialise empty dictionary
        self.types = 0
        self.tokens = 0
        self.order = order
        if word_list is not None:
            self.create_dict_of_dict(word_list)

    def create_dict_of_dict(self, word_list):
        """ 
        Creating a dictionary of {(current_tuple):{next_type: 1}} structure.
        """
        list_length = len(word_list)
        for i in range(0, list_length-self.order):
            if i + 1 + self.order < list_length:
                # Tuple of nth order as current_tuple
                current_tuple = tuple(word for word in word_list[i: i + self.order])
                next_type = word_list[i + 1 + self.order]
                self.add_word_to_dict_of_dict(current_tuple, next_type)
            else:
                current_type = (word_list[i], word_list[i+self.order])
                next_word = 'END'
                self.add_word_to_dict_of_dict(current_type, next_word)

    def add_word_to_dict_of_dict(self, current_type, next_type): 
        """ 
        Adding new tuple key-value pairs  or incrementing next_next_word frequency if
        they exist.
        """ 
        if current_type in self:
            dictogram = self[current_type]
            # Dictogram class incrementing frequency if current_type is found 
            # in initialised dictionary.
            dictogram.add_count(next_type)
        else:
            # New {(current_type, next_word): {next_next_word: 1}} pair being added if current_type
            # is not found. Dictogram used to make histogram. 
            self[current_type] = Dictogram(next_type)
            self.types += 1
            self.tokens += 1
    
    def generate_random_sentence(self, sentence_length=8):
        """ 
        Generating a random sentence from given corpus using markov chains,
        returning as a list. 
        """
        random_sentence_output = list()
        all_types = list(self.keys())
        
        # I will use a completely random word as my first word.
        # random_index = random.randrange(0, len(all_types))
        # random_type = all_types[random_index]
        # random_word = random_type[0]

        # Weighed first word
            # iterate through dict and inner dict to count the freq of word_list[i]. 
            # create histogram based on this freq.
            # call output_random_word on this dict.
        type_frequency_dict = {}
        for type, histogram in self.items():
            for word, frequency in histogram.items():
                if word in type_frequency_dict:
                    type_frequency_dict[word] += frequency
                else:
                    type_frequency_dict[word] = frequency
        random_word = output_random_word(type_frequency_dict)

        # for word in all_types:
        #     if word in self.[word]:
        #         self.count += 1
        #         if word in self.values()[word]:
        #             self.count += 1 

        next_words = list(random_type[1:self.order])
        random_sentence_output.extend((word for word in random_type))
        
        output_count = 1
        # * Now using n'th order markov chains to append the most likely "next_next_word"
        while output_count < sentence_length:
            try:
                random_word = output_random_word(self[random_word])
                if not random_word == 'END':
                    random_sentence_output.append(random_word)
                    output_count += 1
                    
                    next_words.append(random_word)
                    random_word = tuple(next_words)
                    next_words = next_words[1:self.order]
                # 'END' will be used to check if the random word picked is not at the
                # end of the given words_list. If it is, there can be no "next_next_word". 
                else:
                    new_index = random.randint(0, len(self.keys()) - 1)
                    random_word = list(self.keys())[new_index]
            except KeyError:
                 new_index = random.randint(0, len(self.keys()) - 1)
                 random_word = list(self.keys())[new_index]
                 next_word = random_word[1]

        return random_sentence_output
        


