import markov_app
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    sentence_str = markov_app.main()
    return render_template("index.html", sentence=sentence_str)

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
    
