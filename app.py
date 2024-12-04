from flask import Flask, request, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/negocio')
def negocio():
    return render_template('negocio.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    # Salvar os dados em um arquivo
    with open('submissions.txt', 'a') as file:
        file.write(f'Nome: {name}\nEmail: {email}\nMensagem: {message}\n\n')

    return render_template('thank_you.html')

@app.route('/css/<path:filename>')
def send_css(filename):
    return send_from_directory('css', filename)

@app.route('/images/<path:filename>')
def send_image(filename):
    return send_from_directory('images', filename)

if __name__ == '__main__':
    app.run(debug=True)
