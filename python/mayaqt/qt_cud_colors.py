import cud_colors
from . import *

print cud_colors.accent_colors.values()
accent_colors = [QtGui.QColor(*values) for values in cud_colors.accent_colors.values()]
base_colors = [QtGui.QColor(*values) for values in cud_colors.base_colors.values()]
achromatic_colors = [QtGui.QColor(*values) for values in cud_colors.achromatic_colors.values()]
all_colors = [QtGui.QColor(*values) for values in cud_colors.all_colors.values()]
