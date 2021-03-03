import functools
from mayaqt import *
import qtawesome

icons = [
    'building',
    'bookmark',
    'comment-dots',
    'calendar',
    'angry',
    'hand-point-left',
    'hourglass',
    'object-ungroup',
    'snowflake',
    'user-circle',
]

def print_(s):
    print(s)

class TestWindow(maya_dockable_mixin, QtWidgets.QWidget):
    
    def __init__(self, parent=None):
        super(TestWindow, self).__init__(parent)
        self.setWindowTitle('test winidow')
        self.setWindowFlags(QtCore.Qt.Window|QtCore.Qt.WindowCloseButtonHint)
        lo = QtWidgets.QVBoxLayout()
        lo.setContentsMargins(2,2,2,2)
        lo.setSpacing(2)
        self.setLayout(lo)
        self.resize(300, 400)
            
        for iconname in icons:
            icon = qtawesome.icon('fa5.{}'.format(iconname), color='lightgray')
            btn = QtWidgets.QPushButton()
            btn.setIcon(icon)
            btn.setIconSize(QtCore.QSize(32, 32))
            btn.clicked.connect(functools.partial(print_, iconname))
            lo.addWidget(btn)
            
        lo.addStretch()

def show():
    win = TestWindow(maya_win)
    win.show(dockable=True)
