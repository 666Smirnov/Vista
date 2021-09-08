
from PyQt5 import QtCore
from datetime import datetime
from pymysql import Error
import pymysql
def show_table(conn):
    with conn.cursor() as cursor:
        select_all_rows = "SELECT * FROM vista.test_vista "
        cursor.execute(select_all_rows)
        conn.commit()
        records = cursor.fetchall()
        return (records)

def add_row(conn, name, tel, date):
    #date = date.toString(QtCore.Qt.ISODate)
    date = date[-4] + date[-3] + date[-2] + date[-1] + '-' + date[3] + date[4] + '-' + date[0] + date[1]
    with conn.cursor() as cursor:
        sql = f"""INSERT INTO vista.test_vista (Имя, Телефон, Дата) VALUES ('{name}', {tel}, '{date}')"""
        cursor.execute(sql)
        conn.commit()


def delete(conn, id):
    with conn.cursor() as cursor:
        sql = f"DELETE FROM vista.test_vista WHERE id = '{id}'"
        cursor.execute(sql)
        conn.commit()


def updade(conn, id, data):
    id = id[0]['id']
    date = data[2]
    date = date[-4] + date[-3] + date[-2] + date[-1] + '-' + date[3] + date[4] + '-' + date[0] + date[1]
    data = [data[0], data[1], date]
    with conn.cursor() as cursor:
        sql = f"UPDATE vista.test_vista SET Имя = '{data[0]}', Телефон = '{data[1]}', Дата = '{date}' WHERE id = {id};"
        cursor.execute(sql)
        conn.commit()

def add_user(conn, login, password, date):
    date = date.toString(QtCore.Qt.ISODate)
    with conn.cursor() as cursor:
        sql = f"""INSERT INTO vista.user (login, password, date) VALUES('{login}', '{password}', '{date}');"""
        cursor.execute(sql)
        conn.commit()

def show_table_user(conn):
    with conn.cursor() as cursor:
        select_all_rows = "SELECT login, password FROM vista.user "
        cursor.execute(select_all_rows)
        conn.commit()
        records = cursor.fetchall()
        #print (records)
        return (records)

def check_user(conn, login):
    user_list = show_table_user(conn)
    if len(user_list) > 0:
        for l in range(len(user_list)):
            if login == user_list[l]['login']:
                return True
            else:
                return False


def auth(conn, login, password):
    user_list = show_table_user(conn)
    for l in range(len(user_list)):
        if login == user_list[l]['login'] and password == user_list[l]['password']:
            return True

def request_Abc(conn, abc):
    if len(abc) == 2:
        a = abc[0]
        b = abc[1]
        with conn.cursor() as cursor:
            select_name_abc =f"SELECT Имя, Телефон, Дата FROM vista.test_vista WHERE Имя LIKE '{a}%' OR Имя LIKE '{b}%'"
            cursor.execute(select_name_abc)
            records = cursor.fetchall()
            conn.commit()
            return records

    elif len(abc) == 4:
        a = abc[0]
        b = abc[1]
        c = abc[2]
        d = abc[3]
        with conn.cursor() as cursor:
            select_name_abc =f"SELECT Имя, Телефон, Дата FROM vista.test_vista WHERE Имя LIKE '{a}%' OR Имя LIKE '{b}%' OR Имя LIKE '{c}%' OR Имя LIKE '{d}%'"
            cursor.execute(select_name_abc)
            records = cursor.fetchall()
            conn.commit()
            return records

def add_last_user(conn, login, password):
    with conn.cursor() as cursor:
        sql = f"""INSERT INTO vista.last_user (login, password) VALUES ('{login}', '{password}')"""
        cursor.execute(sql)
        conn.commit()

def del_last_user(conn):
    with conn.cursor() as cursor:
        sql = "TRUNCATE TABLE vista.last_user"
        cursor.execute(sql)
        conn.commit()


def check_last_user(conn):
    with conn.cursor() as cursor:
        select_all_rows = "SELECT * FROM vista.last_user "
        cursor.execute(select_all_rows)
        conn.commit()
        records = cursor.fetchall()
        return (records)

def check_id(conn, name, tel, date):
    with conn.cursor() as cursor:
        date = str(date[-4] + date[-3] + date[-2] + date[-1] + '-' + date[3] + date[4] + '-' + date[0] + date[1])
        sql = f"""SELECT id FROM vista.test_vista WHERE Имя = '{name}' AND Телефон = '{tel}' AND Дата = '{date}'"""
        print(sql)
        cursor.execute(sql)
        conn.commit()
        records = cursor.fetchall()
        return (records)

def check_birthday(conn):
    with conn.cursor() as cursor:
        import datetime
        now = datetime.datetime.now()
        sql = f"""SELECT * FROM vista.test_vista WHERE (
date_format(now()+interval 7 day,'%m-%d')>date_format(Дата,'%m-%d')
AND date_format(NOW(),'%m-%d')<date_format(Дата,'%m-%d')
)
OR
(date_format(NOW()+interval 7 day,'%m')='01'
AND date_format(NOW(),'%m')='12'
AND 
   (
   date_format(NOW()+interval 7 day,'%m-%d')>date_format(Дата,'%m-%d') 
   OR
      (
      date_format(NOW(),'%m-%d')<date_format(Дата,'%m-%d')
      AND '12-31'>=date_format(Дата,'%m-%d')
      )
    )
)
ORDER BY Дата ASC"""
        cursor.execute(sql)
        conn.commit()
        records = cursor.fetchall()
        print(records)
        return (records)

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        cursor.execute('USE vista')
        print("Database created successfully")
    except Error as e:
        print(f"The error '{e}' occurred")

def create_connection(host_name, user_name, user_password):
    conn = None
    try:
        conn = pymysql.connect(
            host=host_name,
            user=user_name,
            passwd=user_password,
            cursorclass=pymysql.cursors.DictCursor
        )

        print("Connection to MySQL DB successful")
        return conn
    except Error as e:
        print(f"The error '{e}' occurred")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Таблица создана")
    except Error as e:
        print(f"The error '{e}' occurred")