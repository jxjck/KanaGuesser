from flask import Flask, render_template, request, session
import random
from kana_dict import kana_dict
app = Flask(__name__)
app.secret_key = "some_secret_key"

@app.route('/', methods=['GET', 'POST'])
def guess_kana():
    if request.method == 'POST':
        user_guess = request.form.get('user_input', '').strip()
        correct_reading = session.get('correct_reading', None)

        if user_guess == correct_reading:

            result = "Correct!"
        else:

            result = f"Wrong! The correct reading was '{correct_reading}'."

        random_kana, random_reading = random.choice(list(kana_dict.items()))
        session['current_kana'] = random_kana

        session['correct_reading'] = random_reading

        return render_template('index.html', kana=session['current_kana'], result=result)

    else:  #GET
        random_kana, random_reading = random.choice(list(kana_dict.items()))
        session['current_kana'] = random_kana
        session['correct_reading'] = random_reading

        return render_template('index.html', kana=session['current_kana'])

if __name__ == "__main__":
    app.run()