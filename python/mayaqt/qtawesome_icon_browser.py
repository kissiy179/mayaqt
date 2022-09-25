# encoding: UTF-8
from pprint import pprint
from . import maya_base_mixin, QtWidgets
import qtawesome.icon_browser as icon_browser; reload(icon_browser)

class QtAwesome_IconBrowser(maya_base_mixin, QtWidgets.QMainWindow):
    
    def __init__(self, parent=None):
        super(QtAwesome_IconBrowser, self).__init__(parent)
        self.setWindowTitle('QtAwesome Icon Browser')
        wgt = icon_browser.IconBrowser()
        self.setCentralWidget(wgt)
    
def main():
    win = QtAwesome_IconBrowser()
    win.show()