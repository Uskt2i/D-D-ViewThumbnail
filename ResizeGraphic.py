#!python3
# -*- coding: utf-8 -*-
import sys,cv2
import os.path
 
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

from OpencvProcessing import OpencvProcess

CURRENT_PATH = os.path.dirname(os.path.abspath(sys.argv[0]))
 
class UISample(QtWidgets.QMainWindow):
    def __init__(self, parent=None):
        super(UISample, self).__init__(parent)
 
        self.ui = QUiLoader().load(os.path.join(CURRENT_PATH, 'ResizeGraphic.ui'))
        self.setCentralWidget(self.ui)
        self.setAcceptDrops(True)
        # Signal作成
        #self.ui.pushButton_down.clicked.connect(self.click_btn)
        #self.ui.lineEdit.textChanged.connect(self.changeText)
        
    def click_btn(self):
        # 押したときの動作
        print("push!!")

    def changeText(self, text):
        # 押したときの動作
        print(text)
    def dropEvent(self,event):
        cv_test=OpencvProcess()
        #self.image=cv_test.openPic()
        mimedata_text=event.mimeData().text().replace("file:///","")
        print(mimedata_text)
        self.img=cv_test.openPic(mimedata_text)
        
        self.img=cv_test.thumbnail(self.img)
        self.img=cv_test.convertPic(self.img)
        height,width,channels=self.img.shape#必ずリサイズしてからサイズを計る
        print(height,width,channels)
        bytesPerLine = width * channels
        Qtimage=QtGui.QImage(self.img.data,width,height,bytesPerLine, QtGui.QImage.Format_RGB888)
        self.ui.label.setPixmap(QtGui.QPixmap.fromImage(Qtimage))
        #self.ui.widget.setMaximumSize(1280,720)#(width,height)
        print("conmplete")
    def dragEnterEvent(self,event):
        """
        ドラッグされたオブジェクトを許可するかどうかを決める
        ドラッグされたオブジェクトが、ファイルなら許可する
        """
        mime = event.mimeData()
        if mime.hasUrls() == True:
            event.accept()
        else:
            event.ignore()
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    a = UISample()
    a.show()
    sys.exit(app.exec_())