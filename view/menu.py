from PyQt5.QtWidgets import (QMenuBar, QMenu, QAction)

class Menu(QMenuBar):

    def __init__(self, parent, on_inspector, on_items, on_json_editor):
        super().__init__(parent)

        files_menu = QMenu("&Files", self)
        self.addMenu(files_menu)
        
        new_mod = QAction('New Mod', self)
        # new_mod.triggered.connect(on_new_mod)
        files_menu.addAction(new_mod)

        save_mod = QAction('Save Mod', self)
        # save_mod.triggered.connect(on_save_mod)
        files_menu.addAction(save_mod)

        save_mod_as = QAction('Save Mod As', self)
        # save_mod_as.triggered.connect(on_save_mod_as)
        files_menu.addAction(save_mod_as)

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
