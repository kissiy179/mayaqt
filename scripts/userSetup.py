#encoding: utf-8
import maya.utils
import maya.cmds as cmds
import mayaqt_menu as mayaqt_menu

# メニュー作成
maya.utils.executeDeferred(mayaqt_menu.create_menu)