import mysql.connector
username = "ToDo"
password = "ADE8(cAfS[b0_M2i"

connection = mysql.connector.connect(user=username,password=password,host="127.0.0.1",database="python_todolist",auth_plugin="mysql_native_password")

INSERT_query = f"INSERT INTO todolist(goal, piority, message, date) VALUES (%(goal)s,%(piority)s,%(message)s,%(date)s);"
SELECT_query = "SELECT * FROM todolist;"

cursor = connection.cursor()

# insertData = {
#     "goal" : "Get a job",
#     "piority" : "Really important",
#     "message" : "Good Luck",
#     "date" : "2022-07-20"
# }
# cursor.execute(INSERT_query,insertData)
# connection.commit()


cursor.execute(SELECT_query)
for (id, goal, piority, message, date) in cursor:
    print(f"{id}. {goal} - {message} - {date}")


connection.close()