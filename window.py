
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QTextCursor
from utils import Scientist


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Set window title and size
        self.setWindowTitle('计算机科学家查询工具')
        self.setGeometry(300, 300, 500, 500)

        # Create labels and text boxes
        self.label = QLabel(self)
        self.label.setText('请输入计算机科学家的名字:')
        # self.label.setFont(QFont("Arial", 12))
        self.label.move(50, 50)
        self.textbox = QLineEdit(self)
        self.textbox.move(50, 80)
        self.textbox.resize(400, 30)

        # Create Button
        self.button = QPushButton('查询', self)
        self.button.move(375, 120)
        self.button.resize(75, 30)
        self.button.clicked.connect(self.get_results)

        # Create a sliding text box
        self.textedit = QTextBrowser()
        self.textedit.move(50, 160)
        self.textedit.resize(400, 300)
        self.textedit.setReadOnly(True)
        self.textedit.setOpenExternalLinks(True)
        self.scrollbar = self.textedit.verticalScrollBar()

        # Create layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.textedit)
        self.hlayout = QHBoxLayout()
        self.hlayout.addWidget(self.label)
        self.hlayout.addWidget(self.textbox)
        self.hlayout.addWidget(self.button)
        self.layout.addLayout(self.hlayout)
        self.setLayout(self.layout)

    # def get_name(self):
    #     return self.textbox.text()
    
    def get_results(self):
        name = self.textbox.text()
        scientist = Scientist(name)
        link = scientist.get_scientist_link()
        results = scientist.get_articlelist(link)
        self.textedit.clear()
        self.show_results(results)

    def show_results(self, results):
        # Add text to the text box
        for item in results:
            self.textedit.append('<a >{}</a> <br/> (<a href="{}">{}</a>)'.format(item['title'], item['link'], item['link']))

        # Slide
        self.scrollbar.setValue(self.scrollbar.maximum())