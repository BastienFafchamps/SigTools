from typing import Text
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QLabel, QFormLayout, QLineEdit, QTextEdit, QSpinBox
import re


class SigWidgets():

    def __init__(self) -> None:
        self._widgets = {}
        self._widgets['string'] = self.__add_string
        self._widgets['number'] = self.__add_number

    def get_widgets(self, types_data):
        layout = QFormLayout()

        for type_data in types_data:
            if (type_data['type'] in self._widgets):
                self._widgets[type_data['type']](layout, type_data)
            else:
                print(f'Type {type_data["type"]} not found')

        return layout

    def __to_label(self, value):
        value = re.sub(r"(\w)([A-Z])", r"\1 \2", value)
        value = value.capitalize()
        return value

    def __add_string(self, layout, type_data):
        layout.addRow(self.__to_label(type_data['name']), QLineEdit())
    
    def __add_number(self, layout, type_data):
        layout.addRow(self.__to_label(type_data['name']), QSpinBox())
