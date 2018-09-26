"""Make sure this directory is in your nuke plugin path  with your init.py"""


import nuke
import nukescripts

# Basic widget
from basic_widget import basic_widget

# Load Ui file
from load_ui_file import load_ui_file

# Regisered Widget
from registered_widget import registered_widget


megabrain = nuke.menu('Nuke').addMenu("ves_megabrain")
megabrain.addCommand("Basic Widget", 'basic_widget.start()')
megabrain.addCommand("Load ui example", 'load_ui_file.start()')
megabrain.addCommand("Open up registered widget as floating", 'registered_widget.start()')


nukescripts.panels.registerWidgetAsPanel('registered_widget.RegisteredWidget',
                                         'nuke copy_paste_example',
                                         'de.kombinat-13b.copy_paste_example',
                                         True).addToPane(nuke.getPaneFor('Properties.1'))