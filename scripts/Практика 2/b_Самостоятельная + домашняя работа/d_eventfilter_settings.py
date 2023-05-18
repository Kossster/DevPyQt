"""
Реализация программу взаимодействия виджетов друг с другом:
Форма для приложения (ui/d_eventfilter_settings.ui)

Программа должна обладать следующим функционалом:

1. Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
   выводить новые значения в консоль

2. Соединить между собой QDial, QSlider, QLCDNumber
   (изменение значения в одном, изменяет значения в других)

3. Для QLCDNumber сделать отображение в различных системах счисления (oct, hex, bin, dec),
   изменять формат отображаемого значения в зависимости от выбранного в comboBox параметра.

4. Сохранять значение выбранного в comboBox режима отображения
   и значение LCDNumber в QSettings, при перезапуске программы выводить
   в него соответствующие значения
"""

from PySide6 import QtWidgets, QtCore, QtGui
from ui.d_eventfilter_settings import Ui_Form


class Window(QtWidgets.QWidget):
    comboBoxItems = ["Отображение в  dec", "Отображение в  hex", "Отображение в  bin", "Отображение в  oct"]

    def __init__(self, parent=None):
        super().__init__(parent)

        self.settings = QtCore.QSettings("MySettings_d_eventfilter")
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.comboBox.addItems(self.comboBoxItems)
        self.initSignals()
        self.loadData()


    def keyPressEvent(self, event: QtGui.QKeyEvent) -> None:
        """Добавить для dial возможность установки значений кнопками клавиатуры(+ и -),
            выводить новые значения в консоль"""
        key = event.key()
        current_val = self.ui.dial.value()
        if key == QtGui.Qt.Key.Key_Minus:
            self.ui.dial.setValue(current_val - 1)
        elif key == QtGui.Qt.Key.Key_Plus:
            self.ui.dial.setValue(current_val + 1)
        print(self.ui.dial.value())

    def initSignals(self):
        self.ui.horizontalSlider.valueChanged.connect(self.changeDial)
        self.ui.dial.valueChanged.connect(self.changeHorizontalSlider)
        self.ui.dial.valueChanged.connect(self.changeLcdNumber)
        self.ui.comboBox.currentTextChanged.connect(self.ModeLCDNumber)

    def changeDial(self):
        """Соединить между собой QDial и QSlider"""
        self.ui.dial.setValue(self.ui.horizontalSlider.value())

    def changeHorizontalSlider(self):
        """Соединить между собой QSlider и QDial"""
        self.ui.horizontalSlider.setValue(self.ui.dial.value())

    def changeLcdNumber(self):
        """Соединить между собой QDial и QLCDNumber"""
        self.ui.lcdNumber.display(self.ui.dial.value())

    def ModeLCDNumber(self):
        if self.ui.comboBox.currentText() == self.ui.comboBox.itemText(0):
            self.ui.lcdNumber.setDecMode()
        elif self.ui.comboBox.currentText() == self.ui.comboBox.itemText(1):
            self.ui.lcdNumber.setHexMode()
        elif self.ui.comboBox.currentText() == self.ui.comboBox.itemText(2):
            self.ui.lcdNumber.setBinMode()
        elif self.ui.comboBox.currentText() == self.ui.comboBox.itemText(3):
            self.ui.lcdNumber.setOctMode()

    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        self.settings.setValue("ComboBoxVal", self.ui.comboBox.currentText())
        self.settings.setValue("LcdNumberVal", self.ui.lcdNumber.value())

    def loadData(self) -> None:
        self.ui.comboBox.setCurrentText(self.settings.value("ComboBoxVal", ""))
        self.ui.lcdNumber.setProperty("intValue", self.settings.value("LcdNumberVal", ""))


if __name__ == "__main__":
    app = QtWidgets.QApplication()

    window = Window()
    window.show()

    app.exec()
