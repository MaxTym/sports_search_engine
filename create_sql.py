import psycopg2
import sys
from barca import *

conn = psycopg2.connect("dbname=barca")
cur = conn.cursor()


def create_sql_table():
    cur.execute("CREATE TABLE IF NOT EXISTS team (POS text, NO integer, PLAYER text, AGE integer, GS integer, SB integer, G integer, SH integer, SG integer, A integer, FC integer, FS integer, YC integer, RC integer);")
    conn.commit()


def update_player_info():
    show_all_team()
    player_number = input("Which player would you like to update? Enter a player number ")
    name = input("name? ")
    number = input("number? ")
    position = input("position? (GK, D, M, F)")
    sql = "UPDATE team SET POS = %s, NO = %s, PLAYER=%s WHERE NO = %s"
    cur.execute(sql, (position, number, name, player_number))
    conn.commit()


def check_int():
    while True:
        try:
            number = int(input(""))
        except ValueError:
            print("That was not valid number. Try again...")
        else:
            return number


def check_player_number():
    sql = "SELECT * from team"
    cur.execute(sql)
    db = cur.fetchall()
    list_of_numbers = []
    while True:
        print("Enter player's number")
        player_number = check_int()
        for player in db:
            list_of_numbers.append(player[1])
        if player_number in list_of_numbers:
            print("This number already exists")
        else:
            return player_number
            break


def starts(player_number):
    starts = input("starts ")
    sql = "UPDATE team SET GS = %s WHERE NO = %s"
    cur.execute(sql, (starts, player_number))
    conn.commit()


def sub_ins(player_number):
    sub_ins = input("sub ins ")
    sql = "UPDATE team SET SB = %s WHERE NO = %s"
    cur.execute(sql, (sub_ins, player_number))
    conn.commit()


def total_goals(player_number):
    total_goals = input("total goals ")
    sql = "UPDATE team SET G = %s WHERE NO = %s"
    cur.execute(sql, (total_goals, player_number))
    conn.commit()


def total_shots(player_number):
    total_shots = input("total shots ")
    sql = "UPDATE team SET SH = %s WHERE NO = %s"
    cur.execute(sql, (total_shots, player_number))
    conn.commit()


def shots_on_target(player_number):
    shots_on_target = input("shots on taret ")
    sql = "UPDATE team SET SG = %s WHERE NO = %s"
    cur.execute(sql, (shots_on_target, player_number))
    conn.commit()


def goal_assists(player_number):
    goal_assists = input("sub ins ")
    sql = "UPDATE team SET A = %s WHERE NO = %s"
    cur.execute(sql, (goal_assists, player_number))
    conn.commit()


def fouls_committed(player_number):
    fouls_committed = input("fouls committed ")
    sql = "UPDATE team SET FC = %s WHERE NO = %s"
    cur.execute(sql, (fouls_committed, player_number))
    conn.commit()


def fouls_suffered(player_number):
    fouls_suffered = input("fouls sufferred ")
    sql = "UPDATE team SET FS = %s WHERE NO = %s"
    cur.execute(sql, (fouls_suffered, player_number))
    conn.commit()


def yellow_cards(player_number):
    yellow_cards = input("yellow cards ")
    sql = "UPDATE team SET YC = %s WHERE NO = %s"
    cur.execute(sql, (yellow_cards, player_number))
    conn.commit()


def red_cards(player_number):
    red_cards = input("red cards ")
    sql = "UPDATE team SET RC = %s WHERE NO = %s"
    cur.execute(sql, (red_cards, player_number))
    conn.commit()


def quit():
    sys.exit()


def add_player():
    while True:
        pos = input("position? (GK, D, M, F)").lower()
        if pos == 'gk' or pos == 'd' or pos == 'm' or pos == 'f':
            break
        else:
            print("Wrong position. Try again")
    num = check_player_number()
    name = input("name? ")
    print("Player's age")
    age = check_int()
    sql = "INSERT INTO team (POS, NO, PLAYER, AGE) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (pos.upper(), num, name, age))
    print("Player {} was succesfully added to the team!".format(name))
    conn.commit()


def delete_player():
    show_all_team()
    player_number = input("enter a player number you want to delete? ")
    sql = "DELETE FROM team WHERE NO=%s"
    cur.execute(sql, (player_number,))
    conn.commit()


create_sql_table()
