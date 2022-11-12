from djitellopy import Tello
import sys
import cv2

from PyQt5 import uic
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

me = Tello()
me.connect()
me.streamoff()
me.streamon()


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('movein.ui', self)

        self.kek = QTimer()
        self.kek.timeout.connect(self.update)
        self.kek.start(100)

    def update(self):
        img = me.get_frame_read().frame
        try:
            x,y = self.width(), self.height()
            img = cv2.resize(img, (x, y))
        except Exception as e:
            print(e)
        height, width, channel = img.shape
        bytesPerLine = 3 * width
        img = QImage(img.data, width, height, bytesPerLine, QImage.Format_BGR888)
        try:
            self.image.setPixmap(QPixmap(img))
        except Exception as e:
            print(e)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
