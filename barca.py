import psycopg2 as pq
import os
from tabulate import tabulate
from menu import Menu

conn = pq.connect("dbname=barca")
cur = conn.cursor()


def print_table(table_name):
    headers = ["POS", "NO", "PLAYER", "AGE", "GS", "SB", "G", "SH", "SG", "A", "FC", "FS", "YC", "RC"]
    print(tabulate(table_name, headers, tablefmt="fancy_grid"))
    print("\nPOS: POSSITION NO: NUMBER GS: STARTS SB: SUB INS G: TOTAL GOALS SH: TOTAL SHOTS SG: SHOTS ON TARGET A: GOAL ASSISTS FC: FOULS COMMITTED FS: FOULS SUFFERED YC: YELLOW CARDS RC: RED CARDS")


def add_player():
    pos = input("position? ")
    num = input("number? ")
    name = input("name? ")
    age = input("age? ")
    sql = "INSERT INTO team (POS, NO, PLAYER, AGE) VALUES (%s, %s, %s, %s)"
    cur.execute(sql, (pos, num, name, age))
    print("Player {} was succesfully added to the team!".format(name))
    conn.commit()


def show_all_team():
    sql = "SELECT * FROM team ORDER BY NO"
    cur.execute(sql)
    print_table(cur.fetchall())


def get_best_forwards():
    sql = "SELECT * FROM team ORDER BY G"
    cur.execute(sql)
    print_table(cur.fetchall())


def search_player_by_name():
    player_name = input("Enter player's name: ").strip()
    sql = "SELECT * from team"
    cur.execute(sql)
    db = cur.fetchall()
    t = []
    for i in db:
        if player_name.lower() in i[2].lower():
            t.append(i)
    print_table(t)


def check_int(x):
    while True:
         try:
             x == int(x)
             break
         except ValueError:
            print("Oops!  That was no valid number. Try again...")


def update_player():
    show_all_team()
    player_number = input("Which player would you like to update? Enter a player number ")
    name = input("name? ")
    number = input("number? ")
    position = input("position? ")
    sql = "UPDATE team SET POS = %s, NO = %s, PLAYER=%s WHERE NO=%s"
    cur.execute(sql, (position, number, name, player_number))
    conn.commit()


def search_by_position():
    player_position = input("Enter player's position: ")
    sql = "SELECT * from team"
    cur.execute(sql)
    db = cur.fetchall()
    t = []
    print("POS   NO   PLAYER" + " "*17 + "AGE  GS  SB  G  SH  SG  A  FC  FS  YC  RC")
    for i in db:
        if i[0].strip() == player_position.strip():
            t.append(i)
    print_table(t)


def search_by_number():
    sql = "SELECT * from team"
    cur.execute(sql)
    db = cur.fetchall()
    while True:
         try:
             player_number = int(input("Enter player's number: "))
             break
         except ValueError:
            print("Oops!  That was no valid number. Try again...")
    t = []
    for i in db:
        if i[1] == player_number:
            t.append(i)
    print_table(t)


def delete_player():
    show_all_team()
    player_number = input("enter a number of player you would like to delete? ")
    sql = "DELETE FROM team WHERE NO=%s"
    cur.execute(sql, (player_number,))
    conn.commit()


def check_stats():
    os.system('clear')
    stats_options = input("Check the stats:\n'1' -- by name\n'2' -- by number\n'3' -- by position\n'4' -- all team\n")
    if stats_options == '1':
        search_player_by_name()
    elif stats_options == '2':
        search_by_number()
    elif stats_options == '3':
        search_by_position()
    elif stats_options == '4':
        show_all_team()


def main():
    os.system('clear')
    print("Welcome to Barcelona FC database!")
    print("_"*80)
    choice = input("Do you want to see stats or add new player?\n'1' -- stats\n'2' -- add new palyer\n'3' -- update player's info\n'4' -- delete player\n")
    while True:
        if choice == '1':
            check_stats()
            break
        elif choice == '2':
            add_player()
            break
        elif choice == '3':
            update_player()
            break
        elif choice == '4':
            delete_player()
            break


if __name__ == "__main__":
    main()
