
from kivy.config import Config
Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '400')
from subprocess import Popen

from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton, MDFillRoundFlatButton, MDIconButton, \
    MDFloatingActionButtonSpeedDial, MDFillRoundFlatIconButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivymd import *
from kivymd.uix.taptargetview import MDTapTargetView
from kivy.uix.image import Image
from kivy.lang import Builder
from kivy.uix import dropdown
from kivymd.app import *
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
import webbrowser

BTN_SIZE = (.14, .1)


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

    def delete_table(self, screen):
        for child in screen.children:
            if type(child) == type(MDDataTable()):
                screen.remove_widget(child)

    def build(self):
        # Define Screen
        screen = FloatLayout()
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        self.title = 'Main'
        # Define Table
        def table_list(inst):
            p = Popen('Win\List.py', shell=True)


        def table_control(inst):
            p = Popen('Win\Control.py', shell=True)

        def new(inst):
            p = Popen('AddWin\ResAdd.py', shell=True)

        def warn(inst):
            webbrowser.open("https://www.tinkoff.ru/cf/8s8RSHqPFTd")

        List = MDFillRoundFlatIconButton(text='Список задач',
                              size_hint=BTN_SIZE,
                              pos_hint={'x': 0.7, 'y': 0.5},
                              on_press=table_list,
                              icon="book"
                              )


        New = MDFillRoundFlatIconButton(text='Новая задача',
                                 size_hint=BTN_SIZE,
                                 pos_hint={'x': 0.05, 'y': 0.5},
                             on_press=new,
                             icon="checkbox-marked-circle-plus-outline"
                             )

        Donate = MDIconButton(
            icon="account-cash-outline",
            pos_hint={"center_x": 0.5, "center_y": 0.43},
            on_press=warn
        )
        screen.add_widget(List)
        screen.add_widget(Donate)
        screen.add_widget(New)
        return screen

    def checked(self, instance_table, current_row):
        print('Checked')
        print(instance_table, current_row)
        self.LIST_TO_DELETE.append(current_row)
        print(self.LIST_TO_DELETE)
        # Function for row presses

    def row_checked(self, instance_table, instance_row):
        print('Selected Row')
        print(instance_table, instance_row)


if __name__ == '__main__':
    MainApp().run()
