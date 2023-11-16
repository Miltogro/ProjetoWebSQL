import psycopg2
from main import *

con = psycopg2.connect(host='dpg-cl5fcbpo91lc7385ltmg-a.oregon-postgres.render.com', database='projetosql', user='projetosql_user', password='7exPg72T12JsBMz5GPJli75yiqVwiZHn')

cur = con.cursor()

sql = f"INSERT INTO noticias (titulo, noticia, id_usuario) VALUES ('titulo', 'noticia', 26)"
cur.execute(sql)
con.commit()
