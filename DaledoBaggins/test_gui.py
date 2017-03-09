from PyQt4 import QtGui
import pygame
import sys

class ImageWidget(QtGui.QWidget):
    def __init__(self,surface,parent=None):
        super(ImageWidget,self).__init__(parent)
        w=surface.get_width()
        h=surface.get_height()
        self.data=surface.get_buffer().raw
        self.image=QtGui.QImage(self.data,w,h,QtGui.QImage.Format_RGB32)

    def paintEvent(self,event):
        qp=QtGui.QPainter()
        qp.begin(self)
        qp.drawImage(0,0,self.image)
        qp.end()


class MainWindow(QtGui.QMainWindow):
    def __init__(self,surface,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setCentralWidget(ImageWidget(surface))


if __name__ == "__main__":
    pygame.init()
    s=pygame.Surface((640,480))
    s.fill((64,128,192,224))
    pygame.draw.circle(s,(255,255,255,255),(100,100),50)

    app=QtGui.QApplication(sys.argv)
    w=MainWindow(s)
    w.show()
    app.exec_()