"""
## Ex 3-2. 어플리케이션 아이콘 넣기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Icon')
        self.setWindowIcon(QIcon('web.png'))
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 3-3. 창 닫기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(50, 50)
        btn.resize(btn.sizeHint())
        btn.clicked.connect(QCoreApplication.instance().quit)

        self.setWindowTitle('Quit Button')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 '''

"""
## Ex 3-4. 툴팁 나타내기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QToolTip
from PyQt5.QtGui import QFont


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif', 10))
        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.move(50, 50)
        btn.resize(btn.sizeHint())

        self.setWindowTitle('Tooltips')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""
'''
## Ex 3-5. 상태바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage('Ready')

        self.setWindowTitle('Statusbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''
"""
## Ex 3-6. 메뉴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('&File')
        filemenu.addAction(exitAction)

        self.setWindowTitle('Menubar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 3-7. 툴바 만들기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, qApp
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        saveAction = QAction(QIcon('save.png'), 'Save', self)
        editAction = QAction(QIcon('edit.png'), 'Edit', self)
        printAction = QAction(QIcon('print.png'), 'Print', self)
        exitAction = QAction(QIcon('exit.png'), 'Exit', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Exit application')
        exitAction.triggered.connect(qApp.quit)

        self.statusBar()

        self.toolbar = self.addToolBar('Exit')
        self.toolbar.addAction(saveAction)
        self.toolbar.addAction(editAction)
        self.toolbar.addAction(printAction)
        self.toolbar.addAction(exitAction)

        self.setWindowTitle('Toolbar')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 3-8. 창을 화면의 가운데로.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QDesktopWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Centering')
        self.resize(500, 350)
        self.center()
        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
from PyQt5.QtCore import QDate, Qt

now = QDate.currentDate()
print(now.toString('d.M.yy'))
print(now.toString('dd.MM.yyyy'))
print(now.toString('ddd.MMMM.yyyy'))
print(now.toString(Qt.ISODate))
print(now.toString(Qt.DefaultLocaleLongDate))
'''

"""
from PyQt5.QtCore import QTime

time = QTime.currentTime()
print(time.toString())
"""

'''
from PyQt5.QtCore import QTime, Qt

time = QTime.currentTime()
print(time.toString('h.m.s'))
print(time.toString('hh.mm.ss'))
print(time.toString('hh.mm.ss.zzz'))
print(time.toString(Qt.DefaultLocaleLongDate))
print(time.toString(Qt.DefaultLocaleShortDate))
'''

"""
from PyQt5.QtCore import QDate

now = QDate.currentDate()
print(now.toString())
"""

