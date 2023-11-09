from flask import *
from dao import *

app = Flask(__name__)
app.secret_key = 'tapetedeferro'

@app.route("/")
def home():
    return render_template('index.html')#('mainlog.html')

@app.route("/login", methods=["POST"])
def login():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))

    conexao = conectardb()
    tupla = listarUsuarios(conexao)

    for usuario in tupla:
        if(login == usuario[0] and senha == usuario[1]):
            session['usuario'] = login
            return render_template('mainlog.html', usuario=login)

    else:
        return render_template('errologin.html')

@app.route("/cadastrar", methods=["POST"])
def cadastrarusuario():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))
    nome = str(request.form.get('txt'))

    conexao = conectardb()
    if inserirDB(login, senha, nome, conexao):
        return render_template('index.html')
    else:
        return render_template('errocadastro.html')

@app.route("/mainlog")
def mainlog():
    return render_template('mainlog.html')

if __name__ == "__main__":
    app.run(debug=True)