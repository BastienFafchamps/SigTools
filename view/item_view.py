from PyQt5.QtWidgets import (QDockWidget, QTreeView)
from PyQt5.QtGui import (QStandardItemModel, QStandardItem, QFont)

class ItemsView(QDockWidget):

    def __init__(self, title, parent, items):
        super().__init__(title, parent)
        self.setFloating(False)
        self.set_items(items)

    def set_items(self, items):
        self.items = items
        self.itemsTree = QTreeView()
        self.itemsTree.setHeaderHidden(True)

        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()

        groups = {}
        for item in items:
            category = item['data']['category']
            node = self.__get_node(item['name'])
            if (category not in groups):
                groups[category] = self.__get_node(category)
            groups[category].appendRow(node)
                
        for key in groups:
            rootNode.appendRow(groups[key])

        self.itemsTree.setModel(treeModel)
        self.itemsTree.expandAll()
        self.setWidget(self.itemsTree)

    def set_on_item_selected(self, method):
        self.itemsTree.selectionModel().selectionChanged.connect(lambda: method(self.__get_selected_item()))

    def __get_selected_item(self):
        current = self.itemsTree.currentIndex()
        found_item = None
        if (current.parent() != None):
            for item in self.items:
                if (item['name'] == current.data()):
                    found_item = item
        return found_item

    def __get_node(self, title):
        node = QStandardItem()
        node.setEditable(False)
        node.setText(title)
        return node