'''
## Ex 3-9. 날짜와 시간 표시하기.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtCore import QDate, Qt


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.date = QDate.currentDate()
        self.initUI()

    def initUI(self):
        self.statusBar().showMessage(self.date.toString(Qt.DefaultLocaleLongDate))

        self.setWindowTitle('Date')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 3-10. 스타일 꾸미기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        lbl_red = QLabel('Red')
        lbl_green = QLabel('Green')
        lbl_blue = QLabel('Blue')

        lbl_red.setStyleSheet("color: red;"
                             "border-style: solid;"
                             "border-width: 2px;"
                             "border-color: #FA8072;"
                             "border-radius: 3px")
        lbl_green.setStyleSheet("color: green;"
                               "background-color: #7FFFD4")
        lbl_blue.setStyleSheet("color: blue;"
                              "background-color: #87CEFA;"
                              "border-style: dashed;"
                              "border-width: 3px;"
                              "border-color: #1E90FF")

        vbox = QVBoxLayout()
        vbox.addWidget(lbl_red)
        vbox.addWidget(lbl_green)
        vbox.addWidget(lbl_blue)

        self.setLayout(vbox)

        self.setWindowTitle('Stylesheet')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 4-1. 절대적 배치.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        label1 = QLabel('Label1', self)
        label1.move(20, 20)
        label2 = QLabel('Label2', self)
        label2.move(20, 60)

        btn1 = QPushButton('Button1', self)
        btn1.move(80, 13)
        btn2 = QPushButton('Button2', self)
        btn2.move(80, 53)

        self.setWindowTitle('Absolute Positioning')
        self.setGeometry(300, 300, 400, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 4-2. 박스 레이아웃.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        okButton = QPushButton('OK')
        cancelButton = QPushButton('Cancel')

        hbox = QHBoxLayout()
        hbox.addStretch(1)
        hbox.addWidget(okButton)
        hbox.addWidget(cancelButton)
        hbox.addStretch(1)

        vbox = QVBoxLayout()
        vbox.addStretch(3)
        vbox.addLayout(hbox)
        vbox.addStretch(1)

        self.setLayout(vbox)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 4-3. 그리드 레이아웃.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QTextEdit)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title:'), 0, 0)
        grid.addWidget(QLabel('Author:'), 1, 0)
        grid.addWidget(QLabel('Review:'), 2, 0)

        grid.addWidget(QLineEdit(), 0, 1)
        grid.addWidget(QLineEdit(), 1, 1)
        grid.addWidget(QTextEdit(), 2, 1)

        self.setWindowTitle('QGridLayout')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-1. QPushButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn1 = QPushButton('&Button1', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('Button&2')

        btn3 = QPushButton('Button3', self)
        btn3.setEnabled(False)

        vbox = QVBoxLayout()
        vbox.addWidget(btn1)
        vbox.addWidget(btn2)
        vbox.addWidget(btn3)

        self.setLayout(vbox)
        self.setWindowTitle('QPushButton')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-2. QLabel.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        label1 = QLabel('First Label', self)
        label1.setAlignment(Qt.AlignCenter)

        label2 = QLabel('Second Label', self)
        label2.setAlignment(Qt.AlignVCenter)

        font1 = label1.font()
        font1.setPointSize(20)

        font2 = label2.font()
        font2.setFamily('Times New Roman')
        font2.setBold(True)

        label1.setFont(font1)
        label2.setFont(font2)

        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(label2)

        self.setLayout(layout)

        self.setWindowTitle('QLabel')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-3. QCheckBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QCheckBox
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cb = QCheckBox('Show title', self)
        cb.move(20, 20)
        cb.toggle()
        cb.stateChanged.connect(self.changeTitle)

        self.setWindowTitle('QCheckBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def changeTitle(self, state):
        if state == Qt.Checked:
            self.setWindowTitle('QCheckBox')
        else:
            self.setWindowTitle(' ')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-4. QRadioButton.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QRadioButton


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        rbtn1 = QRadioButton('First Button', self)
        rbtn1.move(50, 50)
        rbtn1.setChecked(True)

        rbtn2 = QRadioButton(self)
        rbtn2.move(50, 70)
        rbtn2.setText('Second Button')

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QRadioButton')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-5. QComboBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel('Option1', self)
        self.lbl.move(50, 150)

        cb = QComboBox(self)
        cb.addItem('Option1')
        cb.addItem('Option2')
        cb.addItem('Option3')
        cb.addItem('Option4')
        cb.move(50, 50)

        cb.activated[str].connect(self.onActivated)

        self.setWindowTitle('QComboBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onActivated(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-6. QLineEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl = QLabel(self)
        self.lbl.move(60, 40)

        qle = QLineEdit(self)
        qle.move(60, 100)
        qle.textChanged[str].connect(self.onChanged)

        self.setWindowTitle('QLineEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def onChanged(self, text):
        self.lbl.setText(text)
        self.lbl.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-6-1. QLineEdit (Advanced).

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # echo_group
        self.echo_group = QGroupBox('Echo')
        self.echo_label = QLabel('Mode:')

        self.echo_cb = QComboBox()
        self.echo_cb.addItem('Normal')
        self.echo_cb.addItem('No Echo')
        self.echo_cb.addItem('Password')
        self.echo_cb.addItem('PasswordEchoOnEdit')

        self.echo_le = QLineEdit()
        self.echo_le.setPlaceholderText('Placeholder Text')
        self.echo_le.setFocus()

        # validator_group
        self.validator_group = QGroupBox('Validator')
        self.validator_label = QLabel('Type:')

        self.validator_cb = QComboBox()
        self.validator_cb.addItem('No validator')
        self.validator_cb.addItem('Integer validator')
        self.validator_cb.addItem('Double validator')

        self.validator_le = QLineEdit()
        self.validator_le.setPlaceholderText('Placeholder Text')

        # alignment_group
        self.alignment_group = QGroupBox('Alignment')
        self.alignment_label = QLabel('Type:')

        self.alignment_cb = QComboBox()
        self.alignment_cb.addItem('Left')
        self.alignment_cb.addItem('Centered')
        self.alignment_cb.addItem('Right')

        self.alignment_le = QLineEdit()
        self.alignment_le.setPlaceholderText('Placeholder Text')

        # input_mask_group
        self.input_mask_group = QGroupBox('Input mask')
        self.input_mask_label = QLabel('Type:')

        self.input_mask_cb = QComboBox()
        self.input_mask_cb.addItem('No mask')
        self.input_mask_cb.addItem('Phone number')
        self.input_mask_cb.addItem('ISO date')
        self.input_mask_cb.addItem('License key')

        self.input_mask_le = QLineEdit()
        self.input_mask_le.setPlaceholderText('Placeholder Text')

        # access_group
        self.access_group = QGroupBox('Access')
        self.access_label = QLabel('Type:')

        self.access_cb = QComboBox()
        self.access_cb.addItem('False')
        self.access_cb.addItem('True')

        self.access_le = QLineEdit()
        self.access_le.setPlaceholderText('Placeholder Text')

        # activated.connect
        self.echo_cb.activated.connect(self.echo_changed)
        self.validator_cb.activated.connect(self.validator_changed)
        self.alignment_cb.activated.connect(self.alignment_changed)
        self.input_mask_cb.activated.connect(self.input_mask_changed)
        self.access_cb.activated.connect(self.access_changed)

        # echo_layout
        self.echo_layout = QGridLayout()
        self.echo_layout.addWidget(self.echo_label, 0, 0)
        self.echo_layout.addWidget(self.echo_cb, 0, 1)
        self.echo_layout.addWidget(self.echo_le, 1, 0, 1, 2)
        self.echo_group.setLayout(self.echo_layout)

        # validator_layout
        self.validator_layout = QGridLayout()
        self.validator_layout.addWidget(self.validator_label, 0, 0)
        self.validator_layout.addWidget(self.validator_cb, 0, 1)
        self.validator_layout.addWidget(self.validator_le, 1, 0, 1, 2)
        self.validator_group.setLayout(self.validator_layout)

        # alignment_layout
        self.alignment_layout = QGridLayout()
        self.alignment_layout.addWidget(self.alignment_label, 0, 0)
        self.alignment_layout.addWidget(self.alignment_cb, 0, 1)
        self.alignment_layout.addWidget(self.alignment_le, 1, 0, 1, 2)
        self.alignment_group.setLayout(self.alignment_layout)

        # input_mask_layout
        self.input_mask_layout = QGridLayout()
        self.input_mask_layout.addWidget(self.input_mask_label, 0, 0)
        self.input_mask_layout.addWidget(self.input_mask_cb, 0, 1)
        self.input_mask_layout.addWidget(self.input_mask_le, 1, 0, 1, 2)
        self.input_mask_group.setLayout(self.input_mask_layout)

        # access_layout
        self.access_layout = QGridLayout()
        self.access_layout.addWidget(self.access_label, 0, 0)
        self.access_layout.addWidget(self.access_cb, 0, 1)
        self.access_layout.addWidget(self.access_le, 1, 0, 1, 2)
        self.access_group.setLayout(self.access_layout)

        # layout
        self.layout = QGridLayout()
        self.layout.addWidget(self.echo_group, 0, 0)
        self.layout.addWidget(self.validator_group, 1, 0)
        self.layout.addWidget(self.alignment_group, 2, 0)
        self.layout.addWidget(self.input_mask_group,0, 1)
        self.layout.addWidget(self.access_group, 1, 1)

        self.setLayout(self.layout)

        self.setWindowTitle('Line Editor')
        self.show()

    def echo_changed(self, index):
        if index == 0:
            self.echo_le.setEchoMode(QLineEdit.Normal)
        elif index == 1:
            self.echo_le.setEchoMode(QLineEdit.NoEcho)
        elif index == 2:
            self.echo_le.setEchoMode(QLineEdit.Password)
        elif index == 3:
            self.echo_le.setEchoMode(QLineEdit.PasswordEchoOnEdit)

    def validator_changed(self, index):
        if index == 0:
            self.validator_le.setValidator(None)
        elif index == 1:
            self.validator_le.setValidator(QIntValidator(-99, 99))
        elif index == 2:
            double_validator = QDoubleValidator(-999.0, 999.0, 2)
            double_validator.setNotation(QDoubleValidator.StandardNotation)
            self.validator_le.setValidator(double_validator)

        self.validator_le.clear()

    def alignment_changed(self, index):
        if index == 0:
            self.alignment_le.setAlignment(Qt.AlignLeft)
        elif index == 1:
            self.alignment_le.setAlignment(Qt.AlignCenter)
        elif index == 2:
            self.alignment_le.setAlignment(Qt.AlignRight)

    def input_mask_changed(self, index):
        if index == 0:
            self.input_mask_le.setInputMask('')
        elif index == 1:
            self.input_mask_le.setInputMask('000-0000-0000')
        elif index == 2:
            self.input_mask_le.setInputMask('0000-00-00')
            self.input_mask_le.setText('20190410')
            self.input_mask_le.setCursorPosition(0)
        elif index == 3:
            self.input_mask_le.setInputMask('>AAAAA-AAAAA-AAAAA-AAAAA;#')

    def access_changed(self, index):
        if index == 0:
            self.access_le.setReadOnly(False)
        elif index == 1:
            self.access_le.setReadOnly(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-7. QProgressBar.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QProgressBar
from PyQt5.QtCore import QBasicTimer


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.pbar = QProgressBar(self)
        self.pbar.setGeometry(30, 40, 200, 25)

        self.btn = QPushButton('Start', self)
        self.btn.move(40, 80)
        self.btn.clicked.connect(self.doAction)

        self.timer = QBasicTimer()
        self.step = 0

        self.setWindowTitle('QProgressBar')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def timerEvent(self, e):
        if self.step >= 100:
            self.timer.stop()
            self.btn.setText('Finished')
            return

        self.step = self.step + 1
        self.pbar.setValue(self.step)

    def doAction(self):
        if self.timer.isActive():
            self.timer.stop()
            self.btn.setText('Start')
        else:
            self.timer.start(100, self)
            self.btn.setText('Stop')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-8. QSlider & QDial.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QSlider, QDial, QPushButton
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.move(30, 30)
        self.slider.setRange(0, 50)
        self.slider.setSingleStep(2)

        self.dial = QDial(self)
        self.dial.move(30, 50)
        self.dial.setRange(0, 50)

        btn = QPushButton('Default', self)
        btn.move(35, 160)

        self.slider.valueChanged.connect(self.dial.setValue)
        self.dial.valueChanged.connect(self.slider.setValue)
        btn.clicked.connect(self.button_clicked)

        self.setWindowTitle('QSlider and QDial')
        self.setGeometry(300, 300, 400, 200)
        self.show()

    def button_clicked(self):
        self.slider.setValue(0)
        self.dial.setValue(0)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-9. QSplitter.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QFrame, QSplitter
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        hbox = QHBoxLayout()

        top = QFrame()
        top.setFrameShape(QFrame.Box)

        midleft = QFrame()
        midleft.setFrameShape(QFrame.StyledPanel)

        midright = QFrame()
        midright.setFrameShape(QFrame.Panel)

        bottom = QFrame()
        bottom.setFrameShape(QFrame.WinPanel)
        bottom.setFrameShadow(QFrame.Sunken)

        splitter1 = QSplitter(Qt.Horizontal)
        splitter1.addWidget(midleft)
        splitter1.addWidget(midright)

        splitter2 = QSplitter(Qt.Vertical)
        splitter2.addWidget(top)
        splitter2.addWidget(splitter1)
        splitter2.addWidget(bottom)

        hbox.addWidget(splitter2)
        self.setLayout(hbox)

        self.setGeometry(300, 300, 300, 200)
        self.setWindowTitle('QSplitter')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-10. QGroupBox.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QGroupBox, QRadioButton
, QCheckBox, QPushButton, QMenu, QGridLayout, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.addWidget(self.createFirstExclusiveGroup(), 0, 0)
        grid.addWidget(self.createSecondExclusiveGroup(), 1, 0)
        grid.addWidget(self.createNonExclusiveGroup(), 0, 1)
        grid.addWidget(self.createPushButtonGroup(), 1, 1)

        self.setLayout(grid)

        self.setWindowTitle('Box Layout')
        self.setGeometry(300, 300, 480, 320)
        self.show()

    def createFirstExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        groupbox.setLayout(vbox)

        return groupbox

    def createSecondExclusiveGroup(self):
        groupbox = QGroupBox('Exclusive Radio Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(False)

        radio1 = QRadioButton('Radio1')
        radio2 = QRadioButton('Radio2')
        radio3 = QRadioButton('Radio3')
        radio1.setChecked(True)
        checkbox = QCheckBox('Independent Checkbox')
        checkbox.setChecked(True)

        vbox = QVBoxLayout()
        vbox.addWidget(radio1)
        vbox.addWidget(radio2)
        vbox.addWidget(radio3)
        vbox.addWidget(checkbox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createNonExclusiveGroup(self):
        groupbox = QGroupBox('Non-Exclusive Checkboxes')
        groupbox.setFlat(True)

        checkbox1 = QCheckBox('Checkbox1')
        checkbox2 = QCheckBox('Checkbox2')
        checkbox2.setChecked(True)
        tristatebox = QCheckBox('Tri-state Button')
        tristatebox.setTristate(True)

        vbox = QVBoxLayout()
        vbox.addWidget(checkbox1)
        vbox.addWidget(checkbox2)
        vbox.addWidget(tristatebox)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox

    def createPushButtonGroup(self):
        groupbox = QGroupBox('Push Buttons')
        groupbox.setCheckable(True)
        groupbox.setChecked(True)

        pushbutton = QPushButton('Normal Button')
        togglebutton = QPushButton('Toggle Button')
        togglebutton.setCheckable(True)
        togglebutton.setChecked(True)
        flatbutton = QPushButton('Flat Button')
        flatbutton.setFlat(True)
        popupbutton = QPushButton('Popup Button')
        menu = QMenu(self)
        menu.addAction('First Item')
        menu.addAction('Second Item')
        menu.addAction('Third Item')
        menu.addAction('Fourth Item')
        popupbutton.setMenu(menu)

        vbox = QVBoxLayout()
        vbox.addWidget(pushbutton)
        vbox.addWidget(togglebutton)
        vbox.addWidget(flatbutton)
        vbox.addWidget(popupbutton)
        vbox.addStretch(1)
        groupbox.setLayout(vbox)

        return groupbox


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-11. QTabWidget.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QTabWidget, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        tab1 = QWidget()
        tab2 = QWidget()

        tabs = QTabWidget()
        tabs.addTab(tab1, 'Tab1')
        tabs.addTab(tab2, 'Tab2')

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-11-1. QTabWidget (Advanced).

import sys
from PyQt5.QtWidgets import *


class MyApp(QDialog):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        tabs = QTabWidget()
        tabs.addTab(FirstTab(), 'First')
        tabs.addTab(SecondTab(), 'Second')
        tabs.addTab(ThirdTab(), 'Third')

        buttonbox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)
        buttonbox.accepted.connect(self.accept)
        buttonbox.rejected.connect(self.reject)

        vbox = QVBoxLayout()
        vbox.addWidget(tabs)
        vbox.addWidget(buttonbox)

        self.setLayout(vbox)

        self.setWindowTitle('QTabWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()


class FirstTab(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        name = QLabel('Name:')
        nameedit = QLineEdit()
        age = QLabel('Age:')
        ageedit = QLineEdit()
        nation = QLabel('Nation:')
        nationedit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(name)
        vbox.addWidget(nameedit)
        vbox.addWidget(age)
        vbox.addWidget(ageedit)
        vbox.addWidget(nation)
        vbox.addWidget(nationedit)
        vbox.addStretch()

        self.setLayout(vbox)


class SecondTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lan_group = QGroupBox('Select Your Language')
        combo = QComboBox()
        list = ['Korean', 'English', 'Chinese']
        combo.addItems(list)

        vbox1 = QVBoxLayout()
        vbox1.addWidget(combo)
        lan_group.setLayout(vbox1)

        learn_group = QGroupBox('Select What You Want To Learn')
        korean = QCheckBox('Korean')
        english = QCheckBox('English')
        chinese = QCheckBox('Chinese')

        vbox2 = QVBoxLayout()
        vbox2.addWidget(korean)
        vbox2.addWidget(english)
        vbox2.addWidget(chinese)
        learn_group.setLayout(vbox2)

        vbox = QVBoxLayout()
        vbox.addWidget(lan_group)
        vbox.addWidget(learn_group)
        self.setLayout(vbox)


class ThirdTab(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('Terms and Conditions')
        text_browser = QTextBrowser()
        text_browser.setText('This is the terms and conditions')
        checkbox = QCheckBox('Check the terms and conditions.')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(text_browser)
        vbox.addWidget(checkbox)

        self.setLayout(vbox)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-12. QPixmap.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt


class MyApp(QWidget):

 def __init__(self):
     super().__init__()
     self.initUI()

 def initUI(self):
     pixmap = QPixmap('minion.jpg')

     lbl_img = QLabel()
     lbl_img.setPixmap(pixmap)
     lbl_size = QLabel('Width: '+str(pixmap.width())+', Height: '+str(pixmap.height()))
     lbl_size.setAlignment(Qt.AlignCenter)

     vbox = QVBoxLayout()
     vbox.addWidget(lbl_img)
     vbox.addWidget(lbl_size)
     self.setLayout(vbox)

     self.setWindowTitle('QPixmap')
     self.move(300, 300)
     self.show()


if __name__ == '__main__':
 app = QApplication(sys.argv)
 ex = MyApp()
 sys.exit(app.exec_())
'''

