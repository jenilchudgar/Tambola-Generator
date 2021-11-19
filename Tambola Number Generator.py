import pyttsx3,sys
from random import Random
from PyQt5.QtWidgets import QApplication,QLabel,QPushButton,QMainWindow
from PyQt5 import uic

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[0])
engine.setProperty('rate',130)

class UI(QMainWindow):
    def __init__(self):
        super(UI,self).__init__()
        uic.loadUi("Tambola Number Generator.ui",self)
        self.numbersDone = []
        self.number = self.findChild(QLabel,"label")
        self.numbersDoneLabel = self.findChild(QLabel,"label_2")
        self.button = self.findChild(QPushButton,"pushButton_2")
        self.button.clicked.connect(lambda:self.click())
        self.show()
    def speak(self,audio:str):
        engine.say(audio)
        engine.runAndWait()

    def getNumber(self):
        val = Random().randint(1,90)
        if val not in self.numbersDone:
            self.numbersDone.append(val)
            return val
            

    def click(self):
        print(len(self.numbersDoneLabel.text()))
        num = self.getNumber()
        if num==None:
            try:
                self.click()
            except:
                self.numbersDoneLabel.setText("All Numbers Done!\nReset After Next Click")
                self.number.setText("0")
                self.numbersDone.clear()
                return
        else:
            self.number.setText(str(num))
            self.speak(str(num))
            self.numbersDoneLabel.setText(str(self.numbersDone).replace("[","").replace("]",""))

if __name__ == "__main__":
    app=QApplication(sys.argv)
    UIWindow=UI()
    app.exec_()