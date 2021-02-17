import sys
import sqlite3
from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Информация о кофе')
        uic.loadUi('main.ui', self)

        self.connection = sqlite3.connect("coffee.db")
        self.result = self.connection.cursor().execute('SELECT * FROM coffee').fetchall()


        self.tableWidget.setRowCount(11)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.resizeRowsToContents()
        self.tableWidget.setHorizontalHeaderLabels(('ID', 'Название сорта', 'Степень обжарки', 'Молотый/В зёрнах', 'Описание вкуса', 'Цена', 'Объём упаковки'))
        for i, elem in enumerate(self.result):
            for j, value in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(value)))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.exit(app.exec())