from kivy.config import Config

Config.set('graphics', 'width', '600')
Config.set('graphics', 'height', '500')

from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.banner import MDBanner
from kivymd.uix.button import MDRaisedButton
from kivymd.uix.fitimage import FitImage
from kivymd.uix.pickers import MDDatePicker, MDTimePicker
from kivymd.uix.textfield import MDTextField
from kivymd.uix.floatlayout import FloatLayout
import SQL

BTN_SIZE = (.14, .1)


class New_Research(MDApp):

    def build(self):
        screen = FloatLayout()
        screen.add_widget(FitImage(source='pic\\1618529499_62-funart_pro-p-oboi-fon-material-dizain-62.png'))
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_pallete = "Orange"
        self.title = 'Add task'
        pk_list = [el[0] for el in SQL.query(SQL.my_cursor, 'SELECT № from tasks')]
        def has_numbers(inputString):
            return any(char.isdigit() for char in inputString)

        def validate():
            But2.disabled = Field1.error

        def error_1(instance, value):
            Field1.error = False
            if Field1.text != "":
                try:
                    int(Field1.text)
                    if int(Field1.text) in pk_list:
                        Field1.helper_text = 'Этот № уже используется'
                        Field1.error = True
                except ValueError:
                    Field1.error = True
                    Field1.helper_text = '№ должен быть INT'
            else:
                Field1.error = True
            validate()

        def save(inst, value, date_range):
            Field4.text = str(value)
            show_time()

        def save_time(inst, value):
            Field4.text += " " + str(value)
            Field4.error = False
            validate()

        def show_date():
            date_dialog = MDDatePicker(year=2023, month=1, day=1)
            date_dialog.bind(on_save=save)
            date_dialog.open()

        def on_focus(inst, value):
            if value:
                if inst == Field4:
                    show_date()

        def show_time():
            time_dialog = MDTimePicker()
            time_dialog.bind(on_save=save_time)
            time_dialog.open()

        Field1 = MDTextField(
            hint_text="№",
            pos_hint={"x": 0.05, "y": 0.7},
            size_hint={0.6, 0.05},
            multiline=False,
            helper_text_mode='on_error',
            max_text_length=64,
            required=True
        )
        def test(inst, value):
            print(Field2.text)
        Field2 = MDTextField(
            hint_text="Task",
            pos_hint={"x": 0.05, "y": 0.6},
            size_hint={0.6, 0.05},
            multiline=False,
            helper_text_mode='on_error',
            max_text_length=64,
            required=True
        )
        Field2.bind(on_focus=test)

        Field3 = MDTextField(
            hint_text="Description",
            pos_hint={"x": 0.05, "y": 0.5},
            size_hint={0.6, 0.05},
            multiline=False,
            max_text_length=20
        )


        Field4 = MDTextField(
            hint_text="Time",
            pos_hint={"x": 0.05, "y": 0.4},
            size_hint={0.6, 0.05},
            multiline=False,
            max_text_length=20,
            helper_text_mode='on_error'
        )

        Field4.bind(focus=on_focus)
        def new(instance):
            print(f'INSERT INTO tasks VALUES ({Field1.text},'
              f'\'{Field2.text}\',\'{Field3.text}\',{str(Field4.text)})')
            SQL.query(SQL.my_cursor, f'INSERT INTO tasks VALUES ({int(Field1.text)},'
                                     f'\'{Field2.text}\',\'{Field3.text}\',\'{Field4.text}\')')
            SQL.mydb.commit()
            MDApp.get_running_app().stop()


        But2 = MDRaisedButton(
            text='Применить',
            size_hint=BTN_SIZE,
            pos_hint={"x": 0.81, "y": 0.05},
            on_release=new,
            disabled=True
        )

        screen.add_widget(Field1)
        screen.add_widget(Field2)
        screen.add_widget(Field3)
        screen.add_widget(Field4)
        screen.add_widget(But2)
        return screen


if __name__ == "__main__":
    New_Research().run()