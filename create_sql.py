import psycopg2


conn = psycopg2.connect("dbname=barca")
cur = conn.cursor()
#sql = "CREATE TABLE team (POS text, NO integer, PLAYER text, AGE integer, GS integer, SB integer, G integer, SH integer, SG integer, A integer, FC integer, FS integer, YC integer, RC integer);"
#cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 9, "Luis Suarez", 29, 10, 1, 8, 35, 16, 3, 9, 16, 5, 0,))
#cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 11, "Neymar", 24, 9, 0, 4, 28, 8, 4, 8, 42, 4, 0,))
cur.execute("UPDATE team SET POS = 'K' WHERE NO = 29")
conn.commit()
