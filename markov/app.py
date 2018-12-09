from flask import Flask 
from markov_nth_order import Markov_nth_order
from weighted_sample import histogram, random_word_histogram
from get_text_from_corpus import read_file
from markov_app import main

app = Flask(__name__)

@app.route("/")
def generate_sentence():
    return main()

if __name__ == "__main__":
    app.run()
