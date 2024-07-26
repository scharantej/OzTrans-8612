
from flask import Flask, render_template, request, redirect
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flashcards', methods=['POST'])
def flashcards():
    flashcards = request.form.getlist('flashcards')
    translated_flashcards = []
    for flashcard in flashcards:
        translation = translator.translate(flashcard, dest='nl')
        translated_flashcards.append((flashcard, translation.text))
    return render_template('results.html', flashcards=translated_flashcards)

@app.route('/results')
def results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)
