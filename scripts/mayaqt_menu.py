#encoding: utf-8

import maya.cmds as cmds
import reloadable_menu

@reloadable_menu.reloadable_menu('Qt')
def create_menu():
    cmds.menuItem(label='QtAwesome Icon Browser', command='import mayaqt.qtawesome_icon_browser as icon_browser; reload(icon_browser); icon_browser.main()')
