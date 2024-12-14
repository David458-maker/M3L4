# Import
from flask import Flask, render_template, request, send_from_directory


app = Flask(__name__)

# Formularz z rezultatami
@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        # odczytywanie wybranego obrazka
        selected_image = request.form.get('image-selector')
        text_top = request.form.get("textTop")
        # Zadanie #2. Odczytywanie tekstu
        text_bottom = request.form.get("textBottom")

        # Zadanie #3. Odczytywanie pozycji tekstu
        text_top_y = request.form.get("textTop_y")
        text_bottom_y = request.form.get("textBottom_y")
        # Zadanie #3. Odczytywanie koloru tekstu
        colour = request.form.get("colour-selector")

        return render_template('index.html', 
                               # Wyświetlanie wybranego obrazka
                               selected_image=selected_image, 

                               # Zadanie #2. Wyświetlanie tekstu
                               text_top = text_top,
                               text_bottom = text_bottom,
                               text_top_y = text_top_y,
                               text_bottom_y = text_bottom_y,
                               colour = colour

                               # Zadanie #3. Wyświetlanie koloru
                               
                               
                               # Zadanie #3. Wyświetlanie pozycji tekstu

                               )
    else:
        # Wyświetlanie pierwszego obrazka, jako grafika domyślna
        return render_template('index.html', selected_image='logo.svg')


@app.route('/static/img/<path:path>')
def serve_images(path):
    return send_from_directory('static/img', path)

app.run(debug=True)
