import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl5bcns72pts73ej6mc0-a.oregon-postgres.render.com', database='servicewebdalina', user='servicewebdalina_user', password='L8MYCEW2GOgP8qDfhIGHkkAaszJoHMX0')

    return con

def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('select * from usuarios')
    recset = cur.fetchall()
    conexao.close()
    return recset

def inserirDB(login, senha, nome, conexao):
    cur = conexao.cursor()

    exito = False
    try:
        sql = f"insert into usuarios values ('{login}', '{senha}', '{nome}')"
        cur.execute(sql)
    except psycopg2.IntegrityError:
        conexao.rollback()
        exito = False
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito