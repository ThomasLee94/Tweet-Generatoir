from markov_nth_order import Markov_nth_order
from weighted_sample import histogram, random_word_histogram
from get_text_from_corpus import read_file

def main():
    word_list = read_file("./texts/beekeeper.txt")
    # word_list = "one fish two fish red fish blue fish".split()
    # word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    list_len = len(word_list)
    markov = Markov_nth_order(order=3)
    print

    markov.create_dict_of_dict(word_list)
    print(markov)
    sentence_list = markov.generate_random_sentence(word_list, 20)
    print(" ".join(sentence_list))

    print(markov.order)
    histogram_dict = histogram(sentence_list)
    print(histogram_dict)
    # random_word_weighted_dict = random_word_histogram(sentence_list,histogram_dict)
    # print(random_word_weighted_dict)

if __name__ == '__main__':
    main()

