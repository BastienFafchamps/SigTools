from typing import Text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QBoxLayout, QLabel, QFormLayout, QLineEdit, QTextEdit, QSpinBox
from view.inspector_layout import InspectorLayout
import re


class SigWidgets():

    def __init__(self) -> None:
        self._widgets = {}
        self._widgets['string'] = self.__add_string
        self._widgets['number'] = self.__add_number

    def get_widgets(self, template):
        layout = InspectorLayout('Inspector')
        layout.addRow(self.__to_label('test'), QLineEdit())
        layout.addRow(self.__to_label('testB'), QLineEdit())

        layoutb = InspectorLayout(no_margins=True)
        layoutb.addRow(self.__to_label('test'), QLineEdit())
        layoutb.addRow(self.__to_label('test'), QLineEdit())
        
        layout.addRow('testB', layoutb)

        return self.__get_widgets(layout, template)

    def __get_widgets(self, layout, template):
        # for key in template:
        #     if (type_data['type'] in self._widgets):
        #         self._widgets[type_data['type']](layout, type_data)
        #     else:
        #         print(f'Type {type_data["type"]} not found')

        return layout

    def __to_label(self, value):
        value = re.sub(r"(\w)([A-Z])", r"\1 \2", value)
        value = value.capitalize()
        return value

    def __add_string(self, layout, type_data):
        layout.addRow(self.__to_label(type_data['name']), QLineEdit())
    
    def __add_number(self, layout, type_data):
        layout.addRow(self.__to_label(type_data['name']), QSpinBox())
