#encoding: utf-8
import maya.utils
import maya.cmds as cmds

# メニュー定義
def createMenu():
    cmds.setParent('MayaWindow')
    cmds.menu(label='test_commands', tearOff=True)
    cmds.menuItem(l='test_window', command='import test_window; reload(test_window); test_window.show()')

# メニュー作成
maya.utils.executeDeferred(createMenu)