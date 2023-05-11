"""
Файл для повторения темы событий

Напомнить про работу с событиями.

Предлагается создать приложение, которое будет показывать все события происходящие в приложении,
(переопределить метод event), вывод событий производить в консоль.
При выводе события указывать время, когда произошло событие.
"""

from PySide6 import QtWidgets, QtCore
import time

class Window(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        self.initUi()
        self.initSignals()
        self.event

    def initUi(self):
        # Задаем кнопки
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Разверни")

        # Создаем горизонтальный и вертикальный слои
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()

        # lineEdit добавляем в горизонтальный слой
        layout1.addWidget(self.lineEditInput)
        layout1.addWidget(self.lineEditMirror)

        # Виджеты(lineEdit и pushButton) добавляем в общий вертикальный слой
        layout2.addLayout(layout1)
        layout2.addWidget(self.pushButtonMirror)

        # Отображаем все в главном окне
        self.setLayout(layout2)

    # Перезагрузка метода event, для отображения действий производимых в приложении в консоль
    def event(self, event: QtCore.QEvent) -> bool:
        print(time.ctime(), event)
        return super().event(event)

    def initSignals(self):
        self.pushButtonMirror.clicked.connect(self.invertData)
        self.lineEditInput.textChanged.connect(lambda x: self.lineEditMirror.setText(x[::-1]))

    @QtCore.Slot()
    def invertData(self):
        self.lineEditMirror.setText(self.lineEditInput.text()[::-1])


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
