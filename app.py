import sys

from data import Data
from view.widgets import SigWidgets
from view.item_view import ItemsView
from view.menu import Menu

from PyQt5.QtWidgets import (QApplication, QMainWindow, QGroupBox, QTabWidget, QDockWidget, QTextEdit, QStyleFactory)
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

from qt_material import apply_stylesheet
from pyqode.json.widgets import JSONCodeEdit

type_data = [
    {'type': 'string', 'name': 'nameOfTheItem'},
    {'type': 'number', 'name': 'value'},
    {'type': 'string', 'name': 'testValue'},
]

template = {
    "type": "SIG.Items.Item",
    "category": "item",
    "enabled": True,
    "id": "SeeItGrow:Carrot",
    "iconId": "Carrot_0",
    "displayName": {
        "values": []
    },
    "description": {
        "values": []
    },
    "unstackable": True,
    "tags": []
}

class Window(QMainWindow):

    def __init__(self):
        super().__init__()
        self.setGeometry(300, 100, 1200, 800)
        self.setWindowTitle('SIG Tool App')
        
        self.sig_widgets = SigWidgets()
        self.data = Data('CarrotMod')
        self.items = self.data.load_items()

        self.initUi()

    def initUi(self):
        self.create_menu_bar()
        self.json_editor()
        # self.setCentralWidget(QTextEdit())
        self.set_dock_inspector()
        self.set_dock_items()

        self.setDockOptions(QMainWindow.AnimatedDocks | QMainWindow.AllowNestedDocks)
        self.setTabPosition(Qt.DockWidgetArea.AllDockWidgetAreas, QTabWidget.TabPosition.North)

    def create_menu_bar(self):
        menu_bar = Menu(self, self.set_dock_inspector, self.set_dock_items, self.json_editor)
        self.setMenuBar(menu_bar)

    def json_editor(self):
        if (hasattr(self, 'json_editor_dock') and self.json_editor_dock.isVisible()):
            return

        self.json_editor_dock = QDockWidget('Json Editor', self)
        self.json_editor_dock.setFloating(False)

        self.json_editor = JSONCodeEdit(self)
        self.json_editor.syntax_highlighter.color_scheme = 'monokai'

        self.json_editor_dock.setWidget(self.json_editor)
        self.addDockWidget(Qt.DockWidgetArea.BottomDockWidgetArea, self.json_editor_dock)

    def set_dock_inspector(self):
        self.inspectorDock = QDockWidget('Inspector', self)

        inspector_layout = QGroupBox()
        inspector_form = self.sig_widgets.get_widgets(type_data)
        inspector_layout.setLayout(inspector_form)

        self.inspectorDock.setWidget(inspector_layout)
        self.inspectorDock.setFloating(False)
        self.addDockWidget(Qt.RightDockWidgetArea, self.inspectorDock)

    def set_dock_items(self):
        self.items_view = ItemsView('Items', self, self.items)
        self.items_view.set_on_item_selected(self.__select_item)
        self.addDockWidget(Qt.LeftDockWidgetArea, self.items_view)

    def __edit_item_json(self):
        if (self.current_item != None):
            self.data.set_item(self.current_item['path'], self.json_editor.toPlainText())

    def __select_item(self, item):
        if (item != None):
            self.current_item = item
            self.json_editor.setDisabled(False)
            self.json_editor.setPlainText(item['raw_text'])
        else:
            self.json_editor.setPlainText('')
            self.json_editor.setDisabled(True)

def window():
    app = QApplication(sys.argv)
    win = Window()
    win.show()

    # win.showMaximized()

    apply_stylesheet(app, theme='dark_amber.xml')

    sys.exit(app.exec_())

window()