"""
## Ex 5-13. QCalenderWidget.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QCalendarWidget
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cal = QCalendarWidget(self)
        cal.setGridVisible(True)
        cal.clicked[QDate].connect(self.showDate)

        self.lbl = QLabel(self)
        date = cal.selectedDate()
        self.lbl.setText(date.toString())

        vbox = QVBoxLayout()
        vbox.addWidget(cal)
        vbox.addWidget(self.lbl)

        self.setLayout(vbox)

        self.setWindowTitle('QCalendarWidget')
        self.setGeometry(300, 300, 400, 300)
        self.show()

    def showDate(self, date):
        self.lbl.setText(date.toString())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-14. QSpinBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QSpinBox')
        self.spinbox = QSpinBox()
        self.spinbox.setMinimum(-10)
        self.spinbox.setMaximum(30)
        # self.spinbox.setRange(-10, 30)
        self.spinbox.setSingleStep(2)
        self.lbl2 = QLabel('0')

        self.spinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.spinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText(str(self.spinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-15. QDoubleSpinBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDoubleSpinBox, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('QDoubleSpinBox')
        self.dspinbox = QDoubleSpinBox()
        self.dspinbox.setRange(0, 100)
        self.dspinbox.setSingleStep(0.5)
        self.dspinbox.setPrefix('$ ')
        self.dspinbox.setDecimals(1)
        self.lbl2 = QLabel('$ 0.0')

        self.dspinbox.valueChanged.connect(self.value_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.dspinbox)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDoubleSpinBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def value_changed(self):
        self.lbl2.setText('$ ' + str(self.dspinbox.value()))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 """

