import mysql.connector
username = "ToDo"
password = "ADE8(cAfS[b0_M2i"

connection = mysql.connector.connect(user=username,password=password,host="127.0.0.1",database="python_todolist",auth_plugin="mysql_native_password")

INSERT_query = f"INSERT INTO todolist(goal, priority, message, date) VALUES (%(goal)s,%(priority)s,%(message)s,%(date)s);"
SELECT_query = "SELECT * FROM todolist {};"
SELECT1_query = "SELECT * FROM todolist WHERE id={};"
UPDATE_query = "UPDATE todolist SET goal = \"{}\", priority = \"{}\", message = \"{}\", date = \"{}\" WHERE id = {};"
DELETE_query = "DELETE FROM todolist WHERE id={};"

cursor = connection.cursor()

# insertData = {
#     "goal" : "Get a job",
#     "priority" : "Really important",
#     "message" : "Good Luck",
#     "date" : "2022-07-20"
# }
# cursor.execute(INSERT_query,insertData)
# connection.commit()


# cursor.execute(SELECT_query)
# for (id, goal, priority, message, date) in cursor:
#     print(f"{id}. {goal} - {message} - {date}")

while True:
    print("1. Wypisz zadania")
    print("2. Dodaj zadanie")
    print("3. Edytuj zadanie")
    print("4. Usuń zadanie")
    print("5. Wyjdź")
    choice = int(input("Wybierze numer:\t"))
    if choice == 5:break
    elif choice == 1:
        choice1 = input("Jeśli chcesz wypisać dane wegług daty, wpisz \"Tak\":\t")
        selectData = ""
        if choice1.lower() == "tak":
            choice2 = input("Jeśli chcesz wypisać dane od najpóźniejszej do najwcześniejszej, wpisz \"PW\":\t")
            selectData = "ORDER BY date"
            if choice2.lower() == "pw":selectData = "ORDER BY date DESC"
        cursor.execute(SELECT_query.format(selectData))
        for (id, goal, priority, message, date) in cursor:
            print(f"{id}. {goal} - {priority} - {message} : {date}")
        print("--KONIEC--")
    elif choice == 2:
        goal = input("Napisz cel zadania:\t")
        priority = input("Napisz priorytet zadania:\t")
        message = input("Dodaj komentarz:\t")
        date = input("Napisz termin w formacie RRRR-MM-DD:\t")
        insertData = {
            "goal": goal,
            "priority": priority,
            "message": message,
            "date": date
        }
        cursor.execute(INSERT_query, insertData)
        connection.commit()
    elif choice == 3:
        choice1 = int(input("Podaj id zadania, które chcesz edytować:\t"))
        cursor.execute(SELECT1_query.format(choice1))
        for (id, goal, priority, message, date) in cursor:
            print(f"{id}. {goal} - {priority} - {message} : {date}")
        goal = input("Napisz cel zadania:\t")
        priority = input("Napisz priorytet zadania:\t")
        message = input("Dodaj komentarz:\t")
        date = input("Napisz termin w formacie RRRR-MM-DD:\t")
        cursor.execute(UPDATE_query.format(goal,priority,message,date,choice1))
        connection.commit()
    elif choice == 4:
        choice1 = int(input("Podaj id zadania, które chcesz usunąć:\t"))
        cursor.execute(DELETE_query.format(choice1))
        connection.commit()
connection.close()
