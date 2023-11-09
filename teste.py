import psycopg2

con = psycopg2.connect(host='dpg-cl5fcbpo91lc7385ltmg-a.oregon-postgres.render.com', database='projetosql', user='projetosql_user', password='7exPg72T12JsBMz5GPJli75yiqVwiZHn')

cur = con.cursor()

sql = "insert into usuarios values ('Emilton', 'emilton@gmail.com','emilton123')"
cur.execute(sql)
con.commit()
