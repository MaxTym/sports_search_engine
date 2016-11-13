import psycopg2 as pq
import os
from tabulate import tabulate
from menu import Menu
from create_sql import *
import sys


conn = pq.connect("dbname=barca")
cur = conn.cursor()


def print_table(table_name):
    headers = ["POS", "NO", "PLAYER", "AGE", "GS", "SB", "G", "SH", "SG", "A", "FC", "FS", "YC", "RC"]
    print(tabulate(table_name, headers, tablefmt="fancy_grid"))
    print("POS: POSITION NO: NUMBER GS: STARTS SB: SUB INS G: TOTAL GOALS SH: TOTAL SHOTS SG: SHOTS ON TARGET A: GOAL ASSISTS FC: FOULS COMMITTED FS: FOULS SUFFERED YC: YELLOW CARDS RC: RED CARDS")


def show_all_team():
    sql = "SELECT * FROM team ORDER BY NO"
    cur.execute(sql)
    print_table(cur.fetchall())


def update_stats():
    show_all_team()
    player_number = input("Which player would you like to update? Enter a player number ")
    while True:
        stat_to_update = input("\n'1' -- STARTS\n'2' -- SUB INS\n'3' -- TOTAL GOALS\n'4' -- TOTAL SHOTS\n'5' -- SHOTS ON TARGET\n'6' -- GOAL ASSISTS\n'7' -- FOULS COMMITTED\n'8' -- FOULS SUFFERED\n'9' -- YELLOW CARDS\n'10' -- RED CARDS\n'11' -- MAIN MENU\n")
        if stat_to_update == '1':
            starts(player_number)
        elif stat_to_update == '2':
            sub_ins(player_number)
        elif stat_to_update == '3':
            total_goals(player_number)
        elif stat_to_update == '4':
            total_shots(player_number)
        elif stat_to_update == '5':
            shots_on_target(player_number)
        elif stat_to_update == '6':
            goal_assists(player_number)
        elif stat_to_update == '7':
            fouls_committed(player_number)
        elif stat_to_update == '8':
            fouls_suffered(player_number)
        elif stat_to_update == '9':
            yellow_cards(player_number)
        elif stat_to_update == '10':
            red_cards(player_number)
        elif stat_to_update == '11':
            main()


def get_best_assistents():
    sql = "SELECT * FROM team ORDER BY A"
    cur.execute(sql)
    print_table(cur.fetchall()[:-6:-1])


def get_best_scorers():
    sql = "SELECT * FROM team ORDER BY G"
    cur.execute(sql)
    print_table(cur.fetchall()[:-6:-1])


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


def quit():
    sys.exit()


def main():
    os.system('clear')
    print("Welcome to Barcelona FC database!")
    print("_"*80)
    m = Menu()
    m.register("stats", check_stats)
    m.register("add new player", add_player)
    m.register("update player's info", update_player_info)
    m.register("update player's stats", update_stats)
    m.register("delete player", delete_player)
    m.register("quit", quit)
    m.display()


if __name__ == "__main__":
    main()
