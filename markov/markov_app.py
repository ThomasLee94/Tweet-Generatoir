from markov import Markov
from weighted_sample import histogram, random_word_histogram

def main():
    word_list = "one fish two fish red fish blue fish".split()
    # word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    list_len = len(word_list)
    markov = Markov()

    for i in range(0, list_len):
        if i + 1 < list_len:
            current_type = word_list[i]
            next_word = word_list[i + 1]
            markov.add_word_to_dict_of_dict(current_type, next_word)

    sentence_list = markov.generate_random_sentence(word_list, 20)
    print(" ".join(sentence_list))

    histogram_dict = histogram(sentence_list)
    print(histogram_dict)
    # random_word_weighted_dict = random_word_histogram(sentence_list,histogram_dict)
    # print(random_word_weighted_dict)

if __name__ == '__main__':
    main()

