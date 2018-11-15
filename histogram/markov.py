from histogram.dictogram import Dictogram
from histogram.weighted_sample 
from functions.get_text_from_corpus import read_file

# We are keeping track of dictionaries, not words
file_path = "texts/beekeepers.txt"
file_data = read_file(file_path)

class Markov(dict):
    def __init__(self):
        super(Markov, self).__init__() # Initialise empty dictionary

    def add_word(word):  
        for word in file_data:
            for i in range(len(word_list)):
                j = i + 1
                current_word = word_list[i]
                next_word =  word_list[j]
                if current_word in self:
                    if self[current_word[i]] == next_word:
                        self[current_word[j]] += 1
                self[current_word] = {next_word: 1}
                    