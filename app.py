from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def home():  # put application's code here
    return render_template('homepage.html')


@app.route('/contatos')
def contatos():  # put application's code here
    return render_template('contatos.html')

@app.route('/escola/<nome_da_escola>')
def escola_nome(nome_da_escola):
    return render_template("escolas.html", nome_da_escola=nome_da_escola)

if __name__ == '__main__':
    app.run(debug=True)
