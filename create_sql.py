import psycopg2


conn = psycopg2.connect("dbname=barca")
cur = conn.cursor()


def create_sql_table():
    "CREATE TABLE team (POS text, NO integer, PLAYER text, AGE integer, GS integer, SB integer, G integer, SH integer, SG integer, A integer, FC integer, FS integer, YC integer, RC integer);"
    # cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 9, "Luis Suarez", 29, 10, 1, 8, 35, 16, 3, 9, 16, 5, 0,))
    # cur.execute("INSERT INTO team VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", ("F", 11, "Neymar", 24, 9, 0, 4, 28, 8, 4, 8, 42, 4, 0,))
    cur.execute("UPDATE team SET POS = 'K' WHERE NO = 29")
    conn.commit()


def update_player():
    player_number = input("Which player would you like to update? Enter a player number ")
    name = input("name? ")
    number = input("number? ")
    position = input("position? ")
    sql = "UPDATE team SET POS = %s, NO = %s, PLAYER=%s WHERE NO=%s"
    cur.execute(sql, (position, number, name, player_number))
    conn.commit()


def add_player():
    pos = input("position? ")
    num = input("number? ")
    name = input("name? ")
    age = input("age? ")
    sql = "INSERT INTO team (POS, NO, PLAYER, AGE) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (pos, num, name, age))
    print("Player {} was succesfully added to the team!".format(name))
    conn.commit()


def delete_player():
    player_number = input("enter a number of player you would like to delete? ")
    sql = "DELETE FROM team WHERE NO=%s"
    cur.execute(sql, (player_number,))
    conn.commit()
