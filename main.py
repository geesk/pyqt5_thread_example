import sys
import time

from PyQt5 import uic
from PyQt5.QtCore import QThread, pyqtSignal
from PyQt5.QtWidgets import QApplication, QMainWindow

form_class = uic.loadUiType("main_ui.ui")[0]
class main_window(QMainWindow, form_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.thread = example_thread()

        # start()를 통해 run()을 시작
        self.thread.start()
        self.thread.progress.connect(self.progressBar.setValue)
        # line edit에 있는 text를 label에 넣는다.
        self.pushButton.clicked.connect(self.set_label_text)

    def set_label_text(self):
        self.label.setText(self.lineEdit.text())

class example_thread(QThread):
    progress = pyqtSignal(int)
    def __init__(self):
        super().__init__()

    def run(self):
        # 1초마다 progress bar의 value를 1씩 증가시킨다.
        value = 0
        while True:
            value += 1
            if value > 100:
                value = 0
            self.progress.emit(value)
            time.sleep(1)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = main_window()
    myWindow.show()
    app.exec_()