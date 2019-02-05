from markov_nth_order import Markov_nth_order
from weighted_sample import histogram, random_word_histogram
from get_text_from_corpus import read_file
import random 

# creat a histogram here
def histogram(word_list):
    histogram = {}
    for word in word_list:
        if word in histogram:
            histogram[word] += 1
        else:
            histogram[word] = 1
    return histogram

# create a weighted histogram here
def weighted(histogram, word_list):
    total_words = len(word_list)-1
    print(histogram)

    freq_hist = {}

    # total_frequency_list = histogram.values()
    # total_frequency_number = 0
    # for frequency in total_frequency_list:
    #     total_frequency_number += frequency

    # random_count = random.randint(0, total_frequency_number-1)

    for k, v in histogram.items():
        # counter += value
        # if counter > random_count:
        #     return key
        # v = histogram[key]
        # check the word is not in freq_hist
        
        print(k)
        freq_hist[k] = float(v/total_words)
    print(freq_hist)
            
def main():
    # word_list = read_file("stan-transcript-s1-s8-&-s10-s20-no-brackets.txt")
    word_list = "one fish two fish red fish blue fish blue red three".split()
    print(word_list)
    # word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    hist = histogram(word_list)
    # print('Histogram: {}'.format(hist))
    freq = weighted(hist, word_list)

if __name__ == '__main__':
    main()

