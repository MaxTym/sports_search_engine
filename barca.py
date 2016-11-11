import psycopg2
import os

conn = psycopg2.connect("dbname=barca")
cur = conn.cursor()

def add_player():
    name = input("position? ")
    dob = input("number? ")
    height = input("name? ")
    sql = "INSERT INTO team (POS, NO, PLAYER) VALUES (%s, %s, %s)"
    cur.execute(sql, (name, dob, height))
    conn.commit()

def show_all_team():
    sql = "SELECT * FROM team"
    cur.execute(sql)
    cur.fetchall()


def search_player_by_name(player_name):
    sql = "SELECT * from team WHERE PLAYER = 'Messi'"
    cur.execute(sql)
    print(cur.fetchall())



def update_player():
    show_all_team()
    student_id = input("which id would you like to update? ")
    name = input("name? ")
    sql = "UPDATE team SET name=%s WHERE id=%s"
    cur.execute(sql, (name, student_id))


def delete_player():
    show_all_team()
    student_id = input("which id would you like to update? ")
    sql = "DELETE FROM team WHERE id=%s"
    cur.execute(sql, (student_id,))


def main():
    os.system('clear')
    print("Welcome to Barcelona FC database!")
    print("_"*80)
    choice = input("Do you want to see stats or add new player?\n'1' -- stats\n'2' -- add new palyer\n")
    while True:
        if choice == '1':
            #show_all_team()
            player_name = input("Enter a player name: ")
            search_player_by_name(player_name)
            break
        elif choice == '2':
            add_player()



#UPDATE <table> SET <column> = <value>
#show_all_team()
#add_player()
main()
