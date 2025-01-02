import sqlite3

try:
    sql_connection = sqlite3.connect("sql_db.db")

    cursor = sql_connection.cursor()

    print("База даних створена й підключена")

except sqlite3.Error as db_error:
    print(f"Помилка підключення до {db_error}")
finally:
    if sql_connection:
        print("Зупинили роботу програми")

    # create_table_query = """CREATE TABLE developers(
    #                             id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    #                             name VARCHAR(20) NOT NULL,
    #                             email VARCHAR(320) NOT NULL,
    #                             joining_date DATETIME,
    #                             salary REAL NOT NULL
    #                         );"""

    # cursor.execute(create_table_query)
    # sql_connection.commit()

    # print("CREATED DEVELOPERS")

    # query = "SELECT * FROM developers"
    # cursor.execute(query)
    # dev_records = cursor.fetchall()
