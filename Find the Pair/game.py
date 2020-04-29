from PyQt5.QtWidgets import QApplication, QMainWindow,QGridLayout
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QUrl, Qt
import sys
import os,random,win32api,win32con
global a
a=[]
for root, dirs, files in os.walk('./img'):   
        a=files*2 #当前路径下所有非目录子文件
global b
b=''
global d
d=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
global count,play_1,play_2
count=0
play_1=0
play_2=0
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1047, 813)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(20, 10, 191, 161))
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_1.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_1.clicked.connect(lambda:self.setimg("1"))

        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(830, 10, 191, 161))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_2.clicked.connect(lambda:self.setimg("2"))
        
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 10, 191, 161))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_3.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_3.clicked.connect(lambda:self.setimg("3"))
        
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(290, 10, 191, 161))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_4.clicked.connect(lambda:self.setimg("4"))
        
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(20, 190, 191, 161))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_5.clicked.connect(lambda:self.setimg("5"))
        
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(830, 190, 191, 161))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_6.clicked.connect(lambda:self.setimg("6"))
        
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(570, 190, 191, 161))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_7.clicked.connect(lambda:self.setimg("7"))
        
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(290, 190, 191, 161))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_8.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_8.clicked.connect(lambda:self.setimg("8"))
        
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(20, 370, 191, 161))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_9.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_9.clicked.connect(lambda:self.setimg("9"))
        
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(830, 370, 191, 161))
        self.pushButton_10.setObjectName("pushButton_10")
        self.pushButton_10.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_10.clicked.connect(lambda:self.setimg("10"))
        
        self.pushButton_11 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_11.setGeometry(QtCore.QRect(570, 370, 191, 161))
        self.pushButton_11.setObjectName("pushButton_11")
        self.pushButton_11.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_11.clicked.connect(lambda:self.setimg("11"))
        
        self.pushButton_12 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_12.setGeometry(QtCore.QRect(290, 370, 191, 161))
        self.pushButton_12.setObjectName("pushButton_12")
        self.pushButton_12.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_12.clicked.connect(lambda:self.setimg("12"))
        
        self.pushButton_13 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_13.setGeometry(QtCore.QRect(20, 560, 191, 161))
        self.pushButton_13.setObjectName("pushButton_13")
        self.pushButton_13.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_13.clicked.connect(lambda:self.setimg("13"))
        
        self.pushButton_14 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_14.setGeometry(QtCore.QRect(830, 560, 191, 161))
        self.pushButton_14.setObjectName("pushButton_14")
        self.pushButton_14.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_14.clicked.connect(lambda:self.setimg("14"))
        
        self.pushButton_15 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_15.setGeometry(QtCore.QRect(570, 560, 191, 161))
        self.pushButton_15.setObjectName("pushButton_15")
        self.pushButton_15.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_15.clicked.connect(lambda:self.setimg("15"))
        
        self.pushButton_16 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_16.setGeometry(QtCore.QRect(290, 560, 191, 161))
        self.pushButton_16.setObjectName("pushButton_16")
        self.pushButton_16.setStyleSheet("QPushButton{border-image: url(mr/1.jpg)}")
        self.pushButton_16.clicked.connect(lambda:self.setimg("16"))
        
        self.pushButton_17 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_17.setGeometry(QtCore.QRect(600, 750, 101, 41))
        self.pushButton_17.setObjectName("pushButton_17")
        self.pushButton_17.clicked.connect(self.stop)
        
        self.pushButton_18 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_18.setGeometry(QtCore.QRect(470, 750, 101, 41))
        self.pushButton_18.setObjectName("pushButton_18")
        self.pushButton_18.clicked.connect(self.pause)
        
        self.pushButton_19 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_19.setGeometry(QtCore.QRect(350, 750, 101, 41))
        self.pushButton_19.setObjectName("pushButton_19")
        self.pushButton_19.clicked.connect(self.play)
        
        url = QUrl.fromLocalFile(r"1.mp3")
        content = QtMultimedia.QMediaContent(url)
        self.player = QtMultimedia.QMediaPlayer()
        self.player.setMedia(content)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
    
    def stop(self):
        self.player.stop()
        
    def play(self):
        self.player.play()
        
    def pause(self):
        self.player.pause()
        
    
    def setimg(self,name):
        global a,b,d,count,play_1,play_2
        if a==[]:
            win32api.MessageBox(0,'游戏结束啦!\n玩家一得分：%s，玩家二得分：%s'%(play_1,play_2),"提醒",win32con.MB_ICONWARNING)
        else:
            if name in d:
                count+=1
                d.remove(name)
                buttonname="self.pushButton_%s"%name
                buttonname=eval(buttonname)
                if b=='':
                    b=random.choice(a)
                    a.remove(b)
                    buttonname.setStyleSheet("QPushButton{border-image: url(img/%s)}"%b)
                else:
                    c=random.choice(a)
                    a.remove(c)
                    buttonname.setStyleSheet("QPushButton{border-image: url(img/%s)}"%c)
                    if c==b:
                        if str(count) in ["2","6","10","14"]:
                            play_1+=1
                            win32api.MessageBox(0, "恭喜你选对了！可以继续游戏。\n当前玩家一得分：%s，玩家二得分：%s"%(play_1,play_2), "提醒",win32con.MB_OK)
                            b=''
                        else:
                            play_2+=1
                            win32api.MessageBox(0, "恭喜你选对了！可以继续游戏。\n当前玩家一得分：%s，玩家二得分：%s"%(play_1,play_2), "提醒",win32con.MB_OK)
                            b=''
                    else:
                        win32api.MessageBox(0,'很遗憾你没选对！下一位玩家', "提醒",win32con.MB_ICONWARNING)
                        b=''
            else:
                win32api.MessageBox(0,'你已经点过该图了！', "提醒",win32con.MB_ICONWARNING)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "点图大战"))
        self.player.play()
        self.pushButton_17.setText(_translate("MainWindow", "停止播放音乐"))
        self.pushButton_18.setText(_translate("MainWindow", "暂停播放音乐"))
        self.pushButton_19.setText(_translate("MainWindow", "继续播放音乐"))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    
