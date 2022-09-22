import sys
from PyQt5.QtWidgets import QApplication, QMainWindow

import mainUI

class MainWindow(QMainWindow):

    def __init__(self, cui, parent=None):
        super(QMainWindow, self).__init__(parent)
        self.ui = cui.Ui_MainWindow()
        self.ui.setupUi(self)

    # 提交按钮的点击相应
    def commit(self):
        print('[debug] commit')
        # info 为输入字符串
        info = self.ui.textEdit.toPlainText()

        # 经过处理后将result输出到输出框
        self.ui.textBrowser.setText(info)
        return 'Hello world!'

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = MainWindow(mainUI)
    mainWindow.show()
    sys.exit(app.exec_())

