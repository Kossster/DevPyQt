"""
Файл для повторения темы фильтр событий

Напомнить про работу с фильтром событий.

Предлагается создать кликабельный QLabel с текстом "Красивая кнопка",
используя html - теги, покрасить разные части текста на нём в разные цвета
(красивая - красным, кнопка - синим)
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
        # Задаем виджеты
        self.lineEditInput = QtWidgets.QLineEdit()
        self.lineEditMirror = QtWidgets.QLineEdit()
        self.pushButtonMirror = QtWidgets.QPushButton("Разверни")

        # Задаем фильтрацию для виджетов
        self.lineEditInput.installEventFilter(self)
        self.lineEditMirror.installEventFilter(self)
        self.pushButtonMirror.installEventFilter(self)

        # Задаем "красивую кнопку"
        self.lable = QtWidgets.QLabel("ДО НАВЕДЕНИЯ")
        self.lable.installEventFilter(self)
        self.lable.setTextFormat(QtCore.Qt.RichText)

        # Создаем горизонтальный и вертикальный слои
        layout1 = QtWidgets.QHBoxLayout()
        layout2 = QtWidgets.QVBoxLayout()

        # lineEdit добавляем в горизонтальный слой
        layout1.addWidget(self.lineEditInput)
        layout1.addWidget(self.lineEditMirror)

        # Виджеты(lineEdit и pushButton) добавляем в общий вертикальный слой
        layout2.addLayout(layout1)
        layout2.addWidget(self.pushButtonMirror)
        layout2.addWidget(self.lable)

        # Отображаем все в главном окне
        self.setLayout(layout2)

    # Перезагрузка метода event, для отображения действий производимых в приложении в консоль
    # def event(self, event: QtCore.QEvent) -> bool:
    #     print(time.ctime(), event)
    #     return super().event(event)

    # Создаем фильтр при котором при наведении на lineEditInput в lineEditMirror будет писаться "XXX"
    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.lineEditInput and event.type() == QtCore.QEvent.Type.Enter:
            self.lineEditMirror.setText("ХХХ")

        if watched == self.lable and event.type() == QtCore.QEvent.Type.Enter:
            self.lable.setText("<html><head/><body><p><span style=' color:#ff0000;'>Красивая </span><span style=' color:#0000ff;'>кнопка</span></p></body></html>")

        return super().eventFilter(watched, event)

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
