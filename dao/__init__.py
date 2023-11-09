import psycopg2

def conectardb():
    con = psycopg2.connect(host='dpg-cl5fcbpo91lc7385ltmg-a.oregon-postgres.render.com', database='projetosql',
    user='projetosql_user', password='7exPg72T12JsBMz5GPJli75yiqVwiZHn')

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