""" 
Take a histogram and output a random word from it based on its frequency.
This means words of a higer frequency have a higher probability to be
outputted in random_word()
"""
import random
from get_text_from_corpus import read_file

def histogram(words_list):
    histogram_dict = {}
    for word in words_list:
        if word in histogram_dict:
            histogram_dict[word] += 1
        else:
            histogram_dict[word] = 1
    return histogram_dict

def unique_words(histogram_dict):
    return len(histogram_dict)

def output_random_word(histogram_dict):
    counter = 0
    # Finding total frequency of all words in the histogram.
    total_frequency_list = histogram_dict.values()
    total_frequency_number = 0
    for frequency in total_frequency_list:
        total_frequency_number += frequency

    random_count = random.randint(0, total_frequency_number-1)

    # TODO: Find out exactly what this does.
    for key,value in histogram_dict.items():
        counter += value
        if counter > random_count:
            return key

# def random_word_markov(dictionary_of_dictionary):
#     counter = 0
#     # Finding total frequency of all words in sub-dictionary
#     total_frequency = dictionary_of_dictionary.tokens
#     random_count = random.randint(0, total_frequency-1)

#     # ! The value of a dictionary_of_dictionary will be a dictionary
#     for key,value in dictionary_of_dictionary.items():
#         for key_inner_dict, value_inner_dict in value.items():
#             counter += value_inner_dict.values()
#             if counter > random_count:
#                 return key 

# * Random words printed put into a dictionary to see
# * the distribution more easily.
def random_word_histogram(words_list, histogram_dict):
    random_word_list = list()
    for i in range(1000):
        random_word_list.append(output_random_word(histogram_dict))
    weighted_histogram = histogram(random_word_list)
    return weighted_histogram
    
def main():
    file_data = read_file("texts/beekeeper.txt")
    histogram_dict = histogram(file_data)
    random_word_weighted = random_word(histogram_dict)
    random_word_weighted_dict = random_word_histogram(file_data,histogram_dict)
    print("*****RANDOM WORD***** \n")
    print(random_word_weighted)
    print("*****DISTRIBUTION DICTIONARY*****")
    print(random_word_weighted_dict)

if __name__ == "__main__":
    main()
        
   