import markov_app
from flask import Flask, render_template, request, redirect
import sys
import twitter

app = Flask(__name__, template_folder="templates")

@app.route("/")
def main():
    sentence_str = markov_app.main()
    return render_template("index.html", sentence=sentence_str)

@app.route('/tweet', methods=['POST'])
def tweet():
    status = request.form['quote']
    twitter.tweet(status)
    return redirect('/')

if __name__ == "__main__":
    app.run(host="0.0.0.0")
    
    
