from qtpy import QtCore, QtGui, QtWidgets
from maya.app.general.mayaMixin import MayaQWidgetBaseMixin
from maya.app.general.mayaMixin import MayaQWidgetDockableMixin

try:
    from shiboken2 import wrapInstance 

except:
    from shiboken import wrapInstance

def get_maya_pointer():
    from maya import OpenMayaUI
    return wrapInstance(long(OpenMayaUI.MQtUtil.mainWindow()), QtWidgets.QWidget)

maya_win = get_maya_pointer()
maya_base_mixin = MayaQWidgetBaseMixin
maya_dockable_mixin = MayaQWidgetDockableMixin