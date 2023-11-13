import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl5fcbpo91lc7385ltmg-a.oregon-postgres.render.com', database='projetosql',
    user='projetosql_user', password='7exPg72T12JsBMz5GPJli75yiqVwiZHn')

    return con

def listarUsuarios(conexao):
    cur = conexao.cursor()
    cur.execute('SELECT * FROM usuarios')
    recset = cur.fetchall()
    conexao.close()
    return recset

def inserirDB(login, senha, nome, reporter, conexao):
    cur = conexao.cursor()

    exito = False
    try:
        sql = f"INSERT INTO usuarios (nome, login, senha, reporter) VALUES ('{nome}', '{login}', '{senha}', '{reporter}')"
        cur.execute(sql)
    except psycopg2.IntegrityError as e:
        conexao.rollback()
        exito = False
        print(e)
    else:
        conexao.commit()
        exito = True

    conexao.close()
    return exito