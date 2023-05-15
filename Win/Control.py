from subprocess import Popen

from kivy.config import Config
from kivymd.uix.button import MDRaisedButton, MDFloatingActionButton, MDFillRoundFlatButton, MDIconButton, \
    MDFillRoundFlatIconButton
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

class ControlApp(MDApp):
    table = ""
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

        def update(instance):
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

        def empl_new(inst):
            p = Popen('AddWin\\EmplAdd.py', shell=True)

        def chempl(inst):
            p = Popen('ChWin\\EmplCh.py', shell=True)

        def delete_empl(inst):
            p = Popen('DelWin\\EmplDel.py', shell=True)


        def empl(inst):
            self.delete_table(screen)
            self.table = "employee"
            Table_empl = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                       size_hint=(.9, 0.6),
                                       use_pagination=True,
                                       column_data=get_columns(SQL.query(my_cursor, describe + "employee")),
                                       row_data=get_rows(SQL.query(my_cursor, select_all + "employee")),
                                       )
            but_add = MDIconButton (
                icon="plus",
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=empl_new
            )
            but_comm = MDIconButton(
                icon="pencil-outline",
                pos_hint={"center_x": 0.9, "center_y": 0.1},
                on_press=chempl
            )
            but_up = MDIconButton(
                icon="update",
                pos_hint={"center_x": 0.7, "center_y": 0.1}, on_press=update
            )
            but_del = MDIconButton(
                icon="delete",
                pos_hint={"center_x": 0.6, "center_y": 0.1}, on_press=delete_empl
            )
            but_sal = MDFillRoundFlatIconButton(text='Пересчетать зарплаты',
                                                size_hint=BTN_SIZE,
                                                pos_hint={'x': 0.1, 'y': 0.05}, on_press=sal, icon="cash-multiple")

            screen.add_widget(but_comm)
            screen.add_widget(but_del)
            screen.add_widget(but_up)
            screen.add_widget(but_add)
            screen.add_widget(but_sal)
            screen.add_widget(Table_empl)

        new_empl = MDFillRoundFlatIconButton(text='Сотрудники',
                                  size_hint=BTN_SIZE,
                                  pos_hint={'x': 0.4, 'y': 0.85}, on_press=empl, icon="account")
        def add_param(inst):
            p = Popen('AddWin\\ParamAdd.py', shell=True)

        def chparam(inst):
            p = Popen('ChWin\\ParamCh.py', shell=True)

        def delete_param(inst):
            p = Popen('DelWin\\ParamDel.py', shell=True)

        def param(inst):
            self.delete_table(screen)
            self.table = "type_of_parameter"
            Table_params = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                     size_hint=(.9, 0.6),
                                     use_pagination=True,
                                     column_data=get_columns(SQL.query(my_cursor, describe + "type_of_parameter")),
                                     row_data=get_rows(SQL.query(my_cursor, select_all + "type_of_parameter")))
            but_add = MDIconButton(
                icon="plus",
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=add_param
            )
            but_comm = MDIconButton(
                icon="pencil-outline",
                pos_hint={"center_x": 0.9, "center_y": 0.1},
                on_press=chparam
            )
            but_up = MDIconButton(
                icon="update",
                pos_hint={"center_x": 0.7, "center_y": 0.1}, on_press=update
            )
            but_del = MDIconButton(
                icon="delete",
                pos_hint={"center_x": 0.6, "center_y": 0.1}, on_press=delete_param
            )
            screen.add_widget(but_comm)
            screen.add_widget(but_del)
            screen.add_widget(but_up)
            screen.add_widget(but_add)
            screen.add_widget(Table_params)

        new_param = MDFillRoundFlatIconButton(text='Параметры',
                                  size_hint=BTN_SIZE,
                                  pos_hint={'x': 0.7, 'y': 0.85}, on_press=param, icon="tune")

        def add_sens(inst):
            p = Popen('AddWin\\SensAdd.py', shell=True)

        def chsens(inst):
            p = Popen('ChWin\\SensCh.py', shell=True)

        def delete_sens(inst):
            p = Popen('DelWin\\SensDel.py', shell=True)

        def sal(inst):
            p = Popen('Win\\sal.py', shell=True)

        def sens(inst):
            self.delete_table(screen)
            self.table = "type_of_sensor"
            Table_sens = MDDataTable(pos_hint={'center_x': 0.5, 'center_y': 0.5},
                                     size_hint=(.9, 0.6),
                                     use_pagination=True,
                                     column_data=get_columns(SQL.query(my_cursor, describe + "type_of_sensor")),
                                     row_data=get_rows(SQL.query(my_cursor, select_all + "type_of_sensor")))
            but_add = MDIconButton(
                icon="plus",
                pos_hint={"center_x": 0.8, "center_y": 0.1},
                on_press=add_sens
            )
            but_comm = MDIconButton(
                icon="pencil-outline",
                pos_hint={"center_x": 0.9, "center_y": 0.1},
                on_press = chsens
            )
            but_up = MDIconButton(
                icon="update",
                pos_hint={"center_x": 0.7, "center_y": 0.1}, on_press=update
            )
            but_del = MDIconButton(
                icon="delete",
                pos_hint={"center_x": 0.6, "center_y": 0.1}, on_press=delete_sens
            )
            screen.add_widget(but_comm)
            screen.add_widget(but_del)
            screen.add_widget(but_up)
            screen.add_widget(but_add)
            screen.add_widget(Table_sens)

        new_sens = MDFillRoundFlatIconButton(text='Сенсоры',
                                   size_hint=BTN_SIZE,
                                   pos_hint={'x': 0.1, 'y': 0.85}, on_press=sens, icon="leak")



        screen.add_widget(new_empl)
        screen.add_widget(new_param)
        screen.add_widget(new_sens)
        return screen

    def checked(self, instance_table, current_row):
        print('Checked')
        print(instance_table, current_row)
        print(self.LIST_TO_DELETE)
        # Function for row presses

    def row_checked(self):
        print('Selected Row')
        if self.table == "employee":
            print("empl")
        if self.table == "type_of_sensor":
            print("type_of_sensor")
            p = Popen('ChWin\\ParamCh.py', shell=True)

if __name__ == '__main__':
    ControlApp().run()