'''
## Ex 5-16. QDateEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateEdit, QVBoxLayout
from PyQt5.QtCore import QDate


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QDateEdit')

        dateedit = QDateEdit(self)
        dateedit.setDate(QDate.currentDate())
        dateedit.setMinimumDate(QDate(1900, 1, 1))
        dateedit.setMaximumDate(QDate(2100, 12, 31))
        # dateedit.setDateRange(QDate(1900, 1, 1), QDate(2100, 12, 31))

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(dateedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-17. QTimeEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTimeEdit, QVBoxLayout
from PyQt5.QtCore import QTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        timeedit = QTimeEdit(self)
        timeedit.setTime(QTime.currentTime())
        timeedit.setTimeRange(QTime(3, 00, 00), QTime(23, 30, 00))
        timeedit.setDisplayFormat('hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(timeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-18. QDateTimeEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QDateTimeEdit, QVBoxLayout
from PyQt5.QtCore import QDateTime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lbl = QLabel('QTimeEdit')

        datetimeedit = QDateTimeEdit(self)
        datetimeedit.setDateTime(QDateTime.currentDateTime())
        datetimeedit.setDateTimeRange(QDateTime(1900, 1, 1, 00, 00, 00), QDateTime(2100, 1, 1, 00, 00, 00))
        datetimeedit.setDisplayFormat('yyyy.MM.dd hh:mm:ss')

        vbox = QVBoxLayout()
        vbox.addWidget(lbl)
        vbox.addWidget(datetimeedit)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QDateTimeEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-19. QTextBrowser.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QLineEdit, QTextBrowser, QPushButton, QVBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.returnPressed.connect(self.append_text)

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        self.clear_btn = QPushButton('Clear')
        self.clear_btn.pressed.connect(self.clear_text)

        vbox = QVBoxLayout()
        vbox.addWidget(self.le, 0)
        vbox.addWidget(self.tb, 1)
        vbox.addWidget(self.clear_btn, 2)

        self.setLayout(vbox)

        self.setWindowTitle('QTextBrowser')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def append_text(self):
        text = self.le.text()
        self.tb.append(text)
        self.le.clear()

    def clear_text(self):
        self.tb.clear()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-19-1. QTextBrowser (Advanced).

import sys
from PyQt5.QtWidgets import *
import requests
from bs4 import BeautifulSoup


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.le = QLineEdit()
        self.le.setPlaceholderText('Enter your search word')
        self.le.returnPressed.connect(self.crawl_news)

        self.btn = QPushButton('Search')
        self.btn.clicked.connect(self.crawl_news)

        self.lbl = QLabel('')

        self.tb = QTextBrowser()
        self.tb.setAcceptRichText(True)
        self.tb.setOpenExternalLinks(True)

        grid = QGridLayout()
        grid.addWidget(self.le, 0, 0, 1, 3)
        grid.addWidget(self.btn, 0, 3, 1, 1)
        grid.addWidget(self.lbl, 1, 0, 1, 4)
        grid.addWidget(self.tb, 2, 0, 1, 4)

        self.setLayout(grid)

        self.setWindowTitle('Web Crawler')
        self.setGeometry(100, 100, 700, 450)
        self.show()

    def crawl_news(self):
        search_word = self.le.text()

        if search_word:
            self.lbl.setText('BBC Search Results for "' + search_word + '"')
            self.tb.clear()
            url_search = 'https://www.bbc.co.uk/search?q='
            url = url_search + search_word
            r = requests.get(url)
            html = r.content
            soup = BeautifulSoup(html, 'html.parser')
            titles_html = soup.select('.search-results > li > article > div > h1 > a')

            for i in range(len(titles_html)):
                title = titles_html[i].text
                link = titles_html[i].get('href')
                self.tb.append(str(i + 1) + '. ' + title + ' (' + '<a href="' + link + '">Link</a>' + ')')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-20. QTextEdit.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lbl1 = QLabel('Enter your sentence:')
        self.te = QTextEdit()
        self.te.setAcceptRichText(False)
        self.lbl2 = QLabel('The number of words is 0')

        self.te.textChanged.connect(self.text_changed)

        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.te)
        vbox.addWidget(self.lbl2)
        vbox.addStretch()

        self.setLayout(vbox)

        self.setWindowTitle('QTextEdit')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def text_changed(self):
        text = self.te.toPlainText()
        self.lbl2.setText('The number of words is ' + str(len(text.split())))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 5-21. QTableWidget.

import sys
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        # self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked)
        # self.tableWidget.setEditTriggers(QAbstractItemView.AllEditTriggers)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)

        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(i+j)))

        layout = QVBoxLayout()
        layout.addWidget(self.tableWidget)
        self.setLayout(layout)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 5-21-1. QTableWidget (Advanced).

import sys
import numpy as np
from PyQt5.QtWidgets import *


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.set_rand_int()

    def initUI(self):

        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(4)

        self.label = QLabel('')

        self.scrollToTop = QPushButton('Scroll to Top')
        self.scrollToTop.clicked.connect(self.tableWidget.scrollToTop)
        self.scrollToBottom = QPushButton('Scroll to Bottom')
        self.scrollToBottom.clicked.connect(self.tableWidget.scrollToBottom)
        self.setItems = QPushButton('Set Items')
        self.setItems.clicked.connect(self.set_rand_int)
        self.clear = QPushButton('Clear')
        self.clear.clicked.connect(self.tableWidget.clear)

        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.tableWidget.cellClicked.connect(self.set_label)

        hbox = QHBoxLayout()
        hbox.addWidget(self.scrollToTop)
        hbox.addWidget(self.scrollToBottom)
        hbox.addWidget(self.setItems)
        hbox.addWidget(self.clear)

        vbox = QVBoxLayout()
        vbox.addWidget(self.tableWidget)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        self.setWindowTitle('QTableWidget')
        self.setGeometry(300, 100, 600, 400)
        self.show()

    def set_rand_int(self):
        rand_int = np.random.randint(1, 100, size=(20, 4))
        for i in range(20):
            for j in range(4):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(rand_int[i, j])))

    def set_label(self, row, column):
        item = self.tableWidget.item(row, column)
        value = item.text()
        label_str = 'Row: ' + str(row+1) + ', Column: ' + str(column+1) + ', Value: ' + str(value)
        self.label.setText(label_str)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 6-1. QInputDialog.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLineEdit, QInputDialog


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.le = QLineEdit(self)
        self.le.move(120, 35)

        self.setWindowTitle('Input dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        text, ok = QInputDialog.getText(self, 'Input Dialog', 'Enter your name:')

        if ok:
            self.le.setText(str(text))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 6-2. QColorDialog.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFrame, QColorDialog
from PyQt5.QtGui import QColor


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        col = QColor(0, 0, 0)

        self.btn = QPushButton('Dialog', self)
        self.btn.move(30, 30)
        self.btn.clicked.connect(self.showDialog)

        self.frm = QFrame(self)
        self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())
        self.frm.setGeometry(130, 35, 100, 100)

        self.setWindowTitle('Color Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        col = QColorDialog.getColor()

        if col.isValid():
            self.frm.setStyleSheet('QWidget { background-color: %s }' % col.name())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 6-3. QFontDialog.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QVBoxLayout
, QPushButton, QSizePolicy, QLabel, QFontDialog)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        btn = QPushButton('Dialog', self)
        btn.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        btn.move(20, 20)
        btn.clicked.connect(self.showDialog)

        vbox = QVBoxLayout()
        vbox.addWidget(btn)

        self.lbl = QLabel('The quick brown fox jumps over the lazy dog', self)
        self.lbl.move(130, 20)

        vbox.addWidget(self.lbl)
        self.setLayout(vbox)

        self.setWindowTitle('Font Dialog')
        self.setGeometry(300, 300, 250, 180)
        self.show()

    def showDialog(self):
        font, ok = QFontDialog.getFont()

        if ok:
           self.lbl.setFont(font)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 6-4. QFileDialog.

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTextEdit, QAction, QFileDialog
from PyQt5.QtGui import QIcon


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)
        self.statusBar()

        openFile = QAction(QIcon('open.png'), 'Open', self)
        openFile.setShortcut('Ctrl+O')
        openFile.setStatusTip('Open New File')
        openFile.triggered.connect(self.showDialog)

        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        fileMenu = menubar.addMenu('&File')
        fileMenu.addAction(openFile)

        self.setWindowTitle('File Dialog')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def showDialog(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file', './')

        if fname[0]:
            f = open(fname[0], 'r')

            with f:
                data = f.read()
                self.textEdit.setText(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 6-5. QMessageBox.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('QMessageBox')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Message', 'Are you sure to quit?',
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = MyApp()
   sys.exit(app.exec_())
'''

