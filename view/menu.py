from PyQt5.QtWidgets import (QMenuBar, QMenu, QAction)

class Menu(QMenuBar):

    def __init__(self, parent, on_inspector, on_items, on_json_editor):
        super().__init__(parent)

        views_menu = QMenu("&Views", self)
        self.addMenu(views_menu)

        inspector = QAction('Inspector', self)
        inspector.triggered.connect(on_inspector)
        views_menu.addAction(inspector)

        items = QAction('Items', self)
        items.triggered.connect(on_items)
        views_menu.addAction(items)

        json_editor = QAction('Json Editor', self)
        json_editor.triggered.connect(on_json_editor)
        views_menu.addAction(json_editor)
