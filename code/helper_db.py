from db import sql_connection, cursor


def insert_execution(name: str, email: str, joining_date: str, salary: float) -> None:
    try:
        insert_query = """INSERT INTO developers (name, email, joining_date, salary)
                        VALUES (?, ?, ?, ?)"""

        data_tuple = (name, email, joining_date, salary)

        cursor.execute(insert_query, data_tuple)

        sql_connection.commit()
        print("Insert Executed")
    except sql_connection.Error as error:
        print("Error in inserting data to table:", error)


def insert_multiple_execution(records: list):
    try:
        insert_query = """INSERT INTO developers (name, email, joining_date, salary)
                        VALUES (?, ?, ?, ?)"""

        cursor.executemany(insert_query, records)

        sql_connection.commit()
        print("Insert Executed")
    except sql_connection.Error as error:
        print("Error in inserting data to table:", error)


def select_data(table: str):
    try:
        select_query = f"SELECT * FROM {table}"
        cursor.execute(select_query)
        return cursor.fetchall()
    except sql_connection.Error as error:
        print("Error in select data from table:", error)