"""
## Ex 7-1. 연결하기.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLCDNumber, QDial, QVBoxLayout


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(300, 300, 200, 200)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 7-2. 이벤트 핸들러 만들기.

import sys
from PyQt5.QtWidgets import (QApplication, QWidget
, QLCDNumber, QDial, QPushButton, QVBoxLayout, QHBoxLayout)


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        dial = QDial(self)
        btn1 = QPushButton('Big', self)
        btn2 = QPushButton('Small', self)

        hbox = QHBoxLayout()
        hbox.addWidget(btn1)
        hbox.addWidget(btn2)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(dial)
        vbox.addLayout(hbox)
        self.setLayout(vbox)

        dial.valueChanged.connect(lcd.display)
        btn1.clicked.connect(self.resizeBig)
        btn2.clicked.connect(self.resizeSmall)

        self.setWindowTitle('Signal and Slot')
        self.setGeometry(200, 200, 200, 250)
        self.show()

    def resizeBig(self):
        self.resize(400, 500)

    def resizeSmall(self):
        self.resize(200, 250)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 7-3. 이벤트 핸들러 재구성하기.

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
        elif e.key() == Qt.Key_F:
            self.showFullScreen()
        elif e.key() == Qt.Key_N:
            self.showNormal()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 7-4. 이벤트 핸들러 재구성하기2.

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        x = 0
        y = 0

        self.text = 'x: {0}, y: {1}'.format(x, y)
        self.label = QLabel(self.text, self)
        self.label.move(20, 20)

        self.setMouseTracking(True)

        self.setWindowTitle('Reimplementing event handler')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = 'x: {0}, y: {1}'.format(x, y)
        self.label.setText(text)
        self.label.adjustSize()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
'''

"""
## Ex 7-5. 사용자 정의 시그널.

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QApplication, QMainWindow


class Communicate(QObject):

    closeApp = pyqtSignal()


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setWindowTitle('Emitting Signal')
        self.setGeometry(300, 300, 300, 200)
        self.show()

    def mousePressEvent(self, e):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 """

'''
## Ex 8-1-1. 점 그리기1 (drawPoint).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('Points')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_point(qp)
        qp.end()

    def draw_point(self, qp):
        qp.setPen(QPen(Qt.blue,  8))
        qp.drawPoint(self.width()/2, self.height()/2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 '''

"""
## Ex 8-2. 직선 그리기 (drawLine).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawLine')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_line(qp)
        qp.end()

    def draw_line(self, qp):
        qp.setPen(QPen(Qt.black, 3, Qt.SolidLine))
        qp.drawLine(20, 20, 380, 20)
        qp.drawText(30, 40, 'Qt.SolidLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashLine))
        qp.drawLine(20, 70, 380, 70)
        qp.drawText(30, 90, 'Qt.DashLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DotLine))
        qp.drawLine(20, 120, 380, 120)
        qp.drawText(30, 140, 'Qt.DotLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashDotLine))
        qp.drawLine(20, 170, 380, 170)
        qp.drawText(30, 190, 'Qt.DashDotLine')

        qp.setPen(QPen(Qt.black, 3, Qt.DashDotDotLine))
        qp.drawLine(20, 220, 380, 220)
        qp.drawText(30, 240, 'Qt.DashDotDotLine')

        pen = QPen(Qt.black, 3, Qt.CustomDashLine)
        pen.setDashPattern([4, 3, 2, 5])
        qp.setPen(pen)
        qp.drawLine(20, 270, 380, 270)
        qp.drawText(30, 290, 'Qt.CustomDashLine')
        
'''
    def draw_line(self, qp):
        qp.setPen(QPen(Qt.blue, 8))
        qp.drawLine(30, 230, 200, 50)
        qp.setPen(QPen(Qt.green, 12))
        qp.drawLine(140, 60, 320, 280)
        qp.setPen(QPen(Qt.red, 16))
        qp.drawLine(330, 250, 40, 190)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 8-3. 직사각형 그리기 (drawRect).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_rect(qp)
        qp.end()

    def draw_rect(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 10, 100, 60)
        qp.drawText(20, 90, 'Qt.SolidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRect(150, 10, 100, 60)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRect(280, 10, 100, 60)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 110, 100, 60)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRect(150, 110, 100, 60)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRect(280, 110, 100, 60)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(20, 210, 100, 60)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRect(150, 210, 100, 60)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRect(280, 210, 100, 60)
        qp.drawText(280, 290, 'Qt.DiagCrossPattern')
'''
    def draw_rect(self, qp):
        qp.setBrush(QColor(180, 100, 160))
        qp.setPen(QPen(QColor(60, 60, 60), 3))
        qp.drawRect(20, 20, 100, 100)

        qp.setBrush(QColor(40, 150, 20))
        qp.setPen(QPen(Qt.blue, 2))
        qp.drawRect(180, 120, 50, 120)

        qp.setBrush(Qt.yellow)
        qp.setPen(QPen(Qt.red, 5))
        qp.drawRect(280, 30, 80, 40)
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 8-4. 둥근 직사각형 그리기 (drawRoundedRect).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawRoundedRect')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_roundedrect(qp)
        qp.end()

    def draw_roundedrect(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 10, 100, 60, 15, 15)
        qp.drawText(20, 90, 'Qt.SolidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 10, 100, 60, 15, 15)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 10, 100, 60, 15, 15)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 110, 100, 60, 15, 15)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 110, 100, 60, 15, 15)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 110, 100, 60, 15, 15)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(20, 210, 100, 60, 15, 15)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(150, 210, 100, 60, 15, 15)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawRoundedRect(280, 210, 100, 60, 15, 15)
        qp.drawText(280, 290, 'Qt.DiagCrossPattern')
    
'''
    def draw_roundedrect(self, qp):
        qp.setPen(QPen(Qt.black, 3))

        qp.drawRoundedRect(20, 20, 100, 100, 0, 0)
        qp.drawText(40, 140, 'radius: 0')

        qp.drawRoundedRect(150, 20, 100, 100, 10, 10)
        qp.drawText(170, 140, 'radius: 10')

        qp.drawRoundedRect(280, 20, 100, 100, 20, 20)
        qp.drawText(300, 140, 'radius: 20')

        qp.drawRoundedRect(20, 160, 100, 100, 30, 30)
        qp.drawText(40, 280, 'radius: 30')

        qp.drawRoundedRect(150, 160, 100, 100, 40, 40)
        qp.drawText(170, 280, 'radius: 40')

        qp.drawRoundedRect(280, 160, 100, 100, 50, 50)
        qp.drawText(300, 280, 'radius: 50')
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

'''
## Ex 8-5. 다각형 그리기 (drawPolygon).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont, QPolygon
from PyQt5.QtCore import Qt, QPoint


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPolygon')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_polygon(qp)
        qp.end()

    def draw_polygon(self, qp):
        points1 = [
            QPoint(20, 20),
            QPoint(200, 80),
            QPoint(150, 135),
            QPoint(50, 115)
        ]
        polygon1 = QPolygon(points1)
        qp.setPen(QPen(Qt.black, 3))
        qp.drawPolygon(polygon1)

        points2 = [
            QPoint(220, 30),
            QPoint(360, 10),
            QPoint(250, 135)
        ]
        polygon2 = QPolygon(points2)
        qp.setPen(QPen(Qt.red, 5, Qt.DashLine))
        qp.setBrush(QBrush(Qt.yellow))
        qp.drawPolygon(polygon2)

        points3 = [
            QPoint(95, 140),
            QPoint(120, 190),
            QPoint(185, 205),
            QPoint(125, 230),
            QPoint(140, 280),
            QPoint(100, 230),
            QPoint(70, 280),
            QPoint(60, 220),
            QPoint(15, 190),
            QPoint(65, 180),
        ]
        polygon3 = QPolygon(points3)
        qp.setPen(QPen(QColor('#1C91CF'), 4, Qt.DashDotDotLine))
        qp.setBrush(QBrush(QColor('#37CF1C'), Qt.CrossPattern))
        qp.drawPolygon(polygon3)

        points4 = [
            QPoint(290, 160),
            QPoint(360, 190),
            QPoint(335, 280),
            QPoint(255, 270),
            QPoint(230, 195)
        ]
        polygon4 = QPolygon(points4)
        qp.setPen(QPen(QColor('#7B33D1'), 3))
        qp.setBrush(QBrush(QColor('#D187EF')))
        qp.drawPolygon(polygon4)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 '''

"""
## Ex 8-6. 타원 그리기 (drawEllipse).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawEllipse')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_ellipse(qp)
        qp.end()

    def draw_ellipse(self, qp):

        qp.setPen(QPen(Qt.black, 3))
        qp.drawEllipse(40, 20, 80, 100)

        qp.setPen(QPen(Qt.green, 5, Qt.DashLine))
        qp.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        qp.drawEllipse(200, 20, 120, 40)

        qp.setPen(QPen(Qt.blue, 2, Qt.DotLine))
        qp.setBrush((QBrush(Qt.CrossPattern)))
        qp.drawEllipse(70, 140, 180, 120)

        qp.setPen(QPen(Qt.red, 2, Qt.DashDotDotLine))
        qp.setBrush((QBrush(Qt.blue, Qt.FDiagPattern)))
        qp.drawEllipse(290, 100, 80, 120)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 """

'''
## Ex 8-7. 호 그리기 (drawArc).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawArc')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_arc(qp)
        qp.end()

    def draw_arc(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawArc(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30°')

        qp.drawArc(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60°')

        qp.drawArc(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90°')

        qp.drawArc(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180°')

        qp.drawArc(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270°')

        qp.drawArc(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360°')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
 '''

"""
## Ex 8-8. 현 그리기 (drawChord).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawChord')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_chord(qp)
        qp.end()

    def draw_chord(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawChord(20, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(20, 90, 'Qt.SolidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawChord(150, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawChord(280, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawChord(20, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawChord(150, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawChord(280, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawChord(20, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawChord(150, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawChord(280, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(270, 290, 'Qt.DiagCrossPattern')
'''
    def draw_chord(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawChord(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30°')

        qp.drawChord(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60°')

        qp.drawChord(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90°')

        qp.drawChord(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180°')

        qp.drawChord(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270°')

        qp.drawChord(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360°')
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 8-9. 파이 그리기 (drawPie).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush
from PyQt5.QtCore import Qt


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 400, 300)
        self.setWindowTitle('drawPie')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_pie(qp)
        qp.end()

    def draw_pie(self, qp):
        brush = QBrush(Qt.SolidPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(20, 90, 'Qt.SolidPattern')

        brush = QBrush(Qt.Dense1Pattern)
        qp.setBrush(brush)
        qp.drawPie(150, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(150, 90, 'Qt.Dense1Pattern')

        brush = QBrush(Qt.Dense2Pattern)
        qp.setBrush(brush)
        qp.drawPie(280, 10, 100, 100, 30 * 16, 120 * 16)
        qp.drawText(280, 90, 'Qt.Dense2Pattern')

        brush = QBrush(Qt.HorPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(20, 190, 'Qt.HorPattern')

        brush = QBrush(Qt.VerPattern)
        qp.setBrush(brush)
        qp.drawPie(150, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(150, 190, 'Qt.VerPattern')

        brush = QBrush(Qt.CrossPattern)
        qp.setBrush(brush)
        qp.drawPie(280, 110, 100, 100, 0 * 16, 135 * 16)
        qp.drawText(280, 190, 'Qt.CrossPattern')

        brush = QBrush(Qt.BDiagPattern)
        qp.setBrush(brush)
        qp.drawPie(20, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(20, 290, 'Qt.BDiagPattern')

        brush = QBrush(Qt.FDiagPattern)
        qp.setBrush(brush)
        qp.drawPie(150, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(150, 290, 'Qt.FDiagPattern')

        brush = QBrush(Qt.DiagCrossPattern)
        qp.setBrush(brush)
        qp.drawPie(280, 210, 100, 100, 45 * 16, 135 * 16)
        qp.drawText(270, 290, 'Qt.DiagCrossPattern')
'''
    def draw_pie(self, qp):
        qp.setPen(QPen(Qt.black, 3))
        qp.drawPie(20, 20, 100, 100, 0 * 16, 30 * 16)
        qp.drawText(60, 100, '30°')

        qp.drawPie(150, 20, 100, 100, 0 * 16, 60 * 16)
        qp.drawText(190, 100, '60°')

        qp.drawPie(280, 20, 100, 100, 0 * 16, 90 * 16)
        qp.drawText(320, 100, '90°')

        qp.drawPie(20, 140, 100, 100, 0 * 16, 180 * 16)
        qp.drawText(60, 270, '180°')

        qp.drawPie(150, 140, 100, 100, 0 * 16, 270 * 16)
        qp.drawText(190, 270, '270°')

        qp.drawPie(280, 140, 100, 100, 0 * 16, 360 * 16)
        qp.drawText(320, 270, '360°')
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 8-10. 텍스트 그리기 (drawText).

import sys
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPainter, QPen, QColor, QBrush, QFont
from PyQt5.QtCore import Qt, QRect


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('drawText')
        self.show()

    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.draw_text(qp)
        qp.end()

    def draw_text(self, qp):
        rect1 = QRect(10, 15, 210, 60)
        qp.drawRect(rect1)
        qp.drawText(rect1, Qt.AlignHCenter, 'AlignHCenter')

        rect2 = QRect(230, 15, 210, 60)
        qp.drawRect(rect2)
        qp.drawText(rect2, Qt.AlignRight, 'AlignRight')

        rect3 = QRect(10, 85, 210, 60)
        qp.drawRect(rect3)
        qp.drawText(rect3, Qt.AlignVCenter, 'AlignVCenter')

        rect4 = QRect(230, 85, 210, 60)
        qp.drawRect(rect4)
        qp.drawText(rect4, Qt.AlignCenter, 'AlignCenter')

        rect5 = QRect(10, 155, 210, 60)
        qp.drawRect(rect5)
        qp.drawText(rect5, Qt.AlignVCenter | Qt.AlignRight, 'AlignVCenter | AlignRight')

        rect6 = QRect(230, 155, 210, 60)
        qp.drawRect(rect6)
        qp.drawText(rect6, Qt.AlignBottom, 'AlignBottom')

        rect7 = QRect(10, 225, 210, 60)
        qp.drawRect(rect7)
        qp.drawText(rect7, Qt.AlignBottom | Qt.AlignHCenter, 'AlignBottom | AlignHCenter')

        rect8 = QRect(230, 225, 210, 60)
        qp.drawRect(rect8)
        qp.drawText(rect8, Qt.AlignBottom | Qt.AlignRight, 'AlignBottom | AlignRight')

'''
    def draw_text(self, qp):
        qp.drawText(20, 40, 'Default')

        qp.setFont(QFont('Arial', 16))
        qp.drawText(150, 40, 'Arial, 16 pts')

        qp.setFont(QFont('Arial', 18))
        qp.drawText(290, 40, 'Arial, 18 pts')

        qp.setFont(QFont('Times New Roman', 14))
        qp.drawText(20, 90, 'Times New Roman')
        qp.drawText(20, 110, '14 pts')

        qp.setFont(QFont('Times New Roman', 16))
        qp.drawText(150, 90, 'Times New Roman')
        qp.drawText(150, 110, '16 pts')

        qp.setFont(QFont('Times New Roman', 18))
        qp.drawText(290, 90, 'Times New Roman')
        qp.drawText(290, 110, '18 pts')

        qp.setFont(QFont('Consolas', 14))
        qp.drawText(20, 160, 'Consolas')
        qp.drawText(20, 180, '14 pts')

        qp.setFont(QFont('Consolas', 16))
        qp.drawText(150, 160, 'Consolas')
        qp.drawText(150, 180, '16 pts')

        qp.setFont(QFont('Consolas', 18))
        qp.drawText(290, 160, 'Consolas')
        qp.drawText(290, 180, '18 pts')

        qp.setFont(QFont('Courier New', 14, italic=True))
        qp.drawText(20, 220, 'Courier New')
        qp.drawText(20, 240, '14 pts')
        qp.drawText(20, 260, 'Italic')

        qp.setFont(QFont('Courier New', 16, italic=True))
        qp.drawText(150, 220, 'Courier New')
        qp.drawText(150, 240, '16 pts')
        qp.drawText(150, 260, 'Italic')

        qp.setFont(QFont('Courier New', 18, italic=True))
        qp.drawText(290, 220, 'Courier New')
        qp.drawText(290, 240, '18 pts')
        qp.drawText(290, 260, 'Italic')
'''

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-1. (x, y) 위치 반복 클릭 프로그램.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.x_le = QLineEdit(self)
        self.y_le = QLineEdit(self)
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Start', self)

        self.x, self.y, self.delay = 0, 0, 0
        self.num_click = 0
        self.initUI()

    def initUI(self):
        self.x_le.move(20, 20)
        self.x_le.setPlaceholderText('x 위치')

        self.y_le.move(160, 20)
        self.y_le.setPlaceholderText('y 위치')

        self.delay_le.move(20, 60)
        self.delay_le.setPlaceholderText('클릭 사이 간격 (초)')

        self.num_le.move(160, 60)
        self.num_le.setPlaceholderText('클릭 횟수')

        self.start_btn.move(110, 100)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Click')
        self.setGeometry(400, 400, 300, 150)
        self.show()

    def start_btn_click(self):
        self.timer = QTimer()
        self.x = int(self.x_le.text())
        self.y = int(self.y_le.text())
        self.delay = int(self.delay_le.text())
        self.num_click = 0

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        self.num_click += 1

        if self.num_click == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-2. (x, y) 위치 반복 클릭 프로그램2.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.x_le = QLineEdit(self)
        self.y_le = QLineEdit(self)
        self.x_le2 = QLineEdit(self)
        self.y_le2 = QLineEdit(self)
        self.x_le3 = QLineEdit(self)
        self.y_le3 = QLineEdit(self)
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Start', self)

        self.x, self.y = 0, 0
        self.x2, self.y2 = 0, 0
        self.x3, self.y3 = 0, 0
        self.delay, self.num_click = 0, 0
        self.initUI()

    def initUI(self):
        self.x_le.move(20, 20)
        self.x_le.setPlaceholderText('x 위치')
        self.x_le2.move(20, 50)
        self.x_le2.setPlaceholderText('x 위치2')
        self.x_le3.move(20, 80)
        self.x_le3.setPlaceholderText('x 위치3')

        self.y_le.move(160, 20)
        self.y_le.setPlaceholderText('y 위치')
        self.y_le2.move(160, 50)
        self.y_le2.setPlaceholderText('y 위치2')
        self.y_le3.move(160, 80)
        self.y_le3.setPlaceholderText('y 위치3')

        self.delay_le.move(20, 110)
        self.delay_le.setPlaceholderText('클릭 사이 간격 (초)')

        self.num_le.move(160, 110)
        self.num_le.setPlaceholderText('클릭 횟수')

        self.start_btn.move(110, 150)
        self.start_btn.clicked.connect(self.start_btn_click)

        self.setWindowTitle('Click')
        self.setGeometry(400, 400, 300, 200)
        self.show()

    def start_btn_click(self):
        self.timer = QTimer()
        self.x, self.y = int(self.x_le.text()), int(self.y_le.text())
        self.x2, self.y2 = int(self.x_le2.text()), int(self.y_le2.text())
        self.x3, self.y3 = int(self.x_le3.text()), int(self.y_le3.text())
        self.delay = int(self.delay_le.text())
        self.num_click = 0

        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.mouse_click)

    def mouse_click(self):
        pyautogui.click(self.x, self.y)
        pyautogui.click(self.x2, self.y2)
        pyautogui.click(self.x3, self.y3)
        self.num_click += 1

        if self.num_click == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-3. 구글 번역기 프로그램.

import sys
from PyQt5.QtWidgets import *
from googletrans import Translator


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.lbl1 = QLabel('한국어:', self)
        self.lbl2 = QLabel('영어:', self)
        self.le = QLineEdit(self)
        self.te = QTextEdit(self)
        self.trans_btn = QPushButton('번역', self)
        self.translator = Translator()
        self.initUI()

    def initUI(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.lbl1)
        vbox.addWidget(self.le)
        vbox.addWidget(self.lbl2)
        vbox.addWidget(self.te)
        vbox.addWidget(self.trans_btn)
        self.setLayout(vbox)

        self.trans_btn.clicked.connect(self.translate_kor)
        self.le.editingFinished.connect(self.translate_kor)

        self.setWindowTitle('Google Translator')
        self.setGeometry(200, 200, 400, 300)
        self.show()

    def translate_kor(self):
        text_kor = self.le.text()
        text_en = self.translator.translate(text_kor).text
        self.te.setText(text_en)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-4. 화면 캡처 프로그램.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QTimer
import pyautogui
import datetime


class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.delay_le = QLineEdit(self)
        self.num_le = QLineEdit(self)
        self.start_btn = QPushButton('Capture', self)

        self.delay, self.num_cap = 0, 0
        self.initUI()

    def initUI(self):
        self.delay_le.setPlaceholderText('캡처 간격 (초)')
        self.num_le.setPlaceholderText('캡처 횟수')
        self.start_btn.clicked.connect(self.start_btn_click)

        hbox = QHBoxLayout()
        hbox.addWidget(self.delay_le)
        hbox.addWidget(self.num_le)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox)
        vbox.addWidget(self.start_btn)

        self.setLayout(vbox)

        self.setWindowTitle('Capture')
        self.setGeometry(200, 200, 300, 150)
        self.show()

    def start_btn_click(self):
        self.delay = int(self.delay_le.text())
        self.num_cap = 0
        self.timer = QTimer()
        self.timer.start(self.delay * 1000)
        self.timer.timeout.connect(self.capture)

    def capture(self):
        today = str(datetime.datetime.today())
        pyautogui.screenshot(today + '.png')
        self.num_cap += 1

        if self.num_cap == int(self.num_le.text()):
            self.timer.stop()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-5. 간단한 그림판 프로그램.

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
## Ex 10-6. MNIST 손글씨 인식 프로그램.

import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import numpy as np
import tensorflow as tf


class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(400, 400), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 30
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.loaded_model = None
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu = menubar.addMenu('File')

        load_model_action = QAction('Load model', self)
        load_model_action.setShortcut('Ctrl+L')
        load_model_action.triggered.connect(self.load_model)

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu.addAction(load_model_action)
        filemenu.addAction(save_action)
        filemenu.addAction(clear_action)

        self.statusbar = self.statusBar()

        self.setWindowTitle('MNIST Classifier')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = True
            self.last_point = e.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() & Qt.LeftButton) & self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(self.brush_color, self.brush_size, Qt.SolidLine, Qt.RoundCap))
            painter.drawLine(self.last_point, e.pos())
            self.last_point = e.pos()
            self.update()

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

            arr = np.zeros((28, 28))
            for i in range(28):
                for j in range(28):
                    arr[j, i] = 1 - self.image.scaled(28, 28).pixelColor(i, j).getRgb()[0] / 255.0
            arr = arr.reshape(-1, 28, 28)

            if self.loaded_model:
                pred = self.loaded_model.predict(arr)[0]
                pred_num = str(np.argmax(pred))
                self.statusbar.showMessage('숫자 ' + pred_num + '입니다.')

    def load_model(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'Load Model', '')

        if fname:
            self.loaded_model = tf.keras.models.load_model(fname)
            self.statusbar.showMessage('Model loaded.')

    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.scaled(28, 28).save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()
        self.statusbar.clearMessage()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
"""

"""
import tensorflow as tf

# 1. MNIST 데이터넷 임포트
mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()

# 2. 데이터 전처리
x_train, x_test = x_train/255.0, x_test/255.0

# 3. 모델 구성
model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# 4. 모델 컴파일
model.compile(optimizer='adam',
            loss='sparse_categorical_crossentropy',
            metrics=['accuracy'])

# 5. 모델 훈련
model.fit(x_train, y_train, epochs=5)

# 6. 모델 저장
model.save('model1.h5')
"""

"""
import tensorflow as tf

mnist = tf.keras.datasets.mnist
(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train/255.0, x_test/255.0

# 모델 복원
loaded_model = tf.keras.models.load_model('model1.h5')
loaded_model.summary()

loss, acc = loaded_model.evaluate(x_test, y_test, verbose=2)
print('Loss: ', loss)
print('Acc: ', acc)
"""
"""
## Python 선 그래프 그리기

import matplotlib.pyplot as plt
import matplotlib.legend as legend
index=[0.7, 0.6, 0.5, 0.4, 0.3, 0.2, 0.1, 0]
#GABDR=[0.86, 1, 0.98, 0.98, 0.99, 0.98, 0.99, 1]
GABDR=[0, 0.51, 0.37, 0.87, 0.41, 0.33, 0.56, 0.65]
gab,=plt.plot(index, GABDR, 'ro-')
#plt.plot(index, GABFPR, 'ro-')
RABDR=[0.94, 0.99, 0.99, 0.97, 0.99, 0.96, 0.90, 1]
RABDR=[0.06, 0.39, 0.53, 0.43, 0.29, 0.42, 0.41, 0.34]
rab,=plt.plot(index, RABDR, 'g^-')
#plt.plot(index, RABFPR, 'r^-')
#DABDR=[0.93, 0.99, 0.99, 1, 1, 0.98, 0.99, 1]
DABDR=[0.39, 0.84, 0.82, 0.84, 0.90, 0.54, 0.62, 0.66]
dab,=plt.plot(index, DABDR, 'bs-')
#plt.plot(index, RABFPR, 'r^-')
plt.legend([dab, rab, gab],['DAB','RAB','RAB'], loc=3)
plt.xlabel('FPR of Stage')
plt.ylabel('False Positive Rate')
plt.axis([-0.05,0.75, 0.0, 1.05])
plt.grid(True)
plt.show()
"""
