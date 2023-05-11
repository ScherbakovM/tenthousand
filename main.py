from datetime import datetime
from PySide6 import QtWidgets
from PySide6.QtWidgets import *
from PySide6 import QtCore
from PySide6.QtCore import *
import pygame

import sys

pygame.init()
FPS = 60
pygame.mixer.music.load("alarm.wav")
pygame.mixer.music.set_volume(0.3)
clock = pygame.time.Clock()
clock.tick(FPS)

class Form(QWidget):

    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        # Create widgets
        self.setMinimumSize(200, 150)
        self.setMaximumSize(250, 250)
        self.setWindowTitle("WellDone")
        self.time_edit = QLineEdit("00:00:00")
        self.time_edit.setObjectName("time_edit")
        self.time_edit.setAlignment(QtCore.Qt.AlignCenter)
        self.time_edit.setStyleSheet('''QLineEdit#time_edit{
                                        background-color: rgba(198, 160, 246, 0);
                                        height: 70px;
                                        color: rgb(110,115,141);
                                        font-family: "DS-Digital";
                                        font-size: 48px;
                                        border: solid;
                                        border-width: 0px;             
                                        }                                         
                                        ''')

        self.btn_start = QPushButton("Старт")
        self.btn_start.setObjectName("btn_start")
        self.btn_start.setStyleSheet('''QPushButton#btn_start {
                                        background-color: rgb(183, 189, 248);
                                        height: 24px;
                                        color: white;
                                        border: solid;
                                        border-width:1px;
                                        border-radius: 2px;
                                        font-family: "Roboto";
                                        border-color: rgb(91, 96, 120);
                                        font-size: 16px;
                                        margin-left:40px;
                                        margin-right:40px;
                                        }
                                        QPushButton#btn_start:hover{
                                        background-color: rgb(178, 173, 248);
                                        }
                                        QPushButton#btn_start:pressed{
                                        background-color: rgba(178, 173, 248, 0.3)
                                        }''')
        self.btn_stop = QPushButton("Стоп")
        self.btn_stop.setObjectName("btn_stop")
        self.btn_stop.setStyleSheet('''QPushButton#btn_stop{
                                        background-color: rgb(183, 189, 248);
                                        height: 24px;
                                        color: white;
                                        border: solid;
                                        border-radius: 2px;
                                        font-family: "Roboto";
                                        border-width:1px;
                                        border-color: rgb(91, 96, 120);
                                        font-size: 16px;
                                        margin-left:40px;
                                        margin-right:40px;
                                        }
                                        QPushButton#btn_stop:hover{
                                        background-color: rgb(178, 173, 248);
                                        }
                                        QPushButton#btn_stop:pressed{
                                        background-color: rgba(178, 173, 248, 0.3)
                                        }
                                                ''')
        self.btn_reset = QPushButton("Сброс")
        self.btn_reset.setObjectName("btn_reset")
        self.btn_reset.setStyleSheet('''QPushButton#btn_reset{
                                        background-color: rgb(183, 189, 248);
                                        height: 24px;
                                        color: white;
                                        border: solid;
                                        border-radius: 2px;
                                        font-family: "Roboto";
                                        border-width:1px;
                                        border-color: rgb(91, 96, 120);
                                        font-size: 16px;
                                        margin-left:40px;
                                        margin-right:40px;
                                        }
                                        QPushButton#btn_reset:hover{
                                        background-color: rgb(178, 173, 248);
                                        }
                                        QPushButton#btn_reset:pressed{
                                        background-color: rgba(178, 173, 248, 0.3)
                                        }
                                                ''')
        # Create layout and add widgets
        layout_main = QVBoxLayout()
        layout_main.addWidget(self.time_edit)
        layout_main.addWidget(self.btn_start)
        layout_main.addWidget(self.btn_stop)
        layout_main.addWidget(self.btn_reset)
        # Set dialog layout
        self.setLayout(layout_main)
        # Add button signal to greetings slot
        self.timer = QtCore.QTimer()
        self.timer.setInterval(1000)# 1 сек.
        self.timer.timeout.connect(self.timer3)
        self.btn_start.clicked.connect(self.action_btn_start)
        self.btn_stop.clicked.connect(self.action_btn_stop)
        self.btn_reset.clicked.connect(self.action_btn_reset)



    def action_btn_start(self):
        self.text = self.time_edit.text()
        self.text = datetime.strptime(self.text, "%H:%M:%S").time()
        self.timer.start()
        
    def action_btn_reset(self):
        self.timer.stop()
        self.time_edit.setText("00:00:00")
        pygame.mixer.music.stop()

    def action_btn_stop(self):
        self.timer.stop()
        pygame.mixer.music.stop()

    def timer3(self):         
        if self.text.second == 00 and self.text.minute == 00:
            if self.text.hour != 00:
                    self.text = self.text.replace(hour=self.text.hour - 1)
                    self.text = self.text.replace(minute=59)
                    self.text = self.text.replace(second=59)
            else:
                self.timer.stop()
                pygame.mixer.music.play(0)
        elif self.text.second == 00:
            self.text = self.text.replace(minute=self.text.minute - 1, second=59)
        elif self.text.second != 00:
            self.text = self.text.replace(second=self.text.second - 1)
        self.time_edit.setText(str(self.text))


if __name__ == '__main__':
    # Create the Qt Application
    app = QApplication(sys.argv)
    # Create and show the form
    form = Form()
    form.show()
    # Run the main Qt loop
    sys.exit(app.exec())

