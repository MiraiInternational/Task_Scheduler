from subprocess import Popen

from kivy.config import Config
from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton, MDFillRoundFlatButton, MDIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.menu import MDDropdownMenu

Config.set('graphics', 'width', '1200')
Config.set('graphics', 'height', '600')
from kivy.lang import Builder
from kivy.uix import dropdown
from kivymd.app import MDApp
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.checkbox import CheckBox
from kivy.uix.spinner import Spinner
from kivymd.uix.floatlayout import FloatLayout
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
import SQL
from SQL import *
from config import *
import AddWindow

def get_columns(data):
    columns = []
    for row in data:
        columns.append([row[0], dp(50)])
    print(columns)
    return columns


def get_rows(data):
    rows = []
    for row in data:
        rows.append(row)
    return rows



class MainApp(MDApp):
    table = ""

    def delete_table(self, screen):
        for child in screen.children:
            if type(child) == type(MDDataTable()):
                screen.remove_widget(child)

    def build(self):
        screen = FloatLayout()
        self.delete_table(screen)
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        SQL.my_cursor.callproc('sal_empl')
        for i in my_cursor.stored_results(): results = i.fetchall()
        table = MDDataTable(
            pos_hint={'center_x': 0.5, 'center_y': 0.5},
            size_hint=(.9, 0.6),
            use_pagination=True,
            column_data=[
                ("Name", dp(64)),
                ("Salary", dp(64)),
            ],
            row_data=get_rows(results)
        )
        screen.add_widget(table)
        return screen

if __name__ == '__main__':
    MainApp().run()