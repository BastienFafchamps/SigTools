from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QBoxLayout, QVBoxLayout, QLabel, QFormLayout, QDialog, QWidget


class InspectorLayout(QVBoxLayout):

    def __init__(self, title=None, parent=None, no_margins=False):
        super().__init__(parent)

        if (title is not None):
            title = QLabel(text=title)
            self.addWidget(title)

        widget = QWidget()
        self.form_layout = QFormLayout()
        
        if (no_margins):
            self.form_layout.setContentsMargins(0, 0, 0, 0)

        widget.setLayout(self.form_layout)
        self.addWidget(widget)
        self.addStretch()
    
    def addRow(self, label, widget):
        self.form_layout.addRow(label, widget)