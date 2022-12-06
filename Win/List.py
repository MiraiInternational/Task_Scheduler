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
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        self.table="research"
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        Table_list = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                 size_hint=(.9, 0.6),
                                 use_pagination=True,
                                 column_data=get_columns(SQL.query(my_cursor, describe + "research")),
                                 row_data=get_rows(SQL.query(my_cursor, select_all + "research")))

        def update(inst):
            self.delete_table(screen)
            newdb = mysql.connector.Connect(
                host=host,
                port=3306,
                user=user,
                password=password,
                db=db_name
            )
            newcur = newdb.cursor()
            table = MDDataTable(
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                size_hint=(.9, 0.6),
                use_pagination=True,
                column_data=get_columns(SQL.query(newcur, describe + self.table)),
                row_data=get_rows(SQL.query(newcur, select_all + self.table))
            )
            screen.add_widget(table)

        but_up = MDIconButton(
            icon="update",
            pos_hint={"center_x": 0.9, "center_y": 0.1}, on_press=update
        )
        def chlist(inst):
            p = Popen('ChWin\\ListCh.py', shell=True)

        but_comm = MDIconButton(
            icon="pencil-outline",
            pos_hint={"center_x": 0.8, "center_y": 0.1},
            on_press=chlist
        )
        def delete_(inst):
            p = Popen('DelWin\\ListDel.py', shell=True)

        but_del = MDIconButton(
            icon="delete",
            pos_hint={"center_x": 0.7, "center_y": 0.1}, on_press=delete_
        )
        screen.add_widget(but_up)
        screen.add_widget(but_del)
        screen.add_widget(Table_list)
        screen.add_widget(but_comm)
        return screen

if __name__ == '__main__':
    MainApp().run()