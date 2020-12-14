import sqlite3
import sys

from PyQt5.QtSql import *
from PyQt5.QtWidgets import *


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.first_creation()
        self.add()
        # Зададим тип базы данных
        db = QSqlDatabase.addDatabase('QSQLITE')
        # Укажем имя базы данных
        db.setDatabaseName('coffee.sqlite')
        # И откроем подключение
        db.open()

        # QTableView - виджет для отображения данных из базы
        view = QTableView(self)
        # Создадим объект QSqlTableModel,
        # зададим таблицу, с которой он будет работать,
        #  и выберем все данные
        model = QSqlTableModel(self, db)
        model.setTable('cofffee')
        model.select()

        # Для отображения данных на виджете
        # свяжем его и нашу модель данных
        view.setModel(model)
        view.move(10, 10)
        view.resize(617, 315)

        self.setGeometry(300, 100, 650, 450)
        self.setWindowTitle('Coffee')

    def first_creation(self):
        try:
            with sqlite3.connect("coffee.sqlite") as conn:
                cursor = conn.cursor()
                cursor.execute("CREATE TABLE cofffee("
                               "id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, "
                               "sort TEXT NOT NULL, "
                               "roast TEXT NOT NULL,"
                               "in_grains BOOL NOT NULL,"
                               "taste TEXT NOT NULL,"
                               "price INTEGER NOT NULL,"
                               "volume INTEGER NOT NULL)")
                conn.commit()
                return {"status": "ok"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()
    def add(self):
        try:
            with sqlite3.connect("coffee.sqlite") as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO cofffee(sort, roast, in_grains, taste, price, volume) VALUES (?, ?, ?, ?, "
                               "?, ?)", ("арабика", "хорошая", True, "мягкий вкус", 1000, 300))
                cursor.execute("INSERT INTO cofffee(sort, roast, in_grains, taste, price, volume) VALUES (?, ?, ?, ?, "
                               "?, ?)", ("либерика", "полная", False, "крепкий вкус", 2000, 500))
                cursor.execute("INSERT INTO cofffee(sort, roast, in_grains, taste, price, volume) VALUES (?, ?, ?, ?, "
                               "?, ?)", ("рибуста", "частичная", True, "мягкий вкус с горчинкой", 1500, 400))
                conn.commit()
                return {"status": "ok"}
        except Exception as ex:
            return {"status": ex.args[0]}
        finally:
            conn.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec())