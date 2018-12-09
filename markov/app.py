from flask import Flask 
from sample import read_file, histogram, random_word, main
app = Flask(__name__)

@app.route("/")
def generate_sentence():
    return main()

if __name__ == "__main__":
    app.run()
