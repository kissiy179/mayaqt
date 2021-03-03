#encoding: utf-8
import maya.utils
import maya.cmds as cmds

def show_message(message):
    print(message)
    cmds.inViewMessage(assistMessage=message,
                        position='midCenter',
                        fade=True,
                        # fadeStayTime=3000,
                        )


# メニュー定義
def create_menu():
    cmds.setParent('MayaWindow')
    cmds.menu(label='test commands', tearOff=True)
    # cmds.menuItem(l='test command 1', command='show_message("test command 1")')
    # cmds.menuItem(l='test command 2', command='show_message("test command 2")')
    cmds.menuItem(l='test window', command='import test_window; reload(test_window); test_window.show()')

# メニュー作成
maya.utils.executeDeferred(create_menu)