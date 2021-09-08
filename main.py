import sys  # sys нужен для передачи argv в QApplication
import traceback

from PyQt5 import QtWidgets
import pymysql
import sys
import design  # Это наш конвертированный файл дизайна
import design_rep_pass
import registration
import alphabet
import book
import redaction
import sql_req
class ExampleApp(QtWidgets.QMainWindow, design.Ui_Authorization, design_rep_pass.Window_rep_pass, alphabet.Ui_ABC, registration.Registration, book.Ui_PhoneBook, redaction.Redact):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле design.py
        super().__init__()
        self.setupUi(self)            # Это нужно для инициализации нашего дизайна



# Connect to MariaDB Platform

conn = sql_req.create_connection(host_name="127.0.0.1", user_name="root", user_password="vista")
create_DB = "CREATE DATABASE IF NOT EXISTS vista"
create_tab_test_vista = "CREATE TABLE IF NOT EXISTS test_vista(id INTEGER AUTO_INCREMENT, Имя VARCHAR(50), Телефон INTEGER, Дата DATE, PRIMARY KEY(id))"
create_tab_last_user = "CREATE TABLE IF NOT EXISTS last_user(login VARCHAR(50), password VARCHAR(50))"
create_tab_user = "CREATE TABLE IF NOT EXISTS user(id INTEGER, login VARCHAR(50), password VARCHAR(50), date DATE)"
sql_req.create_database(conn, create_DB)
sql_req.execute_query(conn, create_tab_test_vista)
sql_req.execute_query(conn, create_tab_last_user)
sql_req.execute_query(conn, create_tab_user)

def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    widget = QtWidgets.QStackedWidget()
    window = ExampleApp()  # Создаём объект класса ExampleApp
    win_list = book.Ui_PhoneBook()
    window_rep_pass = design_rep_pass.Window_rep_pass()
    window_reg = registration.Registration()
    win_abc = alphabet.Ui_ABC()
    win_redact = redaction.Redact()


    #widget.addWidget(window)
    #widget.addWidget(window_rep_pass)

    window.show()  # Показываем окно
    #widget.setFixedHeight(405)
    #widget.setFixedWidth(538)
    #widget.show()
    app.exec_()  # и запускаем приложение

def excepthook(exc_type, exc_value, exc_tb):
    tb = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    print("Oбнаружена ошибка !:", tb)
#    QtWidgets.QApplication.quit()             # !!! если вы хотите, чтобы событие завершилось


sys.excepthook = excepthook

if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
