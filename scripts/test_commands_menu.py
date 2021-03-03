#encoding: utf-8

import maya.cmds as cmds
import reloadable_menu

def show_message(message):
    print(message)
    cmds.inViewMessage(assistMessage=message,
                        position='midCenter',
                        fade=True,
                        # fadeStayTime=3000,
                        )

@reloadable_menu.reloadable_menu('Test Commands')
def create_menu():
    # cmds.setParent('MayaWindow')
    # cmds.menu(label='Test Commands', tearOff=True)
    # cmds.menuItem(l='test command 1', command='show_message("test command 1")')
    # cmds.menuItem(l='test command 2', command='show_message("test command 2")')
    cmds.menuItem(label='Test Window', command='import test_window; reload(test_window); test_window.show()')
