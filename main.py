from flask import *
from dao import *

app = Flask(__name__)
app.secret_key = 'tapetedeferro'

id_usuario = None

def varBool(reporter):
    if reporter.lower() == 'on':
        reporter = True
    elif reporter.lower() == 'none':
        reporter = False
    return reporter

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["POST","GET"])
def login():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))

    conexao = conectardb()
    tupla = listarUsuarios(conexao)

    for usuario in tupla:
        if(login == usuario[1] and senha == usuario[2]):
            session['id']
            session['usuario'] = login
            # print(id_usuario)
            return render_template('mainlog.html', usuario=login, logado=True, id_usuario=usuario[3])

    else:
        return render_template('index.html', logado=False)

@app.route("/cadastrar", methods=["POST","GET"])
def cadastrarusuario():
    login = str(request.form.get('email'))
    senha = str(request.form.get('pswd'))
    nome = str(request.form.get('txt'))
    reporter = str(request.form.get('rpt'))

    #print(reporter)
    reporter = varBool(reporter)
    #print(reporter)

    conexao = conectardb()

    insert = inserirDB(login, senha, nome, reporter, conexao)
    
    return render_template('index.html', exito=insert)

@app.route("/mainlog")
def mainlog():
    return render_template('mainlog.html')

@app.route("/cadastrar-noticia", methods=["POST","GET"])
def cadastrarNoticia():
    tupla = listarUsuarios(conexao)

    titulo = str(request.form.get('title'))
    noticia = str(request.form.get('noticia'))

    conexao = conectardb()

    insert = inserirNoticia(titulo, noticia, id_usuario)

    return render_template("menuADM/cadastrar_noticia.html")

if __name__ == "__main__":
    app.run(debug=True)