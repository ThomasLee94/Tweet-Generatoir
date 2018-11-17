from markov import Markov

def main():
    word_list = ['hi', 'hi', 'hi', 'bye', 'bye', 'bye', 'bye', 'hello', 'there', 'is', 'tokens', 'and', 'words']
    list_len = len(word_list)
    markov = Markov()

    for i in range(0, list_len):
        if i + 1 < list_len:
            current_type = word_list[i]
            next_type = word_list[i + 1]
            markov.add_word_to_dict_of_dict(current_type, next_type)

    sentence = markov.generate_random_sentence()
    print("".join(sentencejjh))

if __name__ == '__main__':
    main()

