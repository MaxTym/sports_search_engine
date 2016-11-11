import psycopg2 as pq
import os
from tabulate import tabulate
from menu import Menu
from create_sql import *


conn = pq.connect("dbname=barca")
cur = conn.cursor()


def print_table(table_name):
    headers = ["POS", "NO", "PLAYER", "AGE", "GS", "SB", "G", "SH", "SG", "A", "FC", "FS", "YC", "RC"]
    print(tabulate(table_name, headers, tablefmt="fancy_grid"))
    print("\nPOS: POSITION NO: NUMBER GS: STARTS SB: SUB INS G: TOTAL GOALS SH: TOTAL SHOTS SG: SHOTS ON TARGET A: GOAL ASSISTS FC: FOULS COMMITTED FS: FOULS SUFFERED YC: YELLOW CARDS RC: RED CARDS")


def show_all_team():
    sql = "SELECT * FROM team ORDER BY NO"
    cur.execute(sql)
    print_table(cur.fetchall())


def get_best_assistents():
    sql = "SELECT * FROM team ORDER BY A"
    cur.execute(sql)
    print_table(cur.fetchall()[-5:])


def get_best_scorers():
    sql = "SELECT * FROM team ORDER BY G"
    cur.execute(sql)
    print_table(cur.fetchall()[-5:])


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


def check_stats():
    os.system('clear')
    stats_options = input("Check the stats:\n'1' -- by name\n'2' -- by number\n'3' -- by position\n'4' -- top scorers\n'5' -- top assistents\n'6' -- all team\n")
    if stats_options == '1':
        search_player_by_name()
    elif stats_options == '2':
        search_by_number()
    elif stats_options == '3':
        search_by_position()
    elif stats_options == '4':
        get_best_scorers()
    elif stats_options == '5':
        get_best_assistents()
    elif stats_options == '6':
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
            Menu.add_player()
            break
        elif choice == '3':
            show_all_team()
            update_player()
            break
        elif choice == '4':
            show_all_team()
            delete_player()
            break


if __name__ == "__main__":
    main()
