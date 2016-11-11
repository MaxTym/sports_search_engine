import psycopg2


conn = psycopg2.connect("dbname=barca")
cur = conn.cursor()
#sql = "CREATE TABLE team (POS text, NO numeric, PLAYER text, AGE numeric, GS numeric, SB numeric, G numeric, SH numeric, SG numeric, A numeric, FC numeric, FS numeric, YC numeric, RC numeric);"
#cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 9, "Luis Suarez", 29, 10, 1, 8, 35, 16, 3, 9, 16, 5, 0,))
#cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 11, "Neymar", 24, 9, 0, 4, 28, 8, 4, 8, 42, 4, 0,))
cur.execute("UPDATE team SET POS = 'K' WHERE NO = 29")

conn.commit()

#A: GOAL ASSISTS AGE: AGE D: DRAWS FC: FOULS COMMITTED FS: FOULS SUFFERED
#G: TOTAL GOALS GC: GOALS CONCEDED GS: STARTS L: LOSSES RC: RED CARDS
#SB: SUB INS SG: SHOTS ON TARGET SH: TOTAL SHOTS SV: SAVES W: WINS YC: YELLOW CARDS